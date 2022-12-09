import os
import sys
import time
import typing as t
import uuid

from dotenv import load_dotenv
from langchain.llms.base import LLM
from pychatgpt import Chat, Options
from pychatgpt.classes.exceptions import Auth0Exception
from pydantic import BaseModel

from ibl_ai_chatgpt_langchain.exceptions import IBLChatGPTError

load_dotenv()


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@singleton
class ChatClientContainer:
    def __init__(self):
        self.chat_clients = dict()  # org ids to clients
        self.timeout = 3600

    def get_chat(self, unique_id, email: t.Optional[str], passowrd: t.Optional[str]):
        client_data = self.chat_clients.get(unique_id)
        if not client_data.get("timestamp"):
            self.make_chat(unique_id, email, passowrd)
        elif time.time() > client_data["timestamp"] + 3600:
            self.make_chat(unique_id, client_data["email"], client_data["password"])
        return self.chat_clients["client"]

    def make_chat(self, unique_id: str, email: str, password: str, options=None):
        if options is None:
            options = Options()
        try:
            chat = Chat(
                email=email,
                password=password,
                options=options,
            )
            self.chat_clients[unique_id] = {
                "client": chat,
                "timestamp": time.time(),
                "email": email,
                "password": password,
            }
        except Auth0Exception as e:
            if "Password was incorrect" in str(e):
                raise IBLChatGPTError(
                    "It is likely you provided incorrect credentials. Check your email address and/or password."
                )
            elif "an access token" in str(e):
                raise IBLChatGPTError(
                    "Too many people are using ChatGPT right now, so please try again later! :3"
                )


class IBLChatGPT(LLM, BaseModel):
    openai_email: t.Optional[str] = os.environ.get("OPENAI_EMAIL")
    openai_password: t.Optional[str] = os.environ.get("OPENAI_PASSWORD")
    unique_id = uuid.uuid4().hex

    def __call__(self, prompt: str, stop=None) -> str:
        container = ChatClientContainer().get_chat(
            self.unique_id, self.openai_email, self.openai_password
        )
        chat = container.chat
        try:
            answer = chat.ask(prompt)
        except BaseException:
            container.refresh_chat()
            answer = chat.ask(prompt)
        return answer


if __name__ == "__main__":
    llm = IBLChatGPT()
    response = llm(sys.argv[1])
    print(response)

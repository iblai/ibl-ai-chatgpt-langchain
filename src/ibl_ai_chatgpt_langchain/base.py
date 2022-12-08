import os
import sys

from dotenv import load_dotenv
from langchain.llms.base import LLM
from pychatgpt import Chat, Options
from pychatgpt.classes.exceptions import Auth0Exception
from pydantic import BaseModel

from ibl_ai_chatgpt_langchain.exceptions import IBLChatGPTError

load_dotenv()
options = Options()


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
        self.chat = None
        self.refresh_chat()

    def refresh_chat(self):
        self.chat = self.make_chat()

    def make_chat(self):
        try:
            chat = Chat(
                email=os.environ["OPENAI_EMAIL"],
                password=os.environ["OPENAI_PASSWORD"],
                options=options,
            )
            return chat
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
    def __call__(self, prompt: str, stop=None) -> str:
        container = ChatClientContainer()
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

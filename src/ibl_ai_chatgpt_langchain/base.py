import os
import sys

from dotenv import load_dotenv
from langchain.llms.base import LLM
from pychatgpt.classes.exceptions import Auth0Exception
from pychatgpt import Chat, Options

from pydantic import BaseModel

from ibl_ai_chatgpt_langchain.exceptions import IBLChatGPTError

load_dotenv()


class IBLChatGPT(LLM, BaseModel):
    def __call__(self, prompt: str, stop=None) -> str:
        options = Options()
        try:
            chat = Chat(
                email=os.environ["OPENAI_EMAIL"], password=os.environ["OPENAI_PASSWORD"], options=options,
            )
        except Auth0Exception as e:
            if "Password was incorrect" in str(e):
                raise IBLChatGPTError(
                    "It is likely you provided incorrect credentials. Check your email address and/or password."
                )
            elif "an access token" in str(e):
                raise IBLChatGPTError(
                    "Too many people are using ChatGPT right now, so please try again later! :3"
                )
        answer = chat.ask(prompt)
        return answer


if __name__ == "__main__":
    llm = IBLChatGPT()
    response = llm(sys.argv[1])
    print(response)

import os
import sys

from dotenv import load_dotenv
from langchain.llms.base import LLM
from pyChatGPT import Chat
from exceptions import IBLChatGPTError
from pyChatGPT.classes.exceptions import Auth0Exception

load_dotenv()


class CustomLLM(LLM):
    def __call__(self, prompt: str) -> str:
        try:
            chat = Chat(email=os.environ["EMAIL"], password=os.environ["PASSWORD"])
        except Auth0Exception as e:
            if("Password was incorrect" in str(e)):
                raise IBLChatGPTError("It is likely you provided incorrect credentials. Check your email address and/or password.")
            elif("an access token" in str(e)):
                raise IBLChatGPTError("This is likely an issue with ChatGPT. Please try again later.")
        answer = chat.ask(prompt)
        return answer


llm = CustomLLM()

response  = llm(sys.argv[1])
print(response)

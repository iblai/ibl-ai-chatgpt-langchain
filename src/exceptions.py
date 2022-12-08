from pyChatGPT.classes.exceptions import Auth0Exception

class IBLChatGPTError(Auth0Exception):
    def __str__(self):
        return self.message
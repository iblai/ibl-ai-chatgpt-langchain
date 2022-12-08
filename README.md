# ChatGPT LangChain LLM

Creates a ChatGPT [LangChain](https://github.com/hwchase17/langchain) LLM model via [PyChatGPT](https://github.com/rawandahmad698/PyChatGPT).

## Installation

- Create a .env in the root directory
- Copy the content of the `.env.template` file to `.env` and update this file based on the text in each entry.
- Run `make setup`

## Credentials

The following openai credentials are required:

Sample .env file

```
EMAIL=info@ibleducation.com
PASSWORD=XXXX
```

## Usage

Here is an example:

```
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from ibl_ai_chatgpt_langchain.base import IBLChatGPT

# make an LLM
llm = IBLChatGPT()

# setup a prompt
prompt = PromptTemplate(
    input_variables=["country"],
    template="Do you like the national anthem of {country}?",
)

# make a chain
chain = LLMChain(llm=llm, prompt=prompt)

# ask ChatGPT if she likes the national anthem of the UK.
chain.run("the United Kingdom")
```

And here is the example output:

```
Out[5]: 'As a machine learning model, I do not have personal preferences or opinions. I am a neutral entity that processes and provides information based on my training and the inputs I receive. My purpose is to assist with information and answer questions to the best of my ability.'
```

# ChatGPT LangChain LLM

Creates a ChatGPT [LangChain](https://github.com/hwchase17/langchain) LLM model via [PyChatGPT](https://github.com/rawandahmad698/PyChatGPT).

## Installation (on existing axd manager)
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
>> Access Token missing or expired. Attempting to create them...
[OpenAI] Email address: does-not-exist@ibleducation.com
[OpenAI] Password: ********
[OpenAI] Beginning auth process
[OpenAI][1] Making request to https://chat.openai.com/auth/login
[OpenAI][1] Request was successful
[OpenAI][2] Beginning part two
[OpenAI][2] Grabbing CSRF token from https://chat.openai.com/api/auth/csrf
[OpenAI][2] Request was successful
[OpenAI][2] CSRF Token: fe3141b156f68bd8f827d85a697ebdc27fea5bdf6c0396d3a56813d
[OpenAI][3] Beginning part three
[OpenAI][3] Making request to https://chat.openai.com/api/auth/signin/auth0?prompt=login
[OpenAI][3] Request was successful
[OpenAI][4] Request was successful
[OpenAI][4] Current State: hKFo2SBIY0JwbHZUQkhtdFQ1NVpYNUp3SVNU1TaFur3VZkYjdDQXZZX1BfX3dQNzJhRWplODJtOGdWMF9pNk9ao2NpZNkgVGRKSWNiZTE2V29USHROOTVueXl3aDVFNHlPbzZJdEc
[OpenAI][5] Making request to https://auth0.openai.com/u/login/identifier?state=hK1TaXZlcnNhbC1sb2dpbqN0aWTZIGZkYjdDQXZZX1BfX3dQNzJhRWplODJtOGdWMF9pNk9ao2NpZNkgVGRKSWNiZTE2V29USHROOTVueXl3aDVFNHlPbzZJdEc
[OpenAI][5] Request was successful
[OpenAI][5] No captcha detected
[OpenAI][6] Making request to https://auth0.openai.com/u/login/identifier
[OpenAI][6] Email found
[OpenAI][7] Entering password...
[OpenAI][7] Password was correct
[OpenAI][7] Old state: hKFo2SasdDHZUQkhtdFQ1NVpYNUp3SVN0SWstU0FETDU1TaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIGZkYjdDQXZZX1BfX3dQNzJhRWplODJtOGdWMF9pNk9ao2NpZNkgVGRKSWNiZTE2V29USHROOTVueXl3aDVFNHlPbzZJdEc
[OpenAI][7] New State: fdb7CAvY_P__wP72d__dsa__a
[OpenAI][8] Making request to https://auth0.openai.com/authorize/resume?state=fdb7CdsaidaEje82m8gV0_i6OZ
[OpenAI][8] All good
[OpenAI][8] Access Token: ...
[OpenAI][9] Saving access token...
[OpenAI][8] Saved access token
Out[5]: 'As a machine learning model, I do not have personal preferences or opinions. I am a neutral entity that processes and provides information based on my training and the inputs I receive. My purpose is to assist with information and answer questions to the best of my ability.'
```

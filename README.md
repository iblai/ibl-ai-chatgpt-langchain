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
    input_variables=["tool"],
    template="What's the value of {tool} in education?",
)

# make a chain
chain = LLMChain(llm=llm, prompt=prompt)

# ask ChatGPT what she thinks about AI in education.
chain.run("AI")
```

And here is the example output:

```
The use of AI in education can potentially offer many benefits.
For example, AI-powered tutoring systems can provide personalized instruction to each student,
helping them to learn at their own pace and address any gaps in their knowledge.
AI can also be used to automate grading and administrative tasks,
freeing up teachers to focus on other aspects of their job.
Additionally, AI can be used to analyze large amounts of educational data and provide insights
that can help educators improve their teaching methods and better meet the needs of their students.
Overall,
the use of AI in education has the potential to enhance the learning experience and improve outcomes for students.
```

# ChatGPT LangChain LLM

Creates a ChatGPT [LangChain](https://github.com/hwchase17/langchain) LLM model via [PyChatGPT](https://github.com/rawandahmad698/PyChatGPT).

## Installation
- First, install the `ibl-ai-chatgpt-langchain` package using `pip` by running this command:
```
pip install ibl-ai-chatgpt-langchain
```
- Create a `.env` in the root directory of your project (e.g. if you use Django, the `.env` file should exist in the same directory as `manage.py`). In the `.env` file, put in your credentials, like below:
```
OPENAI_EMAIL=info@ibleducation.com
OPENAI_PASSWORD=XXXX
```
- (Optional) If you don't want to create a `.env` file or do not know where it should be placed, you can also export the credentials in your shell (like bash, zsh, etc). Just run the commands below:
```
export OPENAI_EMAIL=info@ibleducation.com
export OPENAI_PASSWORD=XXXX
```
- Aaand now we are good to go!


## Usage

Here is an example of me,

asking ChatGPT what she thinks about the value of AI in education:

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
The use of AI in education can potentially offer many benefits. For example, AI-powered tutoring
systems can provide personalized instruction to each student, helping them to learn at their own
pace and address any gaps in their knowledge. AI can also be used to automate grading and administrative
tasks, freeing up teachers to focus on other aspects of their job. Additionally, AI can be used to
analyze large amounts of educational data and provide insights that can help educators improve their
teaching methods and better meet the needs of their students. Overall, the use of AI in education has the
potential to enhance the learning experience and improve outcomes for students.
```

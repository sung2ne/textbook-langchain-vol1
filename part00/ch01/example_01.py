# LangChain 없이 OpenAI API 직접 호출
import openai
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "안녕하세요"}]
)
print(response.choices[0].message.content)

# LangChain으로 같은 작업
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o-mini")
print(llm.invoke("안녕하세요").content)

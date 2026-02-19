from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

class Person(BaseModel):
    name: str = Field(description="이름")
    age: int = Field(description="나이")

parser = PydanticOutputParser(pydantic_object=Person)
print(parser.get_format_instructions())

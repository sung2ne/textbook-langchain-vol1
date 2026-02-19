from langchain_core.output_parsers import JsonOutputParser

parser = JsonOutputParser()
print(parser.get_format_instructions())

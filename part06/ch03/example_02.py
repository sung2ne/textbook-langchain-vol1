from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(
    separator="\n\n",  # 빈 줄로 분할
    chunk_size=200,
    chunk_overlap=0,
)

chunks = splitter.split_text(text)

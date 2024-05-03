# from PyPDF2 import PdfReader
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
from time import sleep

# import os
# os.environ["OPENAI_API_KEY"] = "insert api key"

# reader = PdfReader('ilovepdf_merged.pdf')

# raw_text = ''
# for i, page in enumerate(reader.pages):
#     text = page.extract_text()
#     if text:
#         raw_text += text

# text_splitter = CharacterTextSplitter(
#     separator = "\n",
#     chunk_size = 1000,
#     chunk_overlap  = 200,
#     length_function = len,
# )
# texts = text_splitter.split_text(raw_text)

# embeddings = OpenAIEmbeddings()

# docsearch = FAISS.from_texts(texts, embeddings)

# from langchain.chains.question_answering import load_qa_chain
# from langchain.llms import OpenAI

# chain = load_qa_chain(OpenAI(), chain_type="stuff")
# query = "What is the selection cirteria for infosys"
# docs = docsearch.similarity_search(query)
# chain.run(input_documents=docs, question=query)
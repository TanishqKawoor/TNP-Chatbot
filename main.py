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

from flask import Flask, render_template, request, jsonify
import requests
import json
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("another.html")

@app.route('/webhook', methods= ['POST'])
def webhook():
    user_message = request.json['message']
    print("User message" , user_message)
    

    rasa_response = {"response": "Hi, this is a chatbot"}

    rasa_response_json = rasa_response.json()
    
    print("Rasa Response: ", rasa_response_json)
    return jsonify({"response": rasa_response})

if __name__ == "__main__":
    app.run(debug=True)
import os
import json
from sqlalchemy import create_engine, text
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import Document

os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

engine = create_engine("mssql+pymssql://@db-dev/AccountingDb")

with engine.connect() as conn:
    result = conn.execute(text("select JsonData from AccountingDocuments"))
    docs = []
    for row in result.mappings():
        data = json.loads(row['JsonData'])
        print(data)
        text_data = f"Document: {data['Description']}, Amount: {data['Amount']}, Date: {data['DocumentDate']}, Account Code: {data['AccountCode']}"
        docs.append(Document(page_content=text_data))

embedding_model = OpenAIEmbeddings()

vectorstore = FAISS.from_documents(docs, embedding_model)

retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
llm = ChatOpenAI(model_name="gpt-4", temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

while True:
    question = input("Ask: ")
    if question.lower() in ["exit", "quit"]:
        break
    answer = qa_chain.run(question)
    print("Answer:", answer)

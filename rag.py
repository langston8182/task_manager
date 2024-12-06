from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from pymongo.collection import Collection

from get_secrets import get_key_value

def setup_rag(connection_string: str, database_name: str, tasks_collection: Collection):
    """
    Configure le système RAG.

    Args:
        connection_string (str): Connexion à MongoDB.
        database_name (str): Nom de la base MongoDB.
        tasks_collection (Collection): La collection MongoDB où sont stockées les tâches.

    Returns:
        RetrievalQA: La chaîne de récupération augmentée par génération.
    """
    llm = ChatOpenAI(temperature=0, model="gpt-4-turbo", api_key=get_key_value("OPENAI_API_KEY"))
    embeddings = OpenAIEmbeddings(api_key=get_key_value("OPENAI_API_KEY"))

    # Configurer le stockage vectoriel
    mongo_vector_store = MongoDBAtlasVectorSearch(
        connection_string=connection_string,
        database_name=database_name,
        collection=tasks_collection,
        embedding=embeddings,
        index_name="tasks_index",
    )

    # Configurer la chaîne de récupération
    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    combine_docs_chain = create_stuff_documents_chain(llm, retrieval_qa_chat_prompt)
    retrieval_chain = create_retrieval_chain(
        retriever=mongo_vector_store.as_retriever(),
        combine_docs_chain=combine_docs_chain,
    )

    return retrieval_chain

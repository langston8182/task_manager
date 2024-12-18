from dotenv import load_dotenv
from langchain.agents import tool
from langchain_core.documents import Document
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_openai import OpenAIEmbeddings

from db_config import mongo_collection
from get_secrets import get_key_value

load_dotenv()
embeddings = OpenAIEmbeddings(api_key=get_key_value("OPENAI_API_KEY"))


@tool
def add_task(task: str) -> str:
    """
    Tu dois sauvegarder la tâche dans la base de données.
    Avant de sauvegarder la tâche, tu dois générer un identifiant unique pour la tâche que tu stockera dans l'attribut id.
    La tache est une string de type json.
    Voici le schéma de la tache :
    {
        "id": "identifiant de la tâche"
        "content": "nom de la tâche",
        "due_date": "date limite de la tâche" au format jj/mm/aaaa,
        "status": "statut de la tâche",
        "responsable": "responsable de la tâche"
    }
    Au début de la création de la tache le champ status doit être "en cours".
    si il y a une notion de temps dans la requete (exemple : aujourd'hui, demain, le 3/12/2014, ...), appelle l'outil adpaté.
    si la requête contient une référence à la première personne,
    comme "je", "j'", "ma", "mes", "moi" ou "mon". Si tu détectes une référence à la première personne,
    appelle l'outil approprié pour récupérer le nom de la personne.
    :param task: La tâche à ajouter au format json
    :return: message de confirmation. Je veux aussi que tu me renvoies le contenu de la tâche ajoutée avec le responsable est la date
    """
    try:
        documents = [Document(page_content=f"{task}")]
        MongoDBAtlasVectorSearch.from_documents(
            documents=documents,
            embedding=embeddings,
            collection=mongo_collection,
            index_name="task_index",
        )

        return "Task added successfully."
    except ValueError:
        return "Error when adding task."

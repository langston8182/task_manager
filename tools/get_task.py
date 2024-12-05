from dotenv import load_dotenv
from langchain.tools import tool

from db_config import database_name
from db_config import tasks_collection, connection_string
from rag import setup_rag

load_dotenv()

@tool
def get_task(query: str) -> str:
    """
    Tu dois récupérer des taches en rapport avec la question posée. Pour cela, tu dois utiliser le rag.
    Je veux aussi que tu recuperes l'id de la tache.
    Si dans la requete tu dois recuperer plusieurs taches, tu dois les recuperer toutes une par une en utilisant l'outil approprié.
    important : Si la demande est une mise à jour ou un changement, tu ne dois pas etre ici, tu dois utiliser l'outil approprié.
    Important :
    Si dans la requete il y a la notion de date, utilise le bon outil pour recuperer la date.
    Si dans la requete il y a une notion de date relative a la date du jour (ex : dans 3 jours, la semaine prochaine) alors on doit recuperer la date actuelle. Tu pourras alors utiliser la date actuelle pour faire ta recherche.
    exemple :
    Si la requete initiale est :
        Quelles sont les taches de Virginie a faire pour la semaine prochaine ?
    et que la date du jour est le 10/12/2024
    alors tu dois remplacer la requete par :
        Queles sont les taches de Virginie a faire pour du 10/12/2024 au 17/12/2024 ?
    :param query: La question posée
    :return: la réponse de l'assistant. Je veux que si il y a plusieurs taches tu me les donnes les unes sous les autres.
    """
    retrieval_chain = setup_rag(
        connection_string=connection_string,
        database_name=database_name,
        tasks_collection=tasks_collection,
    )
    result = retrieval_chain.invoke(input={"input": f"{query}"})

    return result["answer"]

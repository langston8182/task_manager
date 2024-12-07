from datetime import datetime

from dotenv import load_dotenv
from langchain.agents import tool

import user_context

load_dotenv()

@tool
def who_am_i(self) -> str:
    """
    Tu es un agent intelligent conçu pour analyser des requêtes en langage naturel.
    Ta tâche est d'identifier si une requête contient une référence à la première personne,
    comme "je", "j'", "ma", "mes", "moi" ou "mon". Si tu détectes une référence à la première personne,
    utilise le nom de la personne connectée. Remplace chaque mot faisant référence
    à la première personne par le nom de l'utilisateur connecté pour contextualiser la réponse.

    Exemples :
    1. Requête : "Je veux voir mes documents."
       Réponse : "arthur veut voir ses documents."

    2. Requête : "Est-ce que j'ai des messages non lus ?"
       Réponse : "arthur se demande s'il a des messages non lus."

    3. Requête : "Où est ma commande ?"
       Réponse : "arthur cherche sa commande."

    4. Requête : "ajoute moi une tache pour ramasser les poubelles pour aujourd'hui"
       Réponse : "Je vais ajouter une tache pour arthur pour ramasser les poubelles pour aujourd'hui."

    Si la requête ne contient aucune référence à la première personne, garde la requête telle qu'elle est.
    :return: Le nom de l'utilisateur connecté
    """
    return user_context.username
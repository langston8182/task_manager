from bson import ObjectId
from pydantic import BaseModel, Field
from datetime import datetime

from pydantic.dataclasses import dataclass


@dataclass
class Task:
    id: str = Field(description="identifiant de la tâche")
    content: str = Field(description="nom de la tâche")
    due_date: datetime = Field(description="date limite de la tâche")
    status: str = Field(description="statut de la tâche")
    responsable: str = Field(description="responsable de la tâche")

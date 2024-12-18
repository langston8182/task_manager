from dotenv import load_dotenv
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI

from env_manager import load_aws_env
from get_secrets import get_key_value
from tools.add_task import add_task
from tools.create_task_id import create_task_id
from tools.delete_task import delete_task
from tools.get_current_time import get_current_time
from tools.get_task import get_task
from tools.update_task import update_task
import user_context
from tools.who_am_i import who_am_i

load_dotenv()
load_aws_env()

def run_llm(query: str, username: str) -> str:
    user_context.username = username
    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini", api_key=get_key_value("OPENAI_API_KEY"))
    prompt = hub.pull("hwchase17/react")
    tools = [
        add_task,
        delete_task,
        get_task,
        get_current_time,
        update_task,
        create_task_id,
        who_am_i,
    ]
    agent = create_react_agent(prompt=prompt, llm=llm, tools=tools)
    executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    result = executor.invoke({"input": query})

    return result["output"]

if __name__ == "__main__":
    query = "Quelles sont toutes mes taches ?"
    #query = "Modifie la tache de virginie pour le velo et modifie le contenu par réparé le velo"
    #query = "Modifie la tache de cyril pour reparer le velo et assigne la a Virginie"
    #query = "Modifie la tache de reparer le velo et elle doit etre terminee pour ce lundi"
    #query = "supprime la tache ou je dois mesurer le plan du bas"
    #query = "je dois appeler mon pere aujourd'hui"
    result = run_llm(query, "Cyril")
    print(result)

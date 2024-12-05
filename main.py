import streamlit as st
from streamlit_chat import message
from core import run_llm
from datetime import datetime

# Configuration de la page
st.set_page_config(page_title="Chat LLM", page_icon="💬", layout="centered")

# Charger le CSS depuis le fichier externe
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialisation des messages
if "chat_data" not in st.session_state:
    st.session_state["chat_data"] = []  # Liste pour stocker les messages et leurs métadonnées

# Titre centré
st.markdown("<h1 style='text-align: center;'>💬 Assistant Virtuel</h1>", unsafe_allow_html=True)

# Formulaire pour la saisie et le bouton d'envoi
with st.form(key="chat_form", clear_on_submit=True):
    prompt = st.text_input("Entrez votre question :", key="prompt_input", placeholder="Posez votre question ici...")
    submit_button = st.form_submit_button("Envoyer")

# Gestion de la soumission
if submit_button and prompt:
    with st.spinner("L'assistant réfléchit..."):
        result = run_llm(query=prompt)  # Appel au backend
        formatted_response = result.replace("\n", "<br>")  # Remplacer les sauts
        current_time = datetime.now().strftime("%H:%M")  # Heure actuelle
        # Ajouter les messages à l'historique
        st.session_state["chat_data"].append({"role": "user", "message": prompt, "time": current_time})
        st.session_state["chat_data"].append({"role": "assistant", "message": formatted_response, "time": current_time})

# Affichage des messages existants
for chat in st.session_state["chat_data"]:
    role_class = "user-message" if chat["role"] == "user" else "ai-message"
    st.markdown(
        f"""
        <div class="message-container">
            <div class="{role_class}">{chat["message"]}</div>
            <div class="message-time">{chat["time"]}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

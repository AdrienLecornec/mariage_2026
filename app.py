import streamlit as st
from datetime import datetime
import time
import streamlit.components.v1 as components

# Configuration de la page
st.set_page_config(page_title="Notre Mariage Hakima", page_icon=":heart:", layout="centered")

# Code d’accès (via secrets Streamlit)
ACCESS_CODE = st.secrets["general"]["access_code"]

# Initialisation des états
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# -------- Authentification --------
if not st.session_state.authenticated:
    st.title("🔐 Accès au site privé")
    code_input = st.text_input("Entrez le code d’accès reçu par mail :", type="password")
    if code_input == ACCESS_CODE:
        st.session_state.authenticated = True
        st.rerun()
    elif code_input:
        st.error("Code incorrect. Veuillez réessayer.")
        st.stop()

# -------- Page principale --------
if st.session_state.authenticated:
 
    st.balloons()

    st.title("Hakima et Adrien")
    st.header("On se marie !")
    st.markdown("* 12 juillet 2026 - Paris 20 *")

    # -------- Compte à rebours --------
    wedding_date = datetime(2026, 7, 12)
    days_left = (wedding_date - datetime.now()).days
    st.metric(label="Jours restants avant le grand jour", value=f"{days_left} jours")

    # -------- Infos pratiques --------
    st.subheader("Infos pratiques")
    st.markdown("""
    **Lieu de la cérémonie :** Les Erables, Meudon  
    **Heure :** 15h00  
    **Dress code :** Chic et pastel  
    [Voir sur Google Maps](https://www.mariages.net/domaine-mariage/les-erables--e17577)
    """)

    # -------- Formulaire RSVP --------
    st.subheader("Confirmez votre présence")
    components.iframe("https://docs.google.com/forms/d/e/1FAIpQLScg66JhQYc7td2CyL8EP_j5eIjrCTJYJZo46Jlo7qYqNK7GPw/viewform?embedded=true"  height="600")

    # -------- Galerie --------
    st.subheader("Souvenirs & moments partagés")
    st.info("Galerie à venir...")

    # -------- Footer --------
    st.markdown("---")
    st.caption("Créé avec amour par les futurs mariés - 2026 💍")

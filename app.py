import streamlit as st
from datetime import datetime
import time

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
 
    time.sleep(2)
    with st.empty():
            st.balloons
            st.markdown("<div style='text-align:center;font-size:64px;'>💖</div>", unsafe_allow_html=True)
            st.markdown("<div style='text-align:center;font-size:20px;'>Chargement du site...</div>", unsafe_allow_html=True)
            time.sleep(2)

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
    with st.form("rsvp_form"):
        name = st.text_input("Votre nom")
        email = st.text_input("Adresse e-mail")
        coming = st.radio("Serez-vous présent ?", ["Oui", "Non"])
        guests = st.number_input("Combien d'accompagnants ?", 0, 5, step=1)
        message = st.text_area("Un petit mot pour nous ?")

        submitted = st.form_submit_button("Envoyer")
        if submitted:
            with open("fichier_reponse.csv", "a", encoding="utf-8") as f:
                f.write(f"{name},{email},{coming},{guests},{message}\n")
            st.success("Merci pour votre réponse ! 💌")

    # -------- Galerie --------
    st.subheader("Souvenirs & moments partagés")
    st.info("Galerie à venir...")

    # -------- Footer --------
    st.markdown("---")
    st.caption("Créé avec amour par les futurs mariés - 2026 💍")

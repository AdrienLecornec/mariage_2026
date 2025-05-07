# app.py
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Notre Mariage hakima", page_icon=":heart:", layout="centered")

# -------- Page d'accueil --------
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
**Lieu de la cérémonie :** Château Pape Clément, Paris  
**Heure :** 15h00  
**Dress code :** Chic et pastel  
[Voir sur Google Maps](https://goo.gl/maps/...)  
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
        st.success("bien répondu au formulaire !")

# -------- Galerie --------
st.subheader("Souvenirs & moments partagés")

# -------- Footer --------
st.markdown("---")
st.caption("Créé avec amour par les futurs mariés - 2026")

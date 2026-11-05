import streamlit as st

# Titel der Webseite
st.title("Zahlen-Auswahl Web App 🚀")

st.write("Klicke auf eine Option, um das Video zu öffnen:")

# Erstellt 4 Spalten nebeneinander für die Buttons
col1, col2, col3, col4 = st.columns(4)

with col1:
    # Ein echter Link, der wie ein Button aussieht und niemals blockiert wird
    st.link_button("Option 1 🕺", "https://youtube.com")
    st.caption("Rickroll")

with col2:
    st.link_button("Option 2 🗣️", "https://youtu.be")
    st.caption("SIX SEVEN!")

with col3:
    st.link_button("Option 3 😮", "https://youtu.be")
    st.caption("wass😮")

with col4:
    st.link_button("Option 4 🇩🇪", "https://youtu.be")
    st.caption("auf der heide")

import streamlit as st
import webbrowser

# Titel der Webseite
st.title("Zahlen-Auswahl Web App 🚀")

st.write("Wähle eine Option aus, um die Aktion zu starten:")

# Erstellt 4 Spalten nebeneinander für die Buttons und Links
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Option 1 🕺"):
        st.success("Du wurdest gerickrollt! 🕺")
        webbrowser.open("https://youtube.com")
    st.caption("[Rickroll](https://youtube.com)")

with col2:
    if st.button("Option 2 🗣️"):
        st.success("SIX SEVEN! 🗣️🔥")
        webbrowser.open("https://youtu.be")
    st.caption("[Six Seven](https://youtu.be)")

with col3:
    if st.button("Option 3 😮"):
        st.success("wass😮")
        webbrowser.open("https://youtu.be")
    st.caption("[Wass](https://youtu.be)")

with col4:
    if st.button("Option 4 🇩🇪"):
        st.success("auf der heide 🇩🇪")
        webbrowser.open("https://youtu.be")
    st.caption("[Auf der Heide](https://youtu.be)")

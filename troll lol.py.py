import streamlit as st

# Titel der Webseite
st.title("Wellcome to troll lol 🤡")

st.write("Wähle eine Option aus, um das Video direkt hier abzuspielen:")

# Initialisiere eine Variable im Hintergrund, um sich die Auswahl zu merken
if "auswahl" not in st.session_state:
    st.session_state.auswahl = None

# Erstellt 4 Buttons nebeneinander
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Option 1 🕺"):
        st.session_state.auswahl = "1"

with col2:
    if st.button("Option 2 🗣️"):
        st.session_state.auswahl = "2"

with col3:
    if st.button("Option 3 😮"):
        st.session_state.auswahl = "3"

with col4:
    if st.button("Option 4 🇩🇪"):
        st.session_state.auswahl = "4"

# Hier wird das Video direkt eingebettet, sobald ein Button geklickt wurde
if st.session_state.auswahl == "1":
    st.success("Du wurdest gerickrollt! 🕺")
    st.video("https://youtu.be/dQw4w9WgXcQ?si=z-os8sV2bCnkoSZ1", autoplay=True)

elif st.session_state.auswahl == "2":
    st.success("SIX SEVEN! 🗣️🔥")
    st.video("https://youtu.be/L7ejl_Hj3A8?si=gt_nVpqMPvhHHz8B", autoplay=True)

elif st.session_state.auswahl == "3":
    st.success("wass😮")
    st.video("https://youtu.be/5Vd3HP87IgU?si=fGuFxuT0FHBxBBI-", autoplay=True)

elif st.session_state.auswahl == "4":
    st.success("auf der heide 🇩🇪")
    st.video("https://youtu.be/Y9q9ycqFC3o?si=mg1iqu5rUz3nhEqI", autoplay=True)

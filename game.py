import streamlit as st
import random

st.set_page_config(
    page_title="AI Guess My Mind",
    page_icon="🧠",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #141e30, #243b55);
    color: white;
}
h1 {
    color: #00ffff;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.title("🧠 AI GUESS MY MIND")
st.subheader("🤖 Can I read your mind?")
st.write("Think of an animal. Let AI guess it!")

animals = {
    "Lion": ["wild", "land", "big"],
    "Tiger": ["wild", "land", "big"],
    "Elephant": ["wild", "land", "big"],
    "Dog": ["pet", "land", "small"],
    "Cat": ["pet", "land", "small"],
    "Rabbit": ["pet", "land", "small"],
    "Eagle": ["wild", "air", "big"],
    "Parrot": ["pet", "air", "small"],
    "Shark": ["wild", "water", "big"],
    "Fish": ["pet", "water", "small"]
}

if "result" not in st.session_state:
    st.session_state.result = None

st.markdown("---")

wild = st.radio(
    "1. Is your animal wild or domestic?",
    ["Wild", "Domestic"]
)

place = st.selectbox(
    "2. Where does it live?",
    ["Land", "Water", "Air"]
)

size = st.radio(
    "3. Is it big or small?",
    ["Big", "Small"]
)

if st.button("🔮 GUESS MY MIND"):

    possible = []

    for animal, features in animals.items():

        if (
            wild.lower() == features[0] or
            (wild == "Domestic" and features[0] == "pet")
        ) and place.lower() == features[1] and size.lower() == features[2]:

            possible.append(animal)

    if possible:
        st.session_state.result = random.choice(possible)
    else:
        st.session_state.result = "Unknown"

if st.session_state.result:

    st.markdown("---")

    st.subheader("🤖 AI Prediction:")

    if st.session_state.result != "Unknown":

        st.success(
            "I think your animal is " +
            st.session_state.result + "!"
        )

        st.balloons()

        correct = st.radio(
            "Did I guess correctly?",
            ["Yes", "No"],
            key="answer"
        )

        if st.button("Submit Answer"):
            if correct == "Yes":
                st.success("🎉 AI WON! You are amazing!")
            else:
                st.info("🏆 YOU WON! You defeated AI!")

    else:
        st.warning("I couldn't guess! You defeated AI!")

if st.button("🔄 PLAY AGAIN"):
    st.session_state.result = None
    st.rerun()

st.markdown("---")
st.caption("Created for College Expo | AI & DS Department")
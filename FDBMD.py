import streamlit as st
import random

activities = {
    "Food": ["Try a new café nearby", "Cook a recipe from another country", "Go for a food truck adventure"],
    "Outdoors": ["Visit a nearby park", "Go for a bike ride", "Take a photo walk around your city"],
    "Hobbies": ["Start a mini DIY project", "Try drawing something new", "Learn a new instrument for 30 mins"],
    "Social": ["Call a friend you haven't spoken to in a while", "Attend a local meetup", "Invite someone for a coffee"]
}

st.title("Fun Day Before Monday")
category = st.selectbox("Pick a category", list(activities.keys()))
if st.button("Generate Activity"):
    st.subheader("Your Activity:")
    st.write(random.choice(activities[category]))

st.markdown("---")
st.markdown("Made by **Ayaan D.** | [My Website](https://ayaandhalait.github.io)")



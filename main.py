import streamlit as st
import random

st.set_page_config(page_title="Snake Water Gun Game", page_icon="🎮")

st.title("🎮 Snake 🐍 Water 💧 Gun 🔫 Game")
st.write("Piay against the computer!")

choices=['Snake','Water','Gun']
player_choice=st.selectbox(f"Choose your option: ",choices)

if 'player_score' not in st.session_state:
    st.session_state.player_score = 0
if 'computer_score' not in st.session_state:
    st.session_state.computer_score = 0
if 'draw' not in st.session_state:
    st.session_state.draw = 0

if st.button("play"):
    computer_Choice=random.choice(choices)

    st.write(f"your Choose: {player_choice}")
    st.write(f"Computer Choose: {computer_Choice}")

    if player_choice==computer_Choice:
        result="Game is draw!🤝"
        st.session_state.draw +=1
    elif(player_choice=="Snake" and computer_Choice=="Water"):
        result="You Win!🎉"
        st.session_state.player_score += 1
    elif(player_choice=="Water" and computer_Choice=="Gun"):
        result="You Win!🎉"
        st.session_state.player_score += 1
    elif(player_choice=="Gun" and computer_Choice=="Snake"):
        result="You Win!🎉"
        st.session_state.player_score += 1
    else:
        result="Computer Win!🎉"
        st.session_state.computer_score += 1

    st.success(result)

    st.markdown("---")
    st.subheader("📊 Scoreboard")
    st.write(f"You: {st.session_state.player_score}")
    st.write(f"Computer: {st.session_state.computer_score}")
    st.write(f"Draw: {st.session_state.draw}")

if st.button("🔄 Reset Score"):
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.draw = 0
    st.info("Scores have been reset.")   
import streamlit as st
import random
import time
from navigation import make_sidebar

make_sidebar()
numbers = list(range(1, 9)) * 2#making a copy of 1st list 
random.shuffle(numbers)

# Create a dictionary to store the card status
cards = {i: {"number": n, "state": "closed"} for i, n in enumerate(numbers)}

# Function to draw the game board
def draw_board(cards):
    cols = st.columns(4)
    for i, card in cards.items():
        col = cols[i % 4]
        if card["state"] == "closed":
            btn = col.button("?", key=f"card-{i}-closed")
        elif card["state"] == "open":
            btn = col.button(str(card["number"]), key=f"card-{i}-open")
        else:  # card["state"] == "matched"
            btn = col.button(str(card["number"]), key=f"card-{i}-matched", disabled=True)

        if btn:
            handle_click(i, cards)

# Function to handle a card click
def handle_click(i, cards):
    # Open the card
    cards[i]["state"] = "open"

    # Get the indices of all open cards
    open_cards = [index for index, card in cards.items() if card["state"] == "open"]

    if len(open_cards) == 2:
        # If the two open cards match
        if cards[open_cards[0]]["number"] == cards[open_cards[1]]["number"]:
            # Mark them as matched
            cards[open_cards[0]]["state"] = "matched"
            cards[open_cards[1]]["state"] = "matched"
            
        else:
            # If they don't match, close them
            time.sleep(1)  # Wait for 1 second
            cards[open_cards[0]]["state"] = "closed"
            cards[open_cards[1]]["state"] = "closed"

    elif len(open_cards) == 3:
        # If there are three open cards, close the first two
        time.sleep(1)  # Wait for 1 second
        cards[open_cards[0]]["state"] = "closed"
        cards[open_cards[1]]["state"] = "closed"

    st.rerun()


def main():
    st.title("Memory Card Game")
    st.write("Please tilt your phone horizontally")
    if "cards" not in st.session_state:
        st.session_state.cards = cards

    draw_board(st.session_state.cards)

    if all(card["state"] == "matched" for card in st.session_state.cards.values()):
        st.success("Congratulations! You found all pairs.")
        st.balloons()

if __name__ == "__main__":
    main()

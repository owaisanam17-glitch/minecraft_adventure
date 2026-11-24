import streamlit as st
import random

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Minecraft Treasure Adventure",
    page_icon="💎",
    layout="centered"
)

# GAME TITLE
st.title("MINECRAFT TREASURE ADVENTURE")
st.subheader("Explore, Collect and Survive!")

st.write("Welcome, brave explorer! Choose a location and discover what is hiding there.")

# INITIALIZE PLAYER
if "player" not in st.session_state:
    st.session_state.player = {
        "health": 100,
        "coins": 50,
        "score": 0
    }

if "inventory" not in st.session_state:
    st.session_state.inventory = []

if "history" not in st.session_state:
    st.session_state.history = []

if "game_over" not in st.session_state:
    st.session_state.game_over = False

# GAME LOCATIONS
locations = {
    "Forest": ["Wood", "Apple", "Emerald"],
    "Cave": ["Diamond", "Gold", "Iron"],
    "Mountain": ["Ruby", "Gold", "Crystal"],
    "Beach": ["Pearl", "Shell", "Gold"]
}

# EXPLORE FUNCTION
def explore(location):

    if st.session_state.game_over:
        return

    event = random.choice(["treasure", "monster", "nothing"])

    if event == "treasure":

        treasure = random.choice(locations[location])

        coins_found = random.randint(10, 30)

        st.session_state.inventory.append(treasure)

        st.session_state.player["coins"] += coins_found

        st.session_state.player["score"] += 10

        message = (
            "You discovered " + treasure +
            " and collected " + str(coins_found) + " coins!"
        )

    elif event == "monster":

        damage = random.randint(10, 25)

        st.session_state.player["health"] -= damage

        if st.session_state.player["health"] < 0:
            st.session_state.player["health"] = 0

        message = (
            "A monster attacked you! You lost " +
            str(damage) + " health points!"
        )

    else:

        message = "Nothing found here. Keep exploring!"

    # SAVE ADVENTURE
    st.session_state.history.append({
        "location": location,
        "message": message
    })

    # CHECK PLAYER HEALTH
    if st.session_state.player["health"] <= 0:
        st.session_state.game_over = True


# RESET FUNCTION
def restart_game():

    st.session_state.player = {
        "health": 100,
        "coins": 50,
        "score": 0
    }

    st.session_state.inventory = []

    st.session_state.history = []

    st.session_state.game_over = False


# SCOREBOARD
st.divider()

st.subheader("YOUR PLAYER STATUS")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "❤️ HEALTH",
        st.session_state.player["health"]
    )

with col2:
    st.metric(
        "🪙 COINS",
        st.session_state.player["coins"]
    )

with col3:
    st.metric(
        "⭐ SCORE",
        st.session_state.player["score"]
    )

# HEALTH BAR
st.progress(
    st.session_state.player["health"] / 100,
    text="Player Health"
)

st.divider()

# GAME OVER
if st.session_state.game_over:

    st.error("GAME OVER! Your health has reached zero.")

    st.write("Your final score:", st.session_state.player["score"])

    st.write("You collected:", len(st.session_state.inventory), "treasures")

# EXPLORATION
else:

    st.subheader("WHERE WOULD YOU LIKE TO EXPLORE?")

    col1, col2 = st.columns(2)

    with col1:
        st.button(
            "🌳 FOREST",
            use_container_width=True,
            on_click=explore,
            args=("Forest",)
        )

        st.button(
            "⛰️ MOUNTAIN",
            use_container_width=True,
            on_click=explore,
            args=("Mountain",)
        )

    with col2:
        st.button(
            "💎 CAVE",
            use_container_width=True,
            on_click=explore,
            args=("Cave",)
        )

        st.button(
            "🏖️ BEACH",
            use_container_width=True,
            on_click=explore,
            args=("Beach",)
        )

# TREASURE INVENTORY
st.divider()

st.subheader("YOUR TREASURE INVENTORY")

if len(st.session_state.inventory) > 0:

    for treasure in st.session_state.inventory:
        st.write("💎", treasure)

else:

    st.write("Your inventory is empty. Go explore!")

# ADVENTURE HISTORY
st.divider()

st.subheader("ADVENTURE HISTORY")

if len(st.session_state.history) > 0:

    for number, adventure in enumerate(
        st.session_state.history, start=1
    ):

        st.write("ROUND", number)

        st.write("Location:", adventure["location"])

        st.info(adventure["message"])

        st.divider()

else:

    st.write("Your adventure has not started yet.")

# RESTART BUTTON
st.button(
    "🔄 START A NEW ADVENTURE",
    use_container_width=True,
    on_click=restart_game
)


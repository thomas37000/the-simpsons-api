import requests
import pathlib
import streamlit as st  # type: ignore
from typing import List, Dict
from classes.card import Card


# To apply the CSS file, I define a function that reads the CSS content and wraps it in a Streamlit HTML element.
# This function is called at the top of the script to ensure styles are applied early.


# function to load CSS from assets
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")


# load the external CSS
css_path = pathlib.Path("assets/style.css")
load_css(css_path)


def characters_page(page=1):
    """Récupère les personnages d'une page précise"""
    url = f"https://thesimpsonsapi.com/api/characters?page={page}"
    response = requests.get(url)
    data = response.json()
    return data["results"]  # liste des personnages (20 par page)


def character_by_id(id):
    char = requests.get(f"https://thesimpsonsapi.com/api/characters/{id}")
    res = char.json()
    name = res["name"]
    phrases = res["phrases"]
    image_url = "https://cdn.thesimpsonsapi.com/200"
    first = res["first_appearance_ep"]
    img_path = first["image_path"]
    avatar = f"{image_url}{img_path}"

    st.image({avatar})
    st.write(f"Hello {name}")

    for say in phrases:
        st.write(f"{name} : {say}")


def render_card(card: Card):
    st.markdown(
        f"""
        <div class="card">
            <img src="{card.avatar}">
            <h4 style="margin: 10px 0 0 0; color: #555;">{card.name}</h4>
            <p style="margin: 2px; color: #555;">{card.age or ""}</p>
            <p style="margin: 0; font-size: 14px; color: #888;">{card.occupation or ""}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def main():
    __metaclass__ = Card

    page_number = 1  # ou st.number_input pour choisir la page
    chars = characters_page(page_number)

    st.title("The Simpsons API")
    st.write("Python & Streamlit")

    image_url = "https://cdn.thesimpsonsapi.com/200"
    cols = st.columns(4)

    for index, c in enumerate(chars):
        img_path = c["portrait_path"] or ""
        avatar = f"{image_url}{img_path}"

        with cols[index % 4]:
            card = Card(
                name=c["name"],
                age=f"{c["age"]} ans" if c["age"] else "",
                avatar=f"{avatar}",
                occupation=c["occupation"] if c["occupation"] != "Unknown" else "",
            )

            render_card(card)

    # Homer = character_by_id(1)
    # st.write(Homer)


if __name__ == "__main__":
    main()

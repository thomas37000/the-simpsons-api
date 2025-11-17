import requests
import streamlit as st  # type: ignore
from typing import List, Dict


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


def main():
    page_number = 1  # ou st.number_input pour choisir la page
    chars = characters_page(page_number)

    st.write(f"Personnages de la page {page_number} (total {len(chars)})")

    for c in chars:
        image_url = "https://cdn.thesimpsonsapi.com/200"
        img_path = c["portrait_path"]
        avatar = f"{image_url}{img_path}"


        st.image({avatar})
        st.write(c["name"])
        age = c.get("age")  # utilise get pour éviter KeyError
        if age is None:
            st.write(" ")
        else:
            st.write(f"{age} ans")
        
        occupation = c.get("occupation")
        if occupation == "Unknown":
            st.write(" ")
        else:
            st.write(occupation)

    # Homer = character_by_id(1)
    # st.write(Homer)


if __name__ == "__main__":
    main()

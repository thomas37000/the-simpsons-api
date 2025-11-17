import requests
import streamlit as st


def main():

    response = requests.get("https://thesimpsonsapi.com/api/characters/1")
    res = response.json()
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


if __name__ == "__main__":
    main()

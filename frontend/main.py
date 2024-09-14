import requests
import streamlit as st

from config import host


def login():
    st.title("_:rainbow[Hi there.]_")

    name = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Log in"):
        response = requests.get(f"{host}/user/name/{name}")
        data = response.json()
        # TODO: create pydantic instance?
        if name == data["name"] and password == data["password"]:
            st.success("Success")
        else:
            st.error("Wrong name or password")


if __name__ == "__main__":
    login()

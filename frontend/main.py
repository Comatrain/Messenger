from enum import Enum

import requests
import streamlit as st

from config import host
from frontend.utils import st_horizontal
from schemas import UserSchema


class LoginStates(Enum):
    SUCCESS_LOGIN = 1
    FAILED_LOGIN = 2
    REGISTER_NEW_USER = 3


def login() -> LoginStates:
    columns = st.columns(3)

    with columns[1]:
        st.title("Hello")

        name = st.text_input("Username")
        password = st.text_input("Password", type="password")

        with st_horizontal():
            if st.button("Log in"):
                response = requests.get(f"{host}/user/login/{name}")
                data = UserSchema.model_validate(response.json())
                if name == data.login and password == data.password:
                    st.success("Success")
                    return LoginStates.SUCCESS_LOGIN
                else:
                    st.error("Wrong name or password")
                    return LoginStates.FAILED_LOGIN
            if st.button("New user?"):
                return LoginStates.REGISTER_NEW_USER


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    login = login()

    if login == LoginStates.SUCCESS_LOGIN:
        st.switch_page("pages/lk.py")
    elif login == LoginStates.REGISTER_NEW_USER:
        st.switch_page("pages/register.py")

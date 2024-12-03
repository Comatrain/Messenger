from contextlib import contextmanager
from enum import Enum

import requests
import streamlit as st

from config import host
from schemas import UserSchema

HORIZONTAL_STYLE = """
<style class="hide-element">
    /* Hides the style container and removes the extra spacing */
    .element-container:has(.hide-element) {
        display: none;
    }
    /*
        The selector for >.element-container is necessary to avoid selecting the whole
        body of the streamlit app, which is also a stVerticalBlock.
    */
    div[data-testid="stVerticalBlock"]:has(> .element-container .horizontal-marker) {
        display: flex;
        flex-direction: row !important;
        flex-wrap: wrap;
        gap: 0.5rem;
        align-items: baseline;
    }
    /* Buttons and their parent container all have a width of 704px, which we need to override */
    div[data-testid="stVerticalBlock"]:has(> .element-container .horizontal-marker) div {
        width: max-content !important;
    }
    /* Just an example of how you would style buttons, if desired */
    /*
    div[data-testid="stVerticalBlock"]:has(> .element-container .horizontal-marker) button {
        border-color: red;
    }
    */
</style>
"""


@contextmanager
def st_horizontal():
    st.markdown(HORIZONTAL_STYLE, unsafe_allow_html=True)
    with st.container():
        st.markdown(
            '<span class="hide-element horizontal-marker"></span>',
            unsafe_allow_html=True,
        )
        yield


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

import streamlit as st


def register():
    columns = st.columns(3)

    with columns[1]:
        st.title("Hello")

        name = st.text_input("Username")
        password = st.text_input("Password", type="password")
        re_password = st.text_input("Re-enter password", type="password")

        if st.button("Register me"):
            pass
        #     response = requests.get(f"{host}/user/login/{name}")
        #     data = UserSchema.model_validate(response.json())
        #     if name == data.login and password == data.password:
        #         st.success("Success")
        #         return LoginStates.SUCCESS_LOGIN
        #     else:
        #         st.error("Wrong name or password")
        #         return LoginStates.FAILED_LOGIN
        # if st.button("New user?"):
        #     return LoginStates.REGISTER_NEW_USER


register()

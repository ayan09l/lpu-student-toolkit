import streamlit as st
import streamlit_authenticator as stauth

# User credentials
names = ['Ayan']
usernames = ['ayan09']
passwords = ['12345']

hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(
    names,
    usernames,
    hashed_passwords,
    'grocery_app',
    'abcdef',

)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    st.success(f"Welcome {name} 👋")
elif authentication_status is False:
    st.error("Incorrect username or password")
elif authentication_status is None:
    st.warning("Please enter your login details")
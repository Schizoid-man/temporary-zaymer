import streamlit as st
import pandas as pd
import hashlib
from time import sleep
from navigation import make_sidebar
# DB Management
import sqlite3 

st.set_page_config(page_title="Zaymer-companion")
st.title("Zaymer-Companion")
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Function to create user table if not exists
def create_user_table():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

# Function to add new user
def add_userdata(username, password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
    conn.commit()

# Function to retrieve user details
def login_user(username, password):
    c.execute('SELECT * FROM userstable WHERE username = ? AND password = ?', (username, password))
    data = c.fetchall()
    return data

# Function to hash password
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# Main function
def main():
    st.subheader("Please sign-in or register to continue:")

    menu = ["Login", "Register"]
    choice = st.selectbox("Menu", menu)

    if choice == "Login":
        st.subheader("Login Section")

        username = st.text_input("User Name")
        password = st.text_input("Password", type='password')
        if st.checkbox("Login"):
            hashed_password = make_hashes(password)
            result = login_user(username, hashed_password)
            if result:
                st.session_state.logged_in = True
                st.success("Logged In as {}".format(username))
                sleep(0.5)
                st.switch_page("pages/game.py")
            else:
                st.warning("Incorrect Username/Password")

    elif choice == "Register":
        st.subheader("Create New Account")
        new_username = st.text_input("User Name")
        new_password = st.text_input("Password", type='password')

        if st.button("Signup"):
            hashed_new_password = make_hashes(new_password)
            add_userdata(new_username, hashed_new_password)
            st.success("You have successfully created a valid account")
            st.info("Go to Login Menu to login")

if __name__ == '__main__':
    create_user_table()
    main()

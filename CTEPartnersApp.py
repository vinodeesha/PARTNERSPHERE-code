import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
import pandas as pd
import hashlib
import sqlite3
import app
import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create Users table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS Users (
             id INTEGER PRIMARY KEY,
             Username TEXT UNIQUE,
             Password TEXT
             )''')

def create_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    try:
        c.execute("INSERT INTO Users (Username, Password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def verify_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    c.execute("SELECT * FROM Users WHERE Username=? AND Password=?", (username, hashed_password))
    return c.fetchone() is not None

# Function to check if user is logged in
def is_logged_in():
    return 'logged_in' in st.session_state and st.session_state.logged_in

# Function to set login flag
def set_logged_in(value):
    st.session_state.logged_in = value

# Streamlit app starts here
st.title('Login / Sign Up')

# Radio button to switch between login and sign-up forms
form_choice = st.sidebar.radio("Choose an action", ("Login", "Sign Up"))

if form_choice == "Login":
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if verify_user(username, password):
            st.success("Successfully logged in!")
            set_logged_in(True)   
            st.empty()
        else:
            st.error("Invalid username or password. Try signing up")

elif form_choice == "Sign Up":
    st.subheader("Sign Up")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    if st.button("Sign Up"):
        if new_password == confirm_password:
            if create_user(new_username, new_password):
                st.success("User created successfully. Please login.")
            else:
                st.error("Username already exists.")
        else:
            st.error("Passwords do not match.")

# Only display the main app content if the user is logged in
if is_logged_in():
    st.empty()
    engine = create_engine('sqlite:///example.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    st.title(' Career and Technical Education Department Partners')

    tabs = ["View Partners", "Add Partner", "Edit Partner", "Delete Partner"]
    choice = st.sidebar.selectbox("Menu", tabs)

    if choice == "View Partners":
        # Fetch all suppliers
        results = session.execute(text("SELECT * FROM Partners"))
        df = pd.DataFrame(results, columns=['ID','PartnerName', 'PartnerType', 'ContactPerson', 'ContactEmail', 'ContactPhone', 'Address', 'Website'])

        # Filter suppliers
        filter = st.text_input('Enter search term')
        if filter:
            df = df[df['PartnerName'].str.contains(filter) | df['PartnerType'].str.contains(filter) | df['ContactPerson'].str.contains(filter)| df['ContactEmail'].str.contains(filter)| df['ContactPhone'].str.contains(filter)| df['Address'].str.contains(filter)| df['Website'].str.contains(filter)]

        st.dataframe(df, height=600, width=4100)
        #st.table(df)
        #st.write(df, height=600, width=4100)

    elif choice == "Add Partner":
        #id = st.number_input('Enter ID', value=1)
        result = session.execute(text("SELECT MAX(ID) FROM Partners")).fetchone()
        id = result[0] + 1 if result[0] else 1
        name = st.text_input('Enter Name')
        type = st.text_input('Enter Type')
        person = st.text_input('Enter Contact Person')
        email = st.text_input('Enter Email')
        phone = st.text_input('Enter Phone')
        address = st.text_input('Enter Address')
        website = st.text_input('Enter Website')

        if st.button('Add Partner'):
            session.execute(text("INSERT INTO Partners (ID, PartnerName, PartnerType, ContactPerson, ContactEmail, ContactPhone, Address, Website) VALUES (:id, :name, :type, :person, :email, :phone, :address, :website)"), {'id': id, 'name': name, 'type': type, 'person': person, 'email': email, 'phone': phone, 'address': address, 'website':website})
            session.commit()
            if st.button('OK'):
                st.success("Partner added successfully.")
                st.experimental_rerun()

    elif choice == "Edit Partner":
        results = session.execute(text("SELECT ID FROM Partners"))
        ids = [result[0] for result in results]
        id = st.selectbox('Select ID of Partner to edit', ids)
        if id:
            result = session.execute(text("SELECT * FROM Partners WHERE ID = :id"), {'id': id}).fetchone()
            if result:
                name = st.text_input('Enter Name', value=result[1])
                type = st.text_input('Enter Type', value=result[2])
                person = st.text_input('Enter Contact Person', value=result[3])
                email = st.text_input('Enter Email', value=result[4])
                phone = st.text_input('Enter Phone', value=result[5])
                address = st.text_input('Enter Address', value=result[6])
                website = st.text_input('Enter Website', value=result[7])
                if st.button('Update Partner'):
                    session.execute(text("UPDATE Partners SET PartnerName = :name, PartnerType = :type, ContactPerson = :person, ContactEmail = :email, ContactPhone = :phone, Address = :address, Website = :website WHERE ID = :id"), {'id': id, 'name': name, 'type': type, 'person': person, 'email': email, 'phone': phone, 'address': address, 'website': website})
                    session.commit()
                    if st.button('OK'):
                        st.success("Partner updated successfully.")
                        st.experimental_rerun()
            else:
                st.write("No Partner found with the given ID.")

    elif choice == "Delete Partner":
        results = session.execute(text("SELECT ID FROM Partners"))
        ids = [result[0] for result in results]
        id = st.selectbox('Select ID of Partner to delete', ids)
        if id:
            result = session.execute(text("SELECT * FROM Partners WHERE ID = :id"), {'id': id}).fetchone()
            if result:
                st.write(f"ID: {result[0]}, PartnerName: {result[1]}, PartnerType: {result[2]}, ContactPerson: {result[3]}, ContactEmail: {result[4]}")
                if st.button('Delete Partner'):
                    session.execute(text("DELETE FROM Partners WHERE ID = :id"), {'id': id})
                    session.commit()
                    st.success("Partner deleted successfully.")
                    choice = "View Partners"
                    st.experimental_rerun()

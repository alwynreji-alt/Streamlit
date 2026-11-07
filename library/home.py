# Transform the given Python MySQL Book CRUD console application into a
# GUI-based web application using the Streamlit package.
# The application should connect to the library_db
# MySQL database and provide a multi-page Streamlit interface.
# Create separate pages for each of the following operations:
# 1. Create Page – Implement the create() function to add a new book.
# 2. List Page – Implement the list() function to display all books.
# 3. Retrieve Page – Implement the retrieve() function to search and display a specific book using its ID.
# 4. Update Page – Implement the update() function to modify the details of an existing book.
# 5. Delete Page – Implement the delete() function to remove a book using its ID.


import streamlit as st

st.title("WELCOME TO MY LIBRARY")
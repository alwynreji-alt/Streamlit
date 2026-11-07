# 3. Retrieve Page – Implement the retrieve() function to search and display a specific book using its ID.
import streamlit as st
from librarydb import BookListCreateRetrieveUpdateDelete

st.title("RETRIEVE BOOK")

book_id = st.number_input(
    "Enter Book ID:",
    min_value=1,
    step=1
)

btn = st.button("SEARCH BOOK")

if btn:

    book_instance = BookListCreateRetrieveUpdateRetrieve()

    result = book_instance.retrieve(book_id)

    book_instance.close()

    if result:

        row = result[0]

        st.success("Book found!")

        st.write("Book ID:", row[0])
        st.write("Title:", row[1])
        st.write("Author:", row[2])
        st.write("Price:", row[3])
        st.write("Pages:", row[4])
        st.write("Language:", row[5])

    else:

        st.error("No book found with this ID.")
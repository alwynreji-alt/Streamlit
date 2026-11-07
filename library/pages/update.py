# 4. Update Page – Implement the update() function to modify the details of an existing book.
import streamlit as st
from librarydb import BookListCreateRetrieveUpdateDelete

st.title("UPDATE BOOK")

book_id = st.number_input(
    "Enter Book ID:",
    min_value=1,
    step=1
)

title = st.text_input("Enter updated book title:")

author = st.text_input("Enter updated author:")

price = st.number_input(
    "Enter updated price:",
    min_value=100,
    step=1
)

pages = st.number_input(
    "Enter updated number of pages:",
    min_value=1,
    step=1
)

language = st.selectbox(
    "Select language:",
    ["English", "Malayalam", "Hindi", "Tamil"]
)

btn = st.button("UPDATE BOOK")

if btn:

    book_instance = BookListCreateRetrieveUpdateDelete()
    result = book_instance.update(
        book_id,
        title,
        author,
        price,
        pages,
        language
    )

    book_instance.close()

    if result > 0:
        st.success("Book updated successfully!")
    else:
        st.error("No book found with this ID.")
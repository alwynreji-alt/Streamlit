# 5. Delete Page – Implement the delete() function to remove a book using its ID.
import streamlit as st
from librarydb import BookListCreateRetrieveUpdateDelete

st.title("DELETE BOOK")

book_id = st.number_input(
    "Enter Book ID:",
    min_value=1,
    step=1
)

btn = st.button("DELETE BOOK")

if btn:

    book_instance = BookListCreateRetrieveUpdateDelete()

    result = book_instance.delete(book_id)

    if result > 0:

        st.success("Book deleted successfully!")

    else:

        st.error("No book found with this ID.")

# 1. Create Page – Implement the create() function to add a new book.

#CREATE PAGE

import streamlit as st
from librarydb import BookListCreateRetrieveUpdateDelete
st.title("CREATE RECORD PAGE")



Title = st.text_input("Enter the name of the book:")
Author = st.text_input("Enter the name of the author:")
Price = st.number_input("Enter the price of the book:",min_value=100)
Pages = st.text_input("Enter the number of pages in the book:",)
Language = st.selectbox("language",["English","Malayalam","Hindi","tamil"])
btn=st.button("ADD BOOK")

if btn:
   book_instance = BookListCreateRetrieveUpdateDelete()
   book_instance.create(Title,Author,Price,Pages,Language)
   st.success("Book added successfully!")



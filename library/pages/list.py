import streamlit as st
from librarydb import BookListCreateRetrieveUpdateDelete

st.title("LIST OF BOOKS")

book_instance = BookListCreateRetrieveUpdateDelete()

result = book_instance.list()

book_instance.close()

if result:

    for row in result:

        st.write("Book ID:", row[0])
        st.write("Title:", row[1])
        st.write("Author:", row[2])
        st.write("Price:", row[3])
        st.write("Pages:", row[4])
        st.write("Language:", row[5])

        st.divider()

else:

    st.info("No books found.")
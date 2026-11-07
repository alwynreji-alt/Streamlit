import mysql.connector


class BookListCreateRetrieveUpdateDelete:

    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="library_db"
        )

        self.c = self.con.cursor()

    # LIST ALL BOOKS
    def list(self):

        query = "SELECT * FROM book"
        self.c.execute(query)
        result = self.c.fetchall()
        return result

    # CREATE BOOK
    def create(self, title, author, price, pages, language):

        query = """
        INSERT INTO book(title, author, price, pages, language)
        VALUES (%s, %s, %s, %s, %s)
        """

        data = (title, author, price, pages, language)
        self.c.execute(query, data)
        self.con.commit()

    # RETRIEVE ONE BOOK
    def retrieve(self, id):
        query = "SELECT * FROM book WHERE id=%s"
        data = (id,)
        self.c.execute(query, data)
        result = self.c.fetchall()
        return result

    # UPDATE BOOK
    def update(self, id, title, author, price, pages, language):

        query = """
        UPDATE book
        SET title=%s,
            author=%s,
            price=%s,
            pages=%s,
            language=%s
        WHERE id=%s
        """
        data = (
            title,
            author,
            price,
            pages,
            language,
            id
        )
        self.c.execute(query, data)
        self.con.commit()
        return self.c.rowcount

    # DELETE BOOK
    def delete(self, id):

        query = "DELETE FROM book WHERE id=%s"
        data = (id,)
        self.c.execute(query, data)
        self.con.commit()
        return self.c.rowcount

    # CLOSE DATABASE
    def close(self):

        self.c.close()
        self.con.close()
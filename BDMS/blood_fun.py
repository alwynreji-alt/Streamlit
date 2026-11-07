
# create = post
# retrive = get(id)
# view,read= get
# delete= delete
# partial update=
# full update= put


import mysql.connector

class BookListCreateRetrieveUpdateDelete:

    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="blooddb"
        )

        self.c = self.con.cursor()

# CREATE/POST

    def post(self  ,name,blood_group,phone_no,city,last_donation):
        query = """
         insert into donor(name,blood_group,phone_no,city,last_donation)
         values (%s , %s , %s , %s , %s)
        """

        data = (name,blood_group,phone_no,city,last_donation)
        self.c.execute(query,data)
        self.con.commit()

    # VIEW OR LIST OR READ /GET

    def get(self):
        query = "select* from donor"
        self.c.execute(query)
        result = self.c.fetchall()
        return result

    # RETRIEVE/GET(ID)

    def get_id(self,id):
        query="select * from donor where id=%s"
        data=(id, )
        self.c.execute(query,data)
        result = self.c.fetchall()
        return result

    # DELETE/DELETE

    def delete(self,id):
        query = "DELETE FROM donor WHERE id=%s"
        data = (id,)
        self.c.execute(query, data)
        self.con.commit()
        return self.c.rowcount

    # UPDATE/PUT

    def put(self,id,name,blood_group,phone_no,city,last_donation):
        query="""
        update donor set name=%s,blood_group=%s,phone_no=%s,city=%s,last_donation=%s where id=%s
        """

        data = (id,name,blood_group,phone_no,city,last_donation)
        self.c.execute(query,data)
        self.con.commit()
        return self.c.rowcount




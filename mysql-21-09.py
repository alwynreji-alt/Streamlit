import mysql.connector

con = mysql.connector.connect(
    user="root",
    password="root",
    host="localhost"
)

c = con.cursor()

c.execute("CREATE DATABASE IF NOT EXISTS vehicle_db")

c.execute("USE vehicle_db")

c.execute("""
CREATE TABLE IF NOT EXISTS vehicle(
    id INT NOT NULL PRIMARY KEY,
    brand VARCHAR(30),
    model VARCHAR(30),
    type VARCHAR(30),
    price INT,
    year INT
)
""")


import mysql.connector


con = mysql.connector.connect(
    user="root",
    password="root",
    host="localhost",
    database="vehicle_db"
)

c = con.cursor()


class vehiclecrud:

    def List(self):
        query = "SELECT * FROM vehicle"

        c.execute(query)

        records = c.fetchall()

        if records:
            for row in records:
                print(row)
        else:
            print("No vehicle records found")

    def Create(self):
        id = int(input("Enter vehicle id: "))
        brand = input("Enter brand: ")
        model = input("Enter model: ")
        type = input("Enter type: ")
        price = int(input("Enter price: "))
        year = int(input("Enter year: "))

        query = """
        INSERT INTO vehicle
        (id, brand, model, type, price, year)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        data = (id, brand, model, type, price, year)

        c.execute(query, data)
        con.commit()

        print("Vehicle inserted successfully")


    def Retrieve(self):
        id = int(input("Enter vehicle id: "))

        query = "SELECT * FROM vehicle WHERE id = %s"

        data = (id,)

        c.execute(query, data)

        record = c.fetchone()

        if record:
            print(record)
        else:
            print("Vehicle not found")


    def Update(self):
        id = int(input("Enter vehicle id: "))
        price = int(input("Enter new price: "))

        query = "UPDATE vehicle SET price = %s WHERE id = %s"

        data = (price, id)

        c.execute(query, data)
        con.commit()

        if c.rowcount > 0:
            print("Vehicle updated successfully")
        else:
            print("Vehicle not found")


    def Delete(self):
        id = int(input("Enter vehicle id: "))

        query = "DELETE FROM vehicle WHERE id = %s"

        data = (id,)

        c.execute(query, data)
        con.commit()

        if c.rowcount > 0:
            print("Vehicle deleted successfully")
        else:
            print("Vehicle not found")


obj = vehiclecrud()

while True:

    print("\n---------- VEHICLE CHOICES ----------")
    print("1. List all vehicles")
    print("2. Create vehicle")
    print("3. Retrieve vehicle")
    print("4. Update vehicle")
    print("5. Delete vehicle")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        obj.List()

    elif choice == 2:
        obj.Create()

    elif choice == 3:
        obj.Retrieve()

    elif choice == 4:
        obj.Update()

    elif choice == 5:
        obj.Delete()

    elif choice == 6:
        print("Program exited")
        break

    else:
        print("Invalid choice")
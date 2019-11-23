import mysql.connector


class Database:
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="admin",
                passwd="admin"
            )
            self.mycursor = self.mydb.cursor()
            self.mycursor.execute("CREATE DATABASE indoorview")
        except Exception as e:
            print(e)

    def create_table(self, table_name):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="admin",
                passwd="admin",
                database="indoorview"
            )
            self.mycursor = self.mydb.cursor()
            self.mycursor.execute("CREATE TABLE " + table_name +
                                  " (id INT AUTO_INCREMENT PRIMARY KEY, coordinates VARCHAR(255), image_path VARCHAR(255))")
        except Exception as e:
            print(e)

    def add_map(self, name, imagepath):
        try:
            self.mycursor.execute(
                "INSERT INTO maps (name, imagepath) VALUES (%s, %s)", (name, imagepath)
            )
            self.mydb.commit()
        except Exception as e:
            print(e)

    def add_coordinate(self, table_name, coordinates, image_path):
        try:
            self.mycursor.execute(
                "INSERT INTO " + table_name + " (coordinates, image_path) VALUES (%s, %s)", (coordinates, image_path))
            self.mydb.commit()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    database = Database()
    database.create_table("maps")
    database.add("mytable1", "1.243534,58670956", "/image/jsfska.jpg")

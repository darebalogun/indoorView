import mysql.connector


class Database:
    """
    Represents a database with methods to perform database operations
    """

    def __init__(self):
        self.name = "sql9317665"
        self.host = "sql9.freemysqlhosting.net"
        self.username = "sql9317665"
        self.password = "Rlkt5e4s9E"

        try:
            self.mydb = mysql.connector.connect(
                host=self.host,
                user=self.username,
                passwd=self.password
            )
            self.mycursor = self.mydb.cursor()
            self.mycursor.execute("CREATE DATABASE IF NOT EXISTS indoorview")
        except Exception as e:
            print(e)

    def create_table(self, table_name):
        """
        Create a database table for this map, overwrite any existing tables with the same name

        Parameters
        ----------
        table_name : str
            the same as the name of the map
        """
        try:
            self.mydb = mysql.connector.connect(
                host=self.host,
                user=self.username,
                passwd=self.password,
                database=self.name
            )
            self.mycursor = self.mydb.cursor()
            self.mycursor.execute("DROP TABLE IF EXISTS " + table_name)
            self.mycursor.execute("CREATE TABLE " + table_name +
                                  " (id INT AUTO_INCREMENT PRIMARY KEY, coordx FLOAT(24), coordy FLOAT(24), image_path VARCHAR(255), mappedx FLOAT(24), mappedy FLOAT(24))")
            print("Table created successfully!")
        except Exception as e:
            print(e)

    def add_map(self, name, imagepath):
        """
        Add our new database to the maps table

        Parameters
        ----------
        name : str
            map name
        imagepath : str
            image path to the maps png 
        """
        try:
            self.mycursor.execute(
                "INSERT INTO maps (name, imagepath) VALUES (%s, %s)", (name, imagepath)
            )
            self.mydb.commit()
        except Exception as e:
            print(e)

    def add_coordinate(self, table_name, coordx, coordy, image_path, mappedx, mappedy):
        """
        Add a set of coordinates and corresponding image

        Parameters
        ----------
        table_name : str
            map name
        coordx, coordy : float
            x y coordinates based on the ros map (origin in centre)
        image_path : str
            path to 360 image captured at those coordinates
        mappedx, mappedy : float
            x y corresponding coordinated with origin at top left
        """
        try:
            self.mycursor.execute(
                "INSERT INTO " + table_name +
                " (coordx, coordy, image_path, mappedx, mappedy) VALUES (%s, %s, %s, %s, %s)", (
                    coordx, coordy, image_path, mappedx, mappedy))
            self.mydb.commit()
        except Exception as e:
            print(e)

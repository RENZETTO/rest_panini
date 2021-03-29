import csv
import mysql.connector

tabella = """
CREATE TABLE IF NOT EXISTS ordinazioni (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `data` DATE NOT NULL,
    classe CHAR NOT NULL,
    sede VARCHAR(16) NOT NULL,
    prodotto VARCHAR(64) NOT NULL,
    numeroOrdinazione MEDIUMINT NOT NULL
)
"""

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="educazione_alimentare"
)

mycursor = mydb.cursor()
mycursor.autocommit = True

mycursor.execute(tabella)

if __name__ == "__main__":

    with open("export_gennaio.csv", "r") as f:
        values = []

        query = "INSERT INTO ordinazioni (data, classe, sede, prodotto, numeroOrdinazione) VALUES (%s, %s, %s, %s, %s)"

        reader = csv.reader(f, delimiter=";")
        
        j = 0
        for i, line in enumerate(reader):
            values.append((line[0], line[1], line[2], line[3], int(line[4])))
            j = j + 1
            
        mycursor.executemany(query, values)
        
        print(mycursor.rowcount, "was inserted.")
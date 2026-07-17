import sqlite3

conn = sqlite3.connect('geeks.db')
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS STUDENT;

CREATE TABLE STUDENT(
    NAME VARCHAR(255),
    CLASS VARCHAR(255),
    SECTION VARCHAR(255)
);

INSERT INTO STUDENT VALUES ('Raju', '7th', 'A');
INSERT INTO STUDENT VALUES ('Shyam', '8th', 'B');
INSERT INTO STUDENT VALUES ('Baburao', '9th', 'C');
""")

conn.commit()

print("Data Inserted in the table:")
cursor.execute("SELECT * FROM STUDENT")
for row in cursor.fetchall():
    print(row)
cursor.execute('''UPDATE STUDENT SET CLASS = '10th' WHERE NAME = 'Raju';''')
print('\nAfter Updating...\n')

print("STUDENT Table: ")
data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)


 
query = "SELECT * FROM STUDENT where NAME = 'Raju'"
print("Raju Details: ")
cursor.execute(query)
for row in cursor.fetchall():
    print(row)
conn.close()
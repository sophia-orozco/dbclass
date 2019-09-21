import mysql.connector
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(
  host="localhost",
  user="sophia",
  passwd="genomaliigh",
  database = "TraitsQLTs_Genetica")

mycursor = mydb.cursor()

mycursor.execute("select medida from Mediciones where tipo='altura'")
rows= mycursor.fetchall()
altura=list(rows)
[i[0] for i in altura]

mycursor.execute("select medida from Mediciones where tipo='frente'")
rows= mycursor.fetchall()
frente=list(rows)
[i[0] for i in frente]

mycursor.execute("select medida from Mediciones where tipo='brazo'")
rows= mycursor.fetchall()
brazo=list(rows)
[i[0] for i in brazo]

mycursor.execute("select medida from Mediciones where tipo='calzado'")
rows= mycursor.fetchall()
calzado=list(rows)
[i[0] for i in calzado]

mycursor.execute("select medida from Mediciones where tipo='sistolica'")
rows= mycursor.fetchall()
sistolica=list(rows)
[i[0] for i in sistolica]

mycursor.execute("select medida from Mediciones where tipo='diastolica'")
rows= mycursor.fetchall()
diastolica=list(rows)
[i[0] for i in diastolica]

mycursor.execute("select medida, persona_id from Mediciones where tipo='frente' or tipo='brazo'")
rows= mycursor.fetchall()
pigmentacion=list(rows)
[i[0] for i in pigmentacion]

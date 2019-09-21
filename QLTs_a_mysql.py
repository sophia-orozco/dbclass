import mysql.connector
import pandas as pd
dataQLTs= pd.read_csv('Datos_QLTs.csv')
datosG=dataQLTs.iloc[2:34,0:4] #nombres, sexo, edad, estado, sin titulos

mydb = mysql.connector.connect(
  host="localhost",
  user="sophia",
  passwd="genomaliigh",
  database = "TraitsQLTs_Genetica")

mycursor = mydb.cursor()

#crear tabla DatosGenerales
sqlDatosGenerales = "CREATE TABLE DatosGenerales ( \
  persona_id INT AUTO_INCREMENT PRIMARY KEY, \
  nombre VARCHAR(255), \
  sexo CHAR(1),\
  edad INT(2), \
  estado  VARCHAR(10)\
  )"

mycursor.execute(sqlDatosGenerales)

#Llena tabla DatosGenerales
for row in datosG.iterrows():
    sql = "INSERT INTO DatosGenerales (nombre, sexo, edad, estado) VALUES (%s, %s, %s, %s)"
    val = list(row[1]) #no sabe leer una serie de pandas, tiene que estar en lista
    #print(val) #print(type(val))
    mycursor.execute(sql, val)

mydb.commit()

#Crear tabla de Mediciones
sqlMediciones = "CREATE TABLE Mediciones ( \
  medicion_id INT AUTO_INCREMENT PRIMARY KEY, \
  tipo VARCHAR(16), \
  medida FLOAT, \
  persona_id INT, \
  CONSTRAINT persona_fk \
  FOREIGN KEY (persona_id) \
     REFERENCES DatosGenerales(persona_id) \
  )"

mycursor.execute(sqlMediciones)

#datosMeciociones contiene: altura, f1, f2, f3, f4, f5, p, b1, b2, b3, b4, b5, p, calzado, sistolica, diastolica
datosMediciones=dataQLTs.iloc[2:34,4:20]

#llenar datos de altura, considerando que es el unico dato de Mediciones que tiene la persona 1
#llenar el resto de mediciones, considerando que no llenamos para la primer persona por falta de datos
val=[]
altura= datosMediciones.iloc[:,0]
frente = datosMediciones.iloc[1:,1:6]
brazo = datosMediciones.iloc[1:,7:12]
calzado = datosMediciones.iloc[1:,13]
sistolica = datosMediciones.iloc[1:,14]
diastolica = datosMediciones.iloc[1:,15]
for i in range (len(frente)):
    val.append(["altura",altura.iloc[i],i+1])
    for j in range (len(frente.iloc[0,:])):
        val.append(["frente",frente.iloc[i][j],i+2])
        val.append(["brazo",brazo.iloc[i][j],i+2])
    val.append(["calzado", calzado.iloc[i],i+2])
    val.append(["sistolica", sistolica.iloc[i],i+2])
    val.append(["diastolica", diastolica.iloc[i],i+2])

val.append(["altura",altura.iloc[31],32]) #porque altura tiene un dato mas
mediciones = pd.DataFrame(val)

#Llenar tabla Mediciones
for row in mediciones.iterrows():
    sql2 = "INSERT INTO Mediciones(tipo, medida, persona_id) VALUES (%s, %s, %s)"
    val = list(row[1])
    mycursor.execute(sql2, val)

mydb.commit()

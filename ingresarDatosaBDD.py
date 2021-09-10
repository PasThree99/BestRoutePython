import pandas as pd
import mysql.connector

df = pd.read_excel("/Users/user/Documents/Chamba isabel/Distancias con coeficiente (1).xlsx")
df = df[["Nombre","Latitud","Longitud"]]


conn = mysql.connector.connect(user='root', password='12345678', host='127.0.0.1', database='rutas')
cur = conn.cursor()



for i in range(len(df)):
    query = "INSERT INTO lugares (nombre, latitud, longitud) VALUES (%s,%s,%s)"
    data = []
    data.append(str(df.iloc[i]["Nombre"]))
    
    data.append(float(df.iloc[i]["Latitud"]))
    
    data.append(float(df.iloc[i]["Longitud"]))

    cur.execute(query,data)

conn.commit()

conn.close()


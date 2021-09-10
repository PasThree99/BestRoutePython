import mysql.connector

def getAPIKey():
    # Returns the updated API key value in a string
    conn = mysql.connector.connect(user='root', password='12345678', host='127.0.0.1', database='rutas')
    cur = conn.cursor()
    cur.execute("Select * From apiKey",[])
    r = cur.fetchall()
    conn.close()
    return r[0][0]

def getAllPlaces():
    # Returns a list of the names of all the registered places. Each name is a string in CAPS
    conn = mysql.connector.connect(user='root', password='12345678', host='127.0.0.1', database='rutas')
    cur = conn.cursor()
    cur.execute("Select Nombre From lugares",[])
    r = cur.fetchall()
    l = []
    for i in r:
        l.append(i[0])
    conn.close()
    return l

def getCoordinates(place):
    # Retunrs the coordinates of the given Place. If the place is not registeres returns None
    conn = mysql.connector.connect(user='root', password='12345678', host='127.0.0.1', database='rutas')
    cur = conn.cursor()
    cur.execute("Select latitud, longitud From lugares where nombre = %s",[place])
    r = cur.fetchall()
    if(len(r) < 1):
        print("No se encontro el lugar: " + place + "\nRevisa que este bien escrito")
        conn.close()
        return None
    t = [float(r[0][0]), float(r[0][1])]
    #print(t)
    conn.close()
    return t


def updateAPI (newKey):
    conn = mysql.connector.connect(user='root', password='12345678', host='127.0.0.1', database='rutas')
    cur = conn.cursor()
    cur.execute("Update apiKey set apiKey = %s where apiKey = %s;",[newKey,getAPIKey()])
    conn.commit()
    return True
    


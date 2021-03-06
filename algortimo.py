from dataBaseConections import getCoordinates
from itertools import permutations
from request import makeRequest

def ruta_a_seguir(lugares):
    origin = "MADER CENTER"
    ori_cords = getCoordinates(origin)
    k = 1
    dic = {}
    for i in lugares:
        dic [k] = i
        k += 1
    per = list(permutations(range(1,k)))

    tiempoMinimo = 10000000
    ordenFinal = []

    for orden in per:
        ua = "MADER CENTER"
        tiempoActual = 0
        for i in orden:
            ca = getCoordinates(ua)
            cs = getCoordinates(dic[i])
            req = makeRequest(ca,cs)
            print("De ",ua," a ",dic[i]," se hacen ", req, " segundos ")
            tiempoActual += req
            ua = dic[i]
        
        if(tiempoActual < tiempoMinimo):
            tiempoMinimo = tiempoActual
            ordenFinal.append(orden)
    
    ordenmin = ordenFinal[-1]
    ca = getCoordinates( ordenmin[-1])
    cf = getCoordinates( origin )

    r = makeRequest(ca,cf)

    tiempoMinimo += r    

        
    
    stf = origin +" -> "
    for lu in ordenFinal[-1]:
        stf = stf + dic[lu]
        
        stf += " -> "
    
    stf +=  origin

    return (stf,tiempoMinimo) 
            






archivo= open("..Archivos/Clificaciones_con_nombre.csv")
contenido = archivo.readlines()

print(contenido)

datos = [i.split(",") for i in contenido]

print(datos)

#datos = [[i[0], for i in datos]
#datos = [[i[0],i [1:]] for i in datos]
datos = [[i[0],list(map(int,i [1:]))] for i in datos]

print(datos)

#Calcular el promedio de cada alumno y agregar el resultado
#a la lista asociada al ususario
#datos= [i for i in datos]
datos= [[i[0],i [1],sum(i[1])/len(i[1])] for i in datos]
print(datos)

#      como graficas valores de es estilo grafiacar en pyton tambien

datos.sort(key=lambda x:x[2])

nombres=[i[0] for i in datos]
promedios=[i[2] for i in datos]

promedioGrupo=sum(promedios)/len(promedios)
promedioGrupo=[promedioGrupo for i in range(len(promedios))]
print(promedioGrupo)




from matplotlib import pyplot as plt

plt.bar(nombres,promedios)
plt.xlabel('nombre')
plt.ylabel('nombre')
plt.ylin(0,12)
plt.show()
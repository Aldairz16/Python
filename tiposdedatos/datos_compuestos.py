# lista 

lista = ['Aldair', 'Rukiur', True, 30.5 ]

# tupla

tupla = ('Aldair', 'Rukiur', True, 30.5 ) #Se usa parentesis para definir una tupla

lista[3] = 30.5 # No se puede cambiar el valor de una tupla, ya que es inmutable pero si se puede cambiar el valor de una lista

#conjunto (set)

conjunto = {'Aldair', 'Rukiur', True, 30.5, 'Aldair' } #Se usa llaves para definir un conjunto y no almacenan datos duplicados
print(conjunto)
# print (conjunto[0]) # No se puede acceder a los elementos de un conjunto por su indice, ya que no tienen orden

# diccionario (dict)

diccionario = {
    'nombre': 'Aldair',
    'apellido': 'Pacherrez',
    'estado emocional': True,
    'estatura': 1.75 #la ultima no lleva coma
}

print(diccionario['nombre']) # Se accede a los elementos de un diccionario por su clave
print(lista[3]) # Se accede a los elementos de una lista por su indice
print(diccionario['estatura']+ 3)
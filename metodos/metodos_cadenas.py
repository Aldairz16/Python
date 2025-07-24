cadena1 = "Hola soy Aldair"
cadena2 = "Bienvendido a Python"

#convierte a mayusculas
resultado = cadena1.upper()
#convierte a minusculas
resultado2 = cadena2.lower()  
#primera letra en mayusculas
resultado3 = cadena1.capitalize()
#-----------------------------------------
#buscar una cadena dentro de otra, sino existe devuelve -1
resultado4 = cadena1.find("H")  
#busqueda una cadena dentro de otra, sino existe devuelve exepción
resultado5 = cadena1.index("H")
#-----------------------------------------
#si es numerico devuelve True, sino False
resultado6 = cadena1.isnumeric()
#si es alfanumerico devuelve True, sino False
resultado7 = cadena1.isalnum()
#------------------------------------------
#devuelve la cantidad de veces que se repite una cadena dentro de otra(metodo)
resultado8 = cadena1.count("a")
#contar caracteres de una cadena (funcion)
resultado9 = len(cadena1)
#------------------------------------------
#verifica si una cadena empieza con otra
resultado10 = cadena1.startswith("Hola")
#verifica si una cadena termina con otra
resultado11 = cadena1.endswith("Aldair ")
#remplaza un pedazo de la cadena por otra
resultado12 = cadena1.replace("Aldair", "Python")
#separa una cadena en una lista
resultado13 = cadena1.split(" ")
print(resultado12)
print(resultado13)
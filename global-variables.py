# VARIABLES GLOBALES Y VARIABLES LOCALES
# Las variables que creamos afuera de una función son llamada globales.
# Las variables que creamos dentro de una función son llamada locales.

name = "Koche" # Asigno la variable global fuera de la función y su valor.

def function(): # Defino la función.
  name = "Steve" # Asigno la variable local dentro de la función y asigno su valor.
  print('Hi! I am ' + name) # Imprimo el mensaje con la variable local "Steve"

function() # Ejecuto la función creada.

print('Hi! I am ' + name) # Imprimo el mensaje con la variable global "Koche"

# VARIABLES LOCALES
# Las variables que creamos dentro de una función son llamada locales.
# Pero mediante la palabra clave GLOBAL dentro de la función definida, puedo cambiar origen de local a global.

name = "Koche" # Asigno la variable global fuera de la función y su valor.

def function(): # Defino la función.
  global name # Asigno con la keyword GLOBAL el alcance que tendrá mi variable name. En este caso será global aun estando dentro de la función.
  name = "Steve" # Asigno la variable local dentro de la función y asigno su valor.

function() # Ejecuto la función creada.

print('Hi! I am ' + name) # Muestro en pantalla el mensaje con la variable global. El valor de la variable será "Steve".
input() # Salgo del programa

# Notar que la variable name fuera de la función contenía el valor "Koche".
# Pero luego, dentro de la función, se asignó el alcance global a la variable con el valor "Steve".

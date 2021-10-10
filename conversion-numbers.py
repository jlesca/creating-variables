# CONVERTIR TIPO DE DATOS NUMERICOS
# Podemos convertir el tipo de dato de una variable asignandole el nuevo tipo de dato.

a = 1 # int
b = 1.5 # float
c = 1j # complex

x = float(a) # El tipo de dato int pasará a ser float
y = int(b) # El tipo de dato float pasará a ser int
z = complex(a) # El tipo de dato int pasará a ser complex

print(x) # Esto muestra 1.0
print(y) # Esto muestra 1
print(z) # Esto muestra (1+0j)

print(type(x)) # Mostrará class 'float'
print(type(y)) # Mostrará class 'int'
print(type(z)) # Mostrará class 'complex'

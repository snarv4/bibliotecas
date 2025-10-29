alumno = {
    "nombre": "Juan Perez",
    "edad": 21,
    "notas": [85,90,78],
    "curso": "Segundo de Bachillerato"
}
# print(alumno["nombre"])

for clave in alumno.keys():
    print (clave)

for valor in alumno.values():
    print (valor)

for clave, valor in alumno.items():
    print(f"propiedad: {clave} -> {valor}")
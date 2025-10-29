alumnos = [
    {
        "nombre": "Lety",
        "notas": [8.0,7.5,8.5]
    },
    {
        "nombre": "Damian",
        "notas": [9.0,6.5,9.5]
    },
    {
        "nombre": "Benito",
        "notas": [10.0,8.5,6.5]
    }
]

suma_promedios_individuales = 0
contador_alumnos = 0

for alumno in alumnos:
    # Capturando los nombres y las notas de mis bibliotecas
    nombre = alumno["nombre"]
    notas = alumno["notas"]
    promedio_individual = sum(notas) / len(notas)
    print(promedio_individual)
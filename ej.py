import json
from datetime import datetime
from openpyxl import Workbook

# Respuesta de la API en formato JSON
json_response = '''
[
  {
    "salary": "$3,946.45",
    "age": 23,
    "name": "Bird Ramsey",
    "gender": "male",
    "proyect": "NIMON",
    "email": "birdramsey@nimon.com"
  },
  {
    "salary": "$2,499.49",
    "age": 31,
    "name": "Jonathan Martinez",
    "gender": "male",
    "proyect": "LUXURIA",
    "email": "jonatanmart@luxuria.com"
  },
  {
    "salary": "$2,820.18",
    "age": 34,
    "name": "Kristie Cole",
    "gender": "female",
    "proyect": "QUADEEBO",
    "email": "kristiecole@quadeebo.com"
  },
  {
    "salary": "$3,277.32",
    "age": 30,
    "name": "Leonor Cross",
    "gender": "female",
    "proyect": "GRONK",
    "email": "leonorcross@gronk.com"
  },
  {
    "salary": "$1,972.47",
    "age": 28,
    "name": "Marsh Mccall",
    "gender": "male",
    "proyect": "ULTRIMAX",
    "email": "marshmccall@ultrimax.com"
  },
  {
    "salary": "$3,124.45",
    "age": 25,
    "name": "Carlitos Jonas",
    "gender": "male",
    "proyect": "NIMON",
    "email": "carlitosjonas@nimon.com"
  },
  {
    "salary": "$1,499.49",
    "age": 34,
    "name": "Bordell Carlman",
    "gender": "female",
    "proyect": "LUXURIA",
    "email": "lillianburgess@luxuria.com"
  },
  {
    "salary": "$2,420.18",
    "age": 34,
    "name": "Cristina Cole",
    "gender": "female",
    "proyect": "QUADEEBO",
    "email": "criscol@quadeebo.com"
  },
  {
    "salary": "$4,277.32",
    "age": 30,
    "name": "Leonora Ruseleve",
    "gender": "female",
    "proyect": "GRONK",
    "email": "leonorarus@gronk.com"
  },
  {
    "salary": "$2,972.47",
    "age": 28,
    "name": "Martiño Rivas",
    "gender": "male",
    "proyect": "ULTRIMAX",
    "email": "marriv@ultrimax.com"
  }
]
'''

# Cargar los datos
employees = json.loads(json_response)

# Obtener fecha actual
now = datetime.now()
fecha = now.strftime("%b-%Y")

wb = Workbook()
ws = wb.active
ws.title = "Pagos Empleados"

# Encabezados
ws.append(["Nombre", "Edad", "Proyecto", "Salario","Email"])

# Procesar datos y agregar al documento Excel
for employee in employees:
    if employee["proyect"] != "GRONK":  # Excluir empleados
        nombre = employee["name"]
        edad = employee["age"]
        proyecto = employee["proyect"]
        salario = float(employee["salary"].replace("$", "").replace(",", "")) # Eliminar $ y añadir €
        email = employee["email"]
        if edad < 30:
            salario *= 1.10  # Aumentar el salario en un 10% para empleados menores de 30 años
        salario = f'{salario}€';
        ws.append([nombre, edad, proyecto, salario, email])

# Crear el documento Excel
nombre_archivo = f"pagos-empleados-{fecha}.xlsx"
wb.save(nombre_archivo)

print(f"El archivo '{nombre_archivo}' ha sido creado exitosamente.")

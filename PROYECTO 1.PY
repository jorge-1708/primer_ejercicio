import pandas as pd
import random
import os

# Definir operaciones matemáticas con funciones lambda
operations = {
    'SUM': lambda x, y: x + y,
    'SUB': lambda x, y: x - y,
    'MUL': lambda x, y: x * y,
    'DIV': lambda x, y: x / y if y != 0 else None,  # Evita división por cero
    'POW': lambda x, y: x ** y if y < 10 else None  # Limita exponentes grandes
}

# Asegurar que la carpeta 'data' exista
output_dir = './data'
os.makedirs(output_dir, exist_ok=True)

# Generar datos
data = []
for _ in range(1000):
    operation = random.choice(list(operations.keys()))
    operand_1 = random.randint(1, 1000)
    operand_2 = random.randint(1, 1000)

    # Ajustar valores específicos
    if operation == 'POW':
        operand_2 = random.randint(1, 5)  # Limitar exponente para evitar números grandes
    elif operation == 'DIV' and operand_2 == 0:
        operand_2 = random.randint(1, 1000)  # Evitar división por cero

    # Calcular resultado usando el diccionario de operaciones
    result = operations[operation](operand_1, operand_2)

    # Agregar a la lista de datos
    data.append([operation, operand_1, operand_2, result])

# Crear DataFrame con Pandas
df = pd.DataFrame(data, columns=['operation', 'operand_1', 'operand_2', 'result'])

# Guardar archivo CSV
csv_path = os.path.join(output_dir, 'math_operations.csv')
df.to_csv(csv_path, index=False)

print(f"✅ Archivo CSV generado correctamente en: {csv_path}")

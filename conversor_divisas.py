# 📚 Ejercicio Avanzado 1: "Conversor de Divisas (Cotización en vivo)"
#
# 🎯 Objetivo:
# Crear un pequeño proyecto que consuma una API pública de cotizaciones y
# muestre los valores en una tabla prolija por consola, integrando entorno
# virtual, librerías de terceros, manejo de errores y buenas prácticas.
#
# 📄 Enunciado:
# Desarrollá un programa de consola que:
#   1. Le pida al usuario un monto en pesos argentinos (ARS).
#   2. Consulte la cotización actual del dólar desde una API pública
#      (por ejemplo: https://dolarapi.com/v1/dolares).
#   3. Convierta ese monto a dólar oficial y dólar blue usando el precio de
#      VENTA (es el precio al que se compran dólares con pesos):
#         total_usd = monto_ars / venta
#      En la respuesta de la API, cada cotización es un diccionario; las que
#      interesan tienen "casa" igual a "oficial" y "blue".
#   4. Muestre el resultado en una tabla ordenada (nombre, compra, venta,
#      total convertido).
#
# 🧩 Librerías de terceros a usar (mínimo 2, instalar con pip):
#   - requests     → para hacer la petición HTTP a la API.
#   - tabulate     → para imprimir los resultados en formato de tabla.
#
# 🛠️ Pasos obligatorios del proyecto:
#   1. Crear una carpeta para el proyecto (ej: "conversor_divisas/").
#   2. Crear el entorno virtual:        python -m venv .venv
#   3. Activarlo:
#         Linux/Mac:   source .venv/bin/activate
#         Windows:     .venv\Scripts\activate
#   4. Instalar las librerías:          pip install requests tabulate
#   5. Congelar las dependencias:       pip freeze > requirements.txt
#   6. Escribir un README.md que explique qué hace el proyecto, cómo crear
#      el entorno virtual, cómo instalar las dependencias y cómo ejecutarlo.
#
# ✅ Requerimientos técnicos:
#   - Manejar TODOS los errores posibles con try / except
#     (sin conexión, API caída, monto no numérico, datos faltantes, etc.).
#   - Cada función debe tener su docstring explicando qué hace.
#   - Usar anotación de tipos en parámetros y valores de retorno.
#   - Respetar PEP8 (nombres, espacios, longitud de línea, sangría).
#   - Entregar la carpeta del proyecto con: el .py, requirements.txt y
#     README.md.

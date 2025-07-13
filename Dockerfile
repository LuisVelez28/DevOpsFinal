# 1. Usar una imagen base oficial de Python
FROM python:3.9-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar el archivo de requerimientos y las dependencias
COPY requirements.txt .

# 4. Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar todo el código del proyecto al directorio de trabajo
COPY . .

# 6. Exponer el puerto en el que correrá la aplicación
EXPOSE 5000

# 7. Comando para iniciar la aplicación cuando el contenedor arranque
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
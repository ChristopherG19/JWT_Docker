# Etapa de construcción
FROM node:18.17.0-alpine AS builder

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos del proyecto al directorio de trabajo
COPY . .

# Instala las dependencias del proyecto
RUN npm install

# Exponer puerto 4200
EXPOSE 4200

# Comando para ejecutar el servidor de desarrollo de Vite
CMD ["npm", "run", "dev"]


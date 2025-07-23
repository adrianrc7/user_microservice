# 🧙‍♂️ User Microservice - Fantasy Project

Este microservicio se encarga de la **gestión de usuarios** en una aplicación de tipo Fantasy. Ha sido desarrollado en **Python** utilizando el microframework **Flask**, y emplea **MongoDB** como sistema de almacenamiento de datos.

## 🚀 Funcionalidad

- Registro de usuarios
- Inicio de sesión y autenticación
- Gestión del perfil de usuario:
  - Nombre de usuario
  - Correo electrónico
  - Contraseña cifrada
  - Fecha de registro
  - Avatar personalizado
  - Idioma preferido
  - Roles (usuario normal o administrador)
  - Jugadores favoritos
  - Estado del usuario (activo/inactivo)
- Control de acceso para administradores
- Base para futuras extensiones (puntos, clasificaciones, etc.)

## ⚙️ Tecnologías usadas

- Python 3
- Flask
- MongoDB
- PyMongo
- bcrypt (para cifrado de contraseñas)
- Flask-Cors 

## 📁 Estructura del proyecto (en desarrollo)

```bash
user-microservice/
├── app.py
├── models/
│   └── user.py
├── routes/
│   └── user_routes.py
├── utils/
│   └── auth.py
├── requirements.txt
├── README.md
```

## 📦 Instalación y ejecución

> Requiere Python 3.9+ y un servidor MongoDB en funcionamiento.

```bash
# Clonar el repositorio
git clone https://github.com/tu_usuario/user-microservice.git

# Entrar al directorio del proyecto
cd user-microservice

# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
flask run
```

## 🛠 En desarrollo

- [ ] CRUD completo de usuarios
- [ ] Validación y sanitización de campos
- [ ] Gestión avanzada de roles
- [ ] Tests unitarios

## 🧑‍💻 Autor

**Adrián Ramos Caballero**  
Estudiante de Ingeniería del Software – Universidad de Extremadura  

---

> Este microservicio forma parte de un sistema distribuido de microservicios para una aplicación de Fantasy Sports. Más información próximamente.

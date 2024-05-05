from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
import jwt
from functools import wraps

# Se crea la app, se agregan CORS y se define la secret_key
app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'chris20541'

# Simular base de datos de usuarios
users = {}

# Se realiza evaluación de token, esta función sustituye la directiva @jwt_required proveniente de jwt.security
def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split()[1]

        if not token:
            return jsonify({'message': 'Token de autenticación faltante'}), 401

        try:
            data = jwt.decode(token, app.config['JWT_SECRET_KEY'], algorithms=["HS256"])
            current_user = data['username']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token de autenticación expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token de autenticación inválido'}), 401

        return f(current_user, *args, **kwargs)

    return decorated_function

# Ruta para el registro de usuarios
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Se revisa en la "base de datos"
    if username in users:
        return jsonify({'message': 'El usuario ya existe'}), 400

    hashed_password = generate_password_hash(password)
    users[username] = hashed_password

    return jsonify({'message': 'Usuario registrado exitosamente'}), 201

# Ruta para el inicio de sesión y generación de token JWT
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username not in users or not check_password_hash(users[username], password):
        return jsonify({'message': 'Credenciales inválidas'}), 401
    
    # Se genera como el ejercicio anterior
    payload = {"username": username}
    token = jwt.encode(payload, app.config["JWT_SECRET_KEY"], algorithm="HS256")
    print(token)

    return jsonify({'access_token': token})

# Ruta protegida que requiere un token JWT válido para acceder
@app.route('/protected', methods=['GET'])
@token_required
def protected(username):
    return jsonify({'message': f'Hola {username}'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

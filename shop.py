import os
import base64
import logging
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import sentry_sdk
import functions 

sentry_sdk.init(
    dsn="https://9ab31e2e0d0c98fe8f441409d641da50@o4509040092446720.ingest.us.sentry.io/4509040094871552",
    send_default_pii=True,
    traces_sample_rate=1.0
)

# Configuración de logs
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

USERNAME = "admin"
PASSWORD = "admin"
SALT = b'salt_'

# Protección de contraseña
def generate_key(password: str, salt: bytes = SALT):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

# Registro de usuarios
def register_user(username: str, password: str):
    try:
        key = generate_key(password)
        f = Fernet(key)
        encrypted_password = f.encrypt(password.encode()).decode()

        with open("usuarios.txt", "a") as file:
            file.write(f"{username}:{encrypted_password}\n")

        logging.info("Usuario %s registrado con éxito.", username)
        print("Usuario registrado con éxito.")

    except Exception as e:
        logging.error("Error al registrar usuario: %s", str(e))
        sentry_sdk.capture_exception(e)

# Autenticación de usuarios
def authenticate(user, password):
    try:
        if not os.path.exists("usuarios.txt"):
            print("No hay usuarios registrados.")
            return False

        with open("usuarios.txt", "r") as file:
            users = file.readlines()

        for u in users:
            saved_user, saved_enc_pass = u.strip().split(":")

            key = generate_key(password)
            f = Fernet(key)
            
            try:
                decrypted_password = f.decrypt(saved_enc_pass.encode()).decode()
            except Exception:
                continue  # Si la clave no coincide, seguir buscando

            if saved_user == user and decrypted_password == password:
                logging.info("Inicio de sesión exitoso para usuario: %s", user)
                return True

        logging.warning("Intento de inicio de sesión fallido para usuario: %s", user)
        print("Credenciales incorrectas.")
        return False

    except Exception as e:
        logging.error("Error en autenticación: %s", str(e))
        sentry_sdk.capture_exception(e)
        return False

# Función principal
if __name__ == "__main__":
    print("\nBienvenido")
    print("¿Qué operación desea realizar?")
    print("1. Registrarse")
    print("2. Iniciar sesión")
        
    choice = input("Seleccione una opción: ")

    if int(choice) == 1:
        user = input("Ingrese un nombre de usuario: ")
        pwd = input("Ingrese una contraseña: ")
        register_user(user, pwd)

    elif int(choice) == 2:
        user = input("Usuario: ")
        pwd = input("Contraseña: ")
        
        if authenticate(user, pwd):
            functions.menu_principal()  
        else:
            print("Acceso denegado.")
    else: 
        print("Error. Opción no válida")

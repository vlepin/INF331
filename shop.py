import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

def generate_key(password: str, salt: bytes = b'salt_'):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def register_user(username: str, password: str):
    key = generate_key(password)
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode()).decode()
    with open("usuarios.txt", "a") as file:
        file.write(f"{username}:{encrypted_password}\n")
    print("Usuario registrado con éxito.")

def authenticate_user(username: str, password: str) -> bool:
    if not os.path.exists("usuarios.txt"):
        print("No hay usuarios registrados.")
        return False
    with open("usuarios.txt", "r") as file:
        for line in file:
            stored_user, stored_password = line.strip().split(":")
            if stored_user == username:
                key = generate_key(password)
                f = Fernet(key)
                try:
                    if f.decrypt(stored_password.encode()).decode() == password:
                        return True
                except:
                    return False
    return False

if __name__ == "__main__":
    choice = input("¿Desea registrarse (R) o iniciar sesión (L)? ").strip().lower()
    if choice == "r":
        user = input("Ingrese un nombre de usuario: ")
        pwd = input("Ingrese una contraseña: ")
        register_user(user, pwd)
    elif choice == "l":
        user = input("Usuario: ")
        pwd = input("Contraseña: ")
        if authenticate_user(user, pwd):
            print("Inicio de sesión exitoso.")
            from functions import menu_principal
            menu_principal()
        else:
            print("Credenciales incorrectas.")
import hashlib
import hmac

# Doc: https://recursospython.com/guias-y-manuales/hashlib-md5-sha/

# ----1. REGISTER----------
# Variable que almacena una contraseña en string
mypassword = "pss"
# ----1.1. CODIFICACIÓN
# El método encode() devuelve una versión codificada de la cadena dada.
encode_pass = mypassword.encode()
# ----1.2 # md5 es un algoritmo de encriptación
hash_pass = hashlib.md5(encode_pass)
# ----1.2. CIFRADO
# hesdigest() cifra la cadena en hexadecimal
crypt_pass = hash_pass.hexdigest()
# ---------------------------------------------------------------------------------
# ----2. LOGIN
read_password = "pss"  # Good password
# read_password = "hola" # Bad password
# ----2.1. Se codifican los valores introducidos
encode_verify_pass = hashlib.md5(read_password.encode())
# ----2.2. Se elige el tipo de cifrado
crypt_verify_pass = encode_verify_pass.hexdigest()
# ----2.3. Se comparan las claves cifradas
if hmac.compare_digest(crypt_pass, crypt_verify_pass):
    print("Bienvenido!")
else:
    print("Contraseña incorrecta")

# ----3. OTROS COMPONENTES
# ----3.1. DECODIFICAR
decode_pass = encode_pass.decode()
print("Clave decodificada: {0}\nClave codificada: {1}".format(
    decode_pass, encode_pass))

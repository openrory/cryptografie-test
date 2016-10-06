from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()


def encrypt(invoerstring:str, key)->str:
    token = f.encrypt(invoerstring)
    return token


def decrypt(invoerstring:str, f)->str:
    return f.decrypt(invoerstring)

beginstation = input('Wat is je beginstation?')
eindstation = input('Wat is je eindstation?')
naam= input('Wat is je naam?')

text = beginstation + eindstation + naam #concateneer de inputstrings
binary_data = text.encode('utf-8') #zet de string om naar de vereiste utf-8 encodering
key = generate_key() #genereer een unieke key om te coderen
f = Fernet(key) # maak een nieuw Fernet object aan
token = encrypt(binary_data, key) #maak een encrypted string (token) aan

print('token:', token)
decrypted = decrypt(token, f) #decrypt de token
utf8_decrypted = decrypted.decode('utf-8') #zet de decrypted string om naar utf-8 encodering
print('decrypted token:', utf8_decrypted)
print('hoi')

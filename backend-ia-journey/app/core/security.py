from pwdlib import PasswordHash


pwd_hash = PasswordHash.recommended()

def hash_password(plain_password: str)-> str:
    return pwd_hash.hash(plain_password)

def verify_password(plain_password:str, password_hashed:str)->str:
    return pwd_hash.verify(plain_password,password_hashed)

import bcrypt


def hash_password(password: str) -> str:
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()  # Generate a salt
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return str(hashed_password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    password_byte_enc = plain_password.encode('utf-8')
    return bcrypt.checkpw(password=password_byte_enc, hashed_password=hashed_password.encode('utf-8'))
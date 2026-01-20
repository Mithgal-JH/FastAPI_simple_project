from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

class Hash():
    def hash_password(password: str) -> str:
        return password_hash.hash(password)
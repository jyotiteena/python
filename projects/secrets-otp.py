import secrets
import string

chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(chars) for _ in range(8))
print("Secure password using secrets module:", password)
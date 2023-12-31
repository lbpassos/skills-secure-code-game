import binascii
import random
import secrets
import hashlib
import os
import bcrypt

# My solution. strong password hashing algorithm (and includes a per-password salt by default)
from argon2 import PasswordHasher
import scrypt

class Random_generator:

    # generates a random token
    def generate_token(self, length=8, alphabet=(
    '0123456789'
    'abcdefghijklmnopqrstuvwxyz'
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    )):
        return ''.join(random.choice(alphabet) for _ in range(length))

    # generates salt
    def generate_salt(self, rounds=12):
        salt = ''.join(str(random.randint(0, 9)) for _ in range(21)) + '.'
        return f'$2b${rounds}${salt}'.encode()

# Now argon2
class SHA256_hasher:

    # produces the password hash by combining password + salt because hashing
    def password_hash(self, password, salt):
        '''
        password = binascii.hexlify(hashlib.sha256(password.encode()).digest())
        password_hash = bcrypt.hashpw(password, salt)
        return password_hash.decode('ascii')
        '''
        #No need to use salt. Already in default
        ph = PasswordHasher()
        return ph.hash(password) # GOOD

    # verifies that the hashed password reverses to the plain text version on verification
    def password_verification(self, password, password_hash):
        '''
        password = binascii.hexlify(hashlib.sha256(password.encode()).digest())
        password_hash = password_hash.encode('ascii')
        return bcrypt.checkpw(password, password_hash)
        '''
        ph = PasswordHasher()
        return ph.verify(password_hash, password) # GOOD

# Now scrypt
class MD5_hasher:

    # same as above but using a different algorithm to hash which is MD5
    def password_hash(self, password):
        #return hashlib.md5(password.encode()).hexdigest()
        maxtime=0.5
        return scrypt.encrypt(password, PASSWORD_HASHER, maxtime=maxtime)

    def password_verification(self, password, password_hash):
        #password = self.password_hash(password)
        #return secrets.compare_digest(password.encode(), password_hash.encode())
        maxtime=0.5
        try:
            scrypt.decrypt(password_hash, PASSWORD_HASHER, maxtime)
            return True
        except scrypt.error:
            return False

# a collection of sensitive secrets necessary for the software to operate
PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
PUBLIC_KEY = os.environ.get('PUBLIC_KEY')
SECRET_KEY = 'TjWnZr4u7x!A%D*G-KaPdSgVkXp2s5v8'
PASSWORD_HASHER = 'MD5_hasher'

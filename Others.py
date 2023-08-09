import hashlib
import secrets

class HashGen:
    @staticmethod
    def generate_random_hash():
        random_string = secrets.token_hex(16)  # Generate a random string
        hash_value = hashlib.sha256(random_string.encode('utf-8'))
        
        return hash_value.hexdigest()

if __name__ == '__main__':
    MyHash = HashGen.generate_random_hash()

    print(MyHash)
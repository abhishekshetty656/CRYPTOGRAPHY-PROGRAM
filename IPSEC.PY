import hashlib

def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

data = input("Enter the data to send ")
hash_value = generate_hash(data)

print("Generate Hash:", hash_value)

received_data =  input("Enter the received data")

received_hash = generate_hash(received_data)

if received_hash == hash_value:
    print("Integrity verified: Data not modified ")
else:
    print("Integrity Failed: Data Modified")
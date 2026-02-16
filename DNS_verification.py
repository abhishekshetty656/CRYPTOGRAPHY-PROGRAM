import hashlib

def sign_data(data):
    return hashlib.sha256(data.encode()).hexdigest()
original_domain = input("Enter the original domainname: ")
signature = sign_data(original_domain)

print("\nGenerate DNS signature:", signature)
received_domain = input("\nEnter the received domain name ")
verify_signature = sign_data(received_domain)

if verify_signature == signature:
    print("\n DNSSEC verification successful: Data is authentic ")
else:
    print("\n DNSSEC verification failed: Data has been modified")
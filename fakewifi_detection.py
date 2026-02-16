import hashlib
trusted_dns_records = {
    "google.com":hashlib.sha256("Google.com".encode()).hexdigest(),
    "amazon.com":hashlib.sha256("amazon.com".encode()).hexdigest(),
    "facebook.com":hashlib.sha256("facebook.com".encode()).hexdigest()
}

user_domain = input("Enter website domain")
if user_domain in trusted_dns_records:
    user_hash = hashlib.sha256(user_domain.encode())

    if user_hash == trusted_dns_records[user_domain]:
        print("\n Website is authentic (Not fake)")
        print("DNSSEC verification successful ")
    else:
        print("\nWarning! Website data modified ")
        print("DNSSEC Verification Failed ")

else:
    print("\n Warning ! website data modified ")
    print("Domain not found in trusted DNS records")
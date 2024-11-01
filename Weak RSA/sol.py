from cryptography.hazmat.primitives import serialization
from Crypto.Util.number import bytes_to_long,long_to_bytes
# Load the public key
with open("key.pub", "rb") as key_file:
    public_key = serialization.load_pem_public_key(key_file.read())

# Get the public numbers
numbers = public_key.public_numbers()
n = numbers.n  # Modulus
e = numbers.e  # Exponent

print(f"Modulus (n): {n}")
print(f"Exponent (e): {e}")

p=28064707897434668850640509471577294090270496538072109622258544167653888581330848582140666982973481448008792075646342219560082338772652988896389532152684857
q= 	20423438101489158688419303567277343858734758547418158024698288475832952556286241362315755217906372987360487170945062468605428809604025093949866146482515539
phi=(p-1)*(q-1);
with open("flag.enc", "rb") as file:
    encrypted_data = file.read();
ct=bytes_to_long(encrypted_data);
d=pow(e,-1,phi);
print(long_to_bytes(pow(ct,d,n)))
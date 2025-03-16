import random

#1)get gdc of 2 numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#2) modular inverse of public exponent and phi, beinh phi'Φ'=((p-1)*(q-1))
def mod_inverse(e, phi):
    for d in range(3, phi):
        if (e * d) % phi == 1:
            return d
    return None

#3) define function to vlidate the primarity of n
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
#4) randomly generate the value of p and q being primes above 1000 ( higher value == more secure)
def generate_prime(min_value=10000):
    while True:
        num = random.randint(min_value, min_value * 2)
        if is_prime(num):
            return num

#5) function to generate values of p and q and an static e
# knowing that the values of p and q are higher than 1000, 17 will always fit  
def generate_rsa_keys():
    p = generate_prime()
    q = generate_prime()
    e = 17  # e defined as a static value  coprime with p and q number.
    n = p * q
    phi = (p - 1) * (q - 1)
    
    #6) Compute modular inverse of e if does exists ( should always exist )
    d = mod_inverse(e, phi)
    if d is None:
        raise ValueError("No modular inverse found for the given e")
    
    public_key = (e, n) #public key variables defined ( encryption )
    private_key = (d, n) #private key variavles ( decryption )
    
    return public_key, private_key, p, q

#7) function to encrypt a message using public key values 
def encrypt(message, public_key):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher

#8) function to decrypt the message using the private key variables 
def decrypt(cipher, private_key):
    d, n = private_key
    decrypted_message = ''.join(chr(pow(char, d, n)) for char in cipher)
    return decrypted_message

# main function printing all values for understanding
if __name__ == "__main__":
    print("""

    ____  _____ ___       ___    __           
   / __ \/ ___//   |     /   |  / /___ _____  
  / /_/ /\__ \/ /| |    / /| | / / __ `/ __ \ 
 / _, _/___/ / ___ |   / ___ |/ / /_/ / /_/ / 
/_/ |_|/____/_/  |_|  /_/  |_/_/\__, /\____(_)
                               /____/         
                              by: nomespaladin
    """)
    print("Defined values by this program, this time ")
    print("-"*40)
    public_key, private_key, p, q = generate_rsa_keys()
    print(f"Generated Prime p: {p}")
    print(f"Generated Prime q: {q}")    
    print(f"Public Key (e, n): {public_key}")
    print(f"Private Key (d, n): {private_key}")
    print("-"*40)
    
    message = input("Message to encrypt:")
    
    cipher = encrypt(message, public_key)
    print(f"Encrypted Message: {cipher}")
    
    decrypted_message = decrypt(cipher, private_key)
    print(f"Decrypted Message: {decrypted_message}")
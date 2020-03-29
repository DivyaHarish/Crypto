LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"    #key space

#conditioning of the plain text and function calls (encrypt and decrypt)
def main():
    key = "PIZZA"
    msg = "COMMON SENSE IS NOT SO COMMON"


    msg=msg.strip().replace(" ","")
    print(msg)

    cipher = ''.join(encrypt(key,msg))
    print(cipher)
    plain = ''.join(decrypt(key,cipher))
    print(plain)

#encrypt function accepts a key and message to encrypt the message using VIgnere polyalphabetic cipher
def encrypt(key,msg):
    encrypt_msg = []
    for i in range(0,len(msg)):
        num1=(LETTERS.find(key[i%len(key)]))
        num2=(LETTERS.find(msg[i]))
        num = (num1 + num2)%26 #(LETTERS.find(key[i%len(key)]) + LETTERS.find(msg[i])) % 26
        encrypt_msg.append(LETTERS[num])
    return encrypt_msg

#decrypt function operates on the cipher text and calculates the plain text provided the key is known
def decrypt(key,msg):
    decrypt_msg = []
    for i in range(0,len(msg)):
        num = ( LETTERS.find(msg[i]) - LETTERS.find(key[i%len(key)]) ) %26   #msg - key
        decrypt_msg.append(LETTERS[num])
    return decrypt_msg

main()

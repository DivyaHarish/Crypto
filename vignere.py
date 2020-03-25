LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def main():
    key = "PIZZA"
#    key = "Z"
    msg = "COMMON SENSE IS NOT SO COMMON"
#    msg = "S"

    msg=msg.strip().replace(" ","")
    print(msg)

    cipher = ''.join(encrypt(key,msg))
    print(cipher)
    plain = ''.join(decrypt(key,cipher))
    print(plain)

def encrypt(key,msg):
    encrypt_msg = []
    for i in range(0,len(msg)):
        num1=(LETTERS.find(key[i%len(key)]))
        #print(num1)
        num2=(LETTERS.find(msg[i]))
        #print(num2)
        num = (num1 + num2)%26 #(LETTERS.find(key[i%len(key)]) + LETTERS.find(msg[i])) % 26
        encrypt_msg.append(LETTERS[num])
    return encrypt_msg

def decrypt(key,msg):
    decrypt_msg = []
    for i in range(0,len(msg)):
        num = ( LETTERS.find(msg[i]) - LETTERS.find(key[i%len(key)]) ) %26   #msg - key
        decrypt_msg.append(LETTERS[num])
    return decrypt_msg

main()

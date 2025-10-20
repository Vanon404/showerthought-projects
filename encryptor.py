

message=input('Enter your message: ')

 
def encryptor(message, shift):
    result = ""
    for char in message:
          result += chr((ord(char) + shift )% 256)
    return result

hello = encryptor(message , 4)

print('encryption:  ', hello)

def decryptor(hello, shift):
    result = ""
    for char in hello:
          result += chr((ord(char) - shift )% 256)
    return result

decrypted = decryptor( hello , 4)

anotheritem = input("do you want to decrypt? yes/no: ")

if anotheritem.lower() == "yes":
    
    
    print('Decrypted message: ', decrypted)

else: 
    print("Thank you for using our service!")




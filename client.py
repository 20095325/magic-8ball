import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""
Start connection to server
"""
s.connect(('127.0.0.1', 1235))

print('Ask the Magic 8 Ball a Question:')

while True:
    """
    Allow the client to ask a question, this will keep looping.
    """
    question = input('Q: ')
    s.send(question.encode())
    if question == "exit":
        break
    print('A:', s.recv(1024).decode())
s.close()

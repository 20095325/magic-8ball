import socket
import random
import signal

possible_answers = [
        'It is certain',
        'It is decidedly so',
        'Without a doubt',
        'Yes definitely',
        'You may rely on it',
        'As I see it, yes',
        'Most likely',
        'Outlook good',
        'Yes',
        'Signs point to yes',
        'Reply hazy, try again',
        'Ask again later',
        'Better not tell you now',
        'Cannot predict now',
        'Concentrate and ask again',
        'Don`t count on it',
        'My reply is no',
        'My sources say no',
        'Outlook not so good',
        'Very doubtful'
    ]


def receive_signal():
    """
    Function that allows the user to give input once the OS signal has been made.
    This will stop the server or do nothing
    """
    close = input('Are you sure you want to close the application? y/n:')
    if close == 'y':
        if client_socket:
            client_socket.close()
        exit()


signal.signal(signal.SIGINT, receive_signal)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    """
    Start the server and listen on a while loop 
    """
    s.bind(('127.0.0.1', 1235))
    s.listen(5)
    client_socket = None
    while True:
        try:
            client_socket, client_addr = s.accept()
            print(f'Connection from {client_addr} has been established!')
            while True:
                question = client_socket.recv(1024).decode()
                if question == 'exit':
                    break
                random.seed(question)
                answer = random.choice(possible_answers)
                client_socket.send(bytes(answer, 'utf-8'))
        except (OSError, socket.error) as e:
            print('there was an error, resetting.')
            client_socket.close()
        else:
            print('client closed the connection, resetting.')
            client_socket.close()




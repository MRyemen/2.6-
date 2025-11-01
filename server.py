""""

Author:Dvir Zilber

Program name:Service.py

Description: A program that connects a client to the server recives a command and sends back the requested data.

Date:11/1/25

"""


import socket
import random
import datetime
import logging

SERVER_IP = '0.0.0.0'
SERVER_PORT = 1712
MAX_PACKET = 1024
NAME = 'Dvirs server'



def name():
    """
    Returns the constant name of the server.
    """
    return NAME


def random_num():
    """
    Returns a random number between 1 and 10 as a string.
    """
    response = str(random.randint(1, 10))
    return response


def get_time():
    """
    Returns the current date and time as a string.
    """
    response = str(datetime.datetime.now())
    return response



def handle_client(client_socket):
    """
    Receives commands from the connected client and sends back the requested data.
    Handles commands: TIME, NAME, RAND, EXIT.
    Closes the connection when 'EXIT' is received or the connection is lost.
    """
    while True:
        cmd = client_socket.recv(4).decode().strip()  #gets the user input
        if not cmd:
            break

        if cmd == 'TIME':
            response = get_time()
            logging.info('command is' "TIME")

        elif cmd == 'NAME':
            response = NAME
            assert(response == 'Dvirs server')
            logging.info('command is' "NAME")
        elif cmd == 'RAND':
            response = random_num()
            assert (0<=int(response)<=10)
            logging.info('command is' "RAND")
        elif cmd == 'EXIT':
            response = 'Bye!'
            try:
                 client_socket.send(response.encode())
                 logging.info('commend is' "EXIT")
            finally:
                break

        else:
            response = 'Unknown command'

        client_socket.send(response.encode())

    client_socket.close()


def main():
    """
    Starts the TCP server, listens for incoming connections, and handles each client.
    Logs when the server is listening and when clients connect or disconnect.
    """
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((SERVER_IP, SERVER_PORT))
        server_socket.listen(3)
        print("Server is listening...")
        logging.info('Server is listening...')
    except:
        logging.info('Server is NOT listening...')

    while True:
            client_socket, client_addr = server_socket.accept()
            print("Client connected:", client_addr)
            handle_client(client_socket)
            print("Client disconnected")




if __name__ == '__main__':
    """
    Configures the logging settings and starts the main server loop.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=
        [
            logging.FileHandler('logg_of_server'),
            # logging.StreamHandler() only when there is a need to show the logs to the user
        ]
    )

    main()

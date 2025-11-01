""""

Author:Dvir Zilber

Program name:client.py

Description: A program that sende the server a command and recives back the desired data then prints it.

Date:11/1/25

"""


import socket
import logging

SERVER_IP = '127.0.0.1'
SERVER_PORT = 1712
MAX_PACKET = 1024

def main():
    """
    Connects to the server, sends user commands, receives responses, and handles communication.
    The user can enter commands: TIME, NAME, RAND, or EXIT.
    Logs events such as successful connection, command sending, and response reception.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        logging.info('Client connected successfully') #giving a logg message
        print('Connected to server at'+ SERVER_IP + str(SERVER_PORT))

        while True:
            cmd = input("Enter command (TIME, NAME, RAND, EXIT): ").upper()
            cmd = cmd.ljust(4)[:4]  #making sure its 4 bytes

            client_socket.send(cmd.encode())#sending the command to the server
            logging.info('Command sent to server successfully')

            response = client_socket.recv(MAX_PACKET)#getting a response from the server
            logging.info('Response received from server')
            print("Server response:", response.decode())


            if cmd == "EXIT":#if cmd == 'exit' then leave the while loop
                print("see ya later")
                break

    except Exception as e:
        print("Error:", e)
    finally:
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    """
    Initializes the logging configuration and runs the main client function.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=
        [
            logging.FileHandler('logg_of_client'),
            # logging.StreamHandler() only when there is a need to show the logs to the user
        ]
    )
    main()

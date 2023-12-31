import socket
import threading
import queue
import signal
import os

SERVER_NAME = "SERVER_SOCKET"
SERVER_NUMBER = 8
PORT = 12000

class TerminateException(Exception):
     pass

def handle_client(connection, q):
        receive_msg = connection.recv(1024).decode()
        print("Message received!")
        
        decoded = receive_msg.split(":")
        string_data = decoded[0]
        int_data = int(decoded[1])

        if int_data < 1 or int_data > 100:
            print(f"Client number out of range: {int_data}")
            connection.close()
            os.kill(os.getpid(), signal.SIGTERM)

        print(f"Client name: {string_data}")
        print(f"Server Name: {SERVER_NAME}")

        print(f"Client Number: {int_data}")
        print(f"Server Number: {SERVER_NUMBER}")
        print(f"Sum of Client and Server numbers: {int_data + SERVER_NUMBER}")

        send_msg = f"{SERVER_NAME}:{SERVER_NUMBER}"

        connection.send(send_msg.encode())
        print("Sending message to client!")

        connection.close()
        print("Connection has been closed!") 

def handle_terminate_signal(signum, frame):
    raise TerminateException()

def main():
    signal.signal(signal.SIGTERM, handle_terminate_signal)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(('', PORT))
    s.listen(1)
    print(f"Listening on port: {PORT}")

    try:
        while True:

            connection, addr = s.accept()
            print("Connection established!")
            
            print("Passing to new thread...")
            q = queue.Queue()
            threading.Thread(target=handle_client(connection, q)).start()

    except TerminateException:
        print("Terminating...")
    
    finally:
        s.close()
    

if __name__ == "__main__":
    main()
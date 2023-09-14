import socket
import threading
import queue

SERVER_NAME = "SERVER_SOCKET"
SERVER_NUMBER = 8
PORT = 12000

def handle_client(connection, q):
        receive_msg = connection.recv(1024).decode()
        print("Message received!")
        
        decoded = receive_msg.split(",")
        string_data = decoded[0]
        int_data = int(decoded[1])

        print(f"Client name: {string_data}")
        print(f"Server Name: {SERVER_NAME}")

        print(f"Client Number: {int_data}")
        print(f"Server Number: {SERVER_NUMBER}")
        print(f"Sum of Client and Server numbers: {int_data + SERVER_NUMBER}")

        send_msg = f"{SERVER_NAME},{SERVER_NUMBER}"

        connection.send(send_msg.encode())
        print("Sending message to client!")

        connection.close()
        print("Connection has been closed!")

        q.put(int_data) 

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(('', PORT))
    s.listen(1)
    print(f"Listening on port: {PORT}")

    while True:

        connection, addr = s.accept()
        print("Connection established!")
        
        print("Passing to new thread...")
        q = queue.Queue()
        threading.Thread(target=handle_client(connection, q)).start()

        int_data = q.get()


        if int_data < 1 or int_data > 100:
            break

if __name__ == "__main__":
    main()
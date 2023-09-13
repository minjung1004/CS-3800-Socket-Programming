import socket


def main():
    port = 12000
    name = "TESTSOCKET"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port))
    s.listen(1)
    print("server ready")
    while True:
        connection, addr = s.accept()

        msg = connection.recv(1024).decode()
        
        decoded = msg.split(",")
        string_data = decoded[0]
        int_data = int(decoded[1])
        print(string_data)
        print(int_data)
        print(type(string_data))
        print(type(int_data))
        msg = None


if __name__ == "__main__":
    main()
import socket

def main():
    name="TESTSOCKET"
    port = 12000

    #take input
    user_num = int(input("please input an integer between 1 and 100: "))

    #start socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), port))

    #define message
    send_message = f"this is a string,{user_num}"
    print(send_message)

    s.send(send_message.encode())
    msg = s.recv(1024)
    print(msg.decode("utf-8"))

    pass

if __name__ == "__main__":
    main()
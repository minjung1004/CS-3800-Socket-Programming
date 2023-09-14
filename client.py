import socket

def main():
    name="CLIENT_SOCKET"
    port = 12000

    #take input
    user_num = int(input("please input an integer between 1 and 100: "))

    #start socket
    print("socket starting")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), port))

    #send message
    print("sending message")
    send_message = f"{name}:{user_num}"
    s.send(send_message.encode())

    #receive message
    msg = s.recv(1024)
    print("message receied, decoding...")
    decoded = msg.decode().split(":")
    string_data = decoded[0]
    int_data = int(decoded[1])

    print("CLIENT NAME:", name)
    print("SERVER NAME:", string_data)

    print("CLIENT INT:", user_num)
    print("SERVER INT:", int_data)
    print("SUM OF VALS:", user_num + int_data)

    print("closing client")
    s.close()

if __name__ == "__main__":
    main()
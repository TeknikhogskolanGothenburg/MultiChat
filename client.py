import socket
import threading

HOST = '127.0.0.1'
PORT = 30125

running = True


def sender(client_socket):
    global running
    while running:
        message = input()
        if message.lower() == '!quit':
            running = False
        message_bytes = message.encode('utf-8')
        client_socket.sendall(message_bytes)


def receiver(client_socket):
    while running:
        message_in = client_socket.recv(1024).decode('utf-8')
        print(message_in)


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    name_question = client_socket.recv(1024).decode('utf-8')
    name = input(name_question)
    name_bytes = name.encode('utf-8')
    client_socket.sendall(name_bytes)

    sender_thread = threading.Thread(target=sender, args=(client_socket,))
    receiver_thread = threading.Thread(target=receiver, args=(client_socket,))

    sender_thread.start()
    receiver_thread.start()

    sender_thread.join()
    receiver_thread.join()

    client_socket.close()


if __name__ == '__main__':
    main()
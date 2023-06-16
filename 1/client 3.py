import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 1234))
q=int(s.recv(1024).decode())
for i in range(q):
    question = s.recv(1024).decode()
    print(question)
    answer = input("Enter your choice: ")
    s.send(answer.encode())


result = s.recv(1024).decode()
print(result)
s.close()
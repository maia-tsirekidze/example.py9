print(" TCP თუ UDP ")

q1 = input("გჭირდება თუ არა სანდო კავშირი, სადაც ყველა პაკეტი მივა? (კი/არა): ")
q2 = input("გირჩევნია თუ არა სისწრაფე სანდოობაზე მეტად? (კი/არა): ")
result = "არასწორი input"

if q1.lower() == "კი" and q2.lower() == "არა":
    result = "TCP"
elif q1.lower() == "არა" and q2.lower() == "კი":
    result = "UDP"
elif q1.lower() == "არა" and q2.lower() == "არა":
    result = "შეგიძლია გამოიყენო ორივე, TCP გირჩევდი"
elif q1.lower() == "კი" and q2.lower() == "კი":
    result = "TCP"

print(f"თქვენ აირჩიეთ: {result}")



if result == "TCP":

    print("SERVER (TCP):")
    print("""
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("TCP server listening...")
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        data = conn.recv(1024)
        print("Received:", data.decode())
        conn.sendall(b'Hello TCP client!')
    """)

    print("CLIENT (TCP):")
    print("""
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello TCP server!')
    data = s.recv(1024)
    print("Server replied:", data.decode())
    """)

elif result == "UDP":

    print("SERVER (UDP):")
    print("""
import socket

HOST = '127.0.0.1'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print("UDP server listening...")
    data, addr = s.recvfrom(1024)
    print("Received from", addr, ":", data.decode())
    s.sendto(b'Hello UDP client!', addr)
    """)

    print("CLIENT (UDP):")
    print("""
import socket

HOST = '127.0.0.1'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b'Hello UDP server!', (HOST, PORT))
    data, _ = s.recvfrom(1024)
    print("Server replied:", data.decode())
    """)

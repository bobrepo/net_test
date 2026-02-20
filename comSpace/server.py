import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
    sc.bind(("localhost", 8000))
    sc.listen()
    print("none connc")
    conc, addr = sc.accept()

    with conc:
        print("conncet")
        while True:
            msg = conc.recv(64)
            if not msg:
                break
            print(msg)

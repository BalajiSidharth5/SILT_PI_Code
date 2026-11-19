
def relay_control(sock, port):
    sock.setblocking(False)
    data = None
    while True: 
        try:
            data, (ip, lport) = sock.recvfrom(1024)
        except BlockingIOError:
            if data:
                port.write(data)
                return ip
            else:
                return None

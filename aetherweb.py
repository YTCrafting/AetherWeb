import socket

class Connection:
    def __init__(self, connection, address:str, port:int) -> None:
        self.connection = connection
        self.address = address
        self.port = port

    def wait_request(self) -> str:
        return self.connection.recv(1024).decode()

    def get_address(self):
        return self.address

    def get_port(self):
        return self.port

    def respond(self, content:str):
        responseBody = content
        responseLine = "HTTP/1.1 200 OK\r\n"
        responseHeaders = f"Content-Type: text/html\r\n"
        responseHeaders += f"Content-Length: {len(responseBody)}\r\n"
        responseHeaders += "Connection: close\r\n"
        response = (responseLine + responseHeaders + "\r\n" + responseBody).encode()
        self.connection.sendall(response)
        self.connection.close()
        return

class WebServer:
    def __init__(self) -> None:
        self.socket = None

    def start(self, address:str="0.0.0.0", port:int=80, maxcon=8) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((address, port))
        self.socket.listen(maxcon)
        return

    def wait_connection(self) -> Connection:
        connection, address = self.socket.accept()
        connection = Connection(connection, address[0], address[1])
        return connection

def unpack_request(request:str) -> dict:
    lines = request.split("\n")
    method, path, protocol = lines[0].split()
    headers = {}
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        if ": " in line:
            name, content = line.split(": ", 1)
            headers[name] = content
    return {"method": method, "path": path, "protocol": protocol, "headers": headers}

def extract_cookies(headers:list) -> dict:
    cookies = {}
    for header in headers:
        if header.startswith("Cookie: "):
            cookieHeader = header[len("Cookie: "):]
            pairs = cookieHeader.split("; ")
            for pair in pairs:
                key, value = pair.split("=")
                cookies[key] = value
    return cookies

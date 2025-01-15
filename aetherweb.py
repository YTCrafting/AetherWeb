import socket

class WebServer:
    def __init__(self) -> None:
        self.socket = None

    def start(self, address:str="0.0.0.0", port:int=80, maxcon=8) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((address, port))
        self.socket.listen(maxcon)
        return

    def wait_connection(self):
        connection, address = self.socket.accept()
        return connection, address

    def wait_request(self, connection) -> str:
        return connection.recv(1024).decode()

    def unpack_request(self, request:str) -> dict:
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

    def extract_cookies(self, headers:list):
        cookies = {}
        for header in headers:
            if header.startswith("Cookie: "):
                cookieHeader = header[len("Cookie: "):]
                pairs = cookieHeader.split("; ")
                for pair in pairs:
                    key, value = pair.split("=")
                    cookies[key] = value
        return cookies

    def respond(self, connection, content:str):
        responseBody = content
        responseLine = "HTTP/1.1 200 OK\r\n"
        responseHeaders = f"Content-Type: text/html\r\n"
        responseHeaders += f"Content-Length: {len(responseBody)}\r\n"
        responseHeaders += "Connection: close\r\n"
        response = (responseLine + responseHeaders + "\r\n" + responseBody).encode()
        connection.sendall(response)
        connection.close()
        return

import socket

STATUSCODE_NAMES = {
    102: "Processing",
    200: "Ok",
    203: "Non-Authorative Information",
    204: "No Content",
    206: "Partial Content",
    301: "Moved Permanently",
    302: "Found",
    307: "Temporary Redirection",
    308: "Permanent Redirection",
    400: "Bad Request",
    402: "Unauthorized",
    404: "Not Found",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    408: "Request Timeout",
    410: "Gone",
    413: "Payload Too Large",
    414: "Request URI Too Large",
    423: "Locked",
    429: "Too Many Requests",
    500: "Internal Server Error",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
    522: "Connection Timed Out",
    525: "SSL Handshake Failed"
}

STATUSCODE_IMAGES = {
    102: "https://pa1.narvii.com/6377/8fd54f5a87043cc3f9192d0d05e579506b2e4223_hq.gif",
    200: "https://i.pinimg.com/originals/4d/f5/f3/4df5f321255c7ebef4dc574bdf3018b0.jpg",
    203: "http://pm1.narvii.com/6291/40c2d61f7440a1dbb21d45f36571ceedf0899edf_00.jpg",
    204: "https://i.pinimg.com/originals/9f/13/e3/9f13e3e67e7382a2c9f8db02180d2b61.jpg",
    206: "https://c.tenor.com/pHht4Q82LscAAAAC/cake-food.gif",
    301: "https://allanimemag.files.wordpress.com/2020/12/heavens-lost-property-packing-boxes-screenshot-1.png",
    302: "https://i.kym-cdn.com/photos/images/newsfeed/000/730/678/bee.gif",
    307: "https://media3.giphy.com/media/XaAUgxOriqslHO69U2/giphy.gif",
    308: "https://media3.giphy.com/media/XaAUgxOriqslHO69U2/giphy.gif",
    400: "https://c.tenor.com/brI34ue84U0AAAAC/anime-smug-smug.gif",
    402: "https://pbs.twimg.com/media/EoGryrMXEAAC74v.jpg",
    404: "https://c.tenor.com/1RyM7ikzraIAAAAM/anime-what.gif",
    405: "https://i.gifer.com/8KWv.gif",
    406: "https://c.tenor.com/lPVf0QcafhEAAAAC/stop-right-there-buster-nope.gif",
    408: "https://64.media.tumblr.com/39d0f2988bf37dbcbe15e3296cd899b6/d305745d447129dc-5b/s1280x1920/2c5c923836ee66c526a1e9e8c7501cdaf2448657.gif", 410: "https://media.tenor.com/1PdUCJWK6LUAAAAC/anime-disappear.gif",
    413: "https://cdn.shopify.com/s/files/1/0318/2649/files/tenor_ef8ea3ac-40cd-42b8-9afd-5ea82e47d745_large.gif?v=1563938313", 414: "https://64.media.tumblr.com/175ac9a42e8122b3d113cb6b175c35a5/tumblr_o47ouv5DoS1s0ifhgo1_500.gif",
    423: "https://c.tenor.com/NbBCakbfZnkAAAAC/die-kill.gif",
    429: "https://i.kym-cdn.com/photos/images/original/001/291/790/051.gif",
    500: "https://c.tenor.com/YhvPxE804eEAAAAC/anime-de-panico.gif",
    502: "https://c.tenor.com/9Ql_VyYvMZkAAAAC/anime-sleeping.gif",
    503: "https://i0.wp.com/www.live-evil.org/wp-content/uploads/2022/06/sleepy.gif",
    504: "https://c.tenor.com/ULY2-MRkG7IAAAAC/load-loading-gif.gif",
    522: "https://c.tenor.com/MYFSAXUCXt4AAAAC/kronii-loading.gif",
    525: "https://c.tenor.com/4yWFhsgqzfEAAAAC/anime-handshake.gif"
}

class StatusCodes:
    def __init__(self) -> None:
        self.statuscodes = {}

    def set_statuscode(self, statuscode:int, content:str) -> None:
        self.statuscodes[statuscode] = content

    def get_statuscode(self, statuscode:int) -> None:
        if statuscode in self.statuscodes:
            content = self.statuscodes[statuscode]
        else:
            content = (
                f'<!DOCTYPE html>\n'
                f'<html lang="en">\n'
                f'<head>\n'
                f'    <meta charset="UTF-8">\n'
                f'    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n'
                f'    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
                f'    <title>{statuscode} {STATUSCODE_NAMES[statuscode]}</title>\n'
                f'    <style>\n'
                f'        body {{\n'
                f'            background: #222222;\n'
                f'            display: flex;\n'
                f'            justify-content: center;\n'
                f'            align-items: center;\n'
                f'            flex-direction: column;\n'
                f'            font-family: \'Trebuchet MS\', sans-serif;\n'
                f'            padding: 10% 10% 10% 10%;\n'
                f'        }}\n'
                f'        #image {{\n'
                f'            width: inherit;\n'
                f'            border: 3px solid white;\n'
                f'        }}\n'
                f'        .box {{\n'
                f'            width: 240px;\n'
                f'            float: left;\n'
                f'            margin: 3px;\n'
                f'            padding: 3px;\n'
                f'        }}\n'
                f'        h2, h1 {{\n'
                f'            font-weight: bolder;\n'
                f'            color: white;\n'
                f'            margin-block-start: 0.12em;\n'
                f'            margin-block-end: 0em;\n'
                f'        }}\n'
                f'    </style>\n'
                f'</head>\n'
                f'<body>\n'
                f'    <div class="box">\n'
                f'        <img id="image" src="{STATUSCODE_IMAGES[statuscode]}" alt="">\n'
                f'    </div>\n'
                f'    <h1>{statuscode}</h1>\n'
                f'    <h2>{STATUSCODE_NAMES[statuscode]}</h2>\n'
                f'</body>\n'
                f'</html>'
            )
        return content

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

    def respond(self, content:str, statuscode:int=200):
        responseBody = content
        responseLine = f"HTTP/1.1 {statuscode} {STATUSCODE_NAMES[statuscode]}\r\n"
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

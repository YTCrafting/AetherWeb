from aetherweb import WebServer

server = WebServer()
server.start()

while True:
    connection, address = server.wait_connection()
    raw_request = server.wait_request(connection)
    request = server.unpack_request(raw_request)

    if request["method"] == "GET":
        if request["path"] == "/":
            server.respond(connection, f"Hello, {address[0]}!")

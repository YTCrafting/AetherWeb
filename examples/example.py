import aetherweb

server = aetherweb.WebServer()
server.start()

while True:
    connection = server.wait_connection()
    raw_request = connection.wait_request()
    request = aetherweb.unpack_request(raw_request)

    if request["method"] == "GET":
        if request["path"] == "/":
            connection.respond(f"Hello, {connection.get_address()}!")

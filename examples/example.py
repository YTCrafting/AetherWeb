import aetherweb

server = aetherweb.WebServer()
scodes = aetherweb.StatusCodes()
server.start()

while True:
    connection = server.wait_connection()
    request = connection.wait_request()
    request = aetherweb.unpack_request(request)

    if request["method"] == "GET":
        if request["path"] == "/":
            connection.respond(f"Hello, {connection.get_address()}!")
        else:
            connection.respond(scodes.get_statuscode(404), 404)
    else:
        connection.respond(scodes.get_statuscode(405), 405)

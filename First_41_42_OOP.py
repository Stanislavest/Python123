# ========================================== 22.02.2022
# ================================================= MVC
# Model - модель
# Viev - вид или представление
# Controller - контроллер

# ========================================== 24.02.2022
# Как создаются Сокеты
# Сетевые протоколы OSI | TCP/IP
#
import socket

URLS = {
    '/': 'index page',
    '/blog': 'blog page',

}


def parse_request(request):
    parsed = request.split(" ")
    method = parsed[0]
    url = parsed[1]
    return method, url


def generate_headers(method, url):
    if method != 'GET':
        return 'HTTP/1.1 405 Method Not Allowed!\n\n', 405
    if url not in URLS:
        return 'HTTP/1.1 404 Method Not Found!\n\n', 404
    return "HTTP/1.1 200 OK!", 200


def generate_response(request):
    method, url = parse_request(request)
    headers, code = generate_headers(method, url)
    body = URLS[url]
    return (headers + body).encode()


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5000))
    server_socket.listen()  # 127.0.0.1:5000

    while True:
        client_socket, address = server_socket.accept()  # возвр. кортеж из сокета и ...
        request = client_socket.recv(1024)  # читает и возвр. в 2ом формате
        print(f'Клиент: {address} => \n{request.decode("utf-8")}\n')

        response = generate_response(request.decode())
        client_socket.sendall(response)
        client_socket.close()


if __name__ == "__main__":
    run()

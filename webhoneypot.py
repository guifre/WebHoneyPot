import logging
import socket

LOG_PATH = '/var/log/webhoneypot.log'
PORT = 80

class Server:
    def __init__(self, logger, port):
        self.logger = logger
        self.port = port
        self.request_max_size = 2048

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', self.port))
        sock.listen(1)
        while True:
            csock, caddr = sock.accept()
            req = csock.recv(self.request_max_size)
            self.logger.info("Client[%s] request: %s\n" % (`caddr`, req))
            csock.sendall("<html><body><h2>Welcome to router admin page</h2>")
            if '/login' in req:
                csock.sendall('<p>Invalid Password!</p>')
            csock.sendall("<p>Please, log in</p><form action='/login' method='get'>username: <input name='username' value=''/><br />password: <input name='password' type='password' value=''/><br /><input type='submit'/></form></body></html>")
            csock.close()


class Logger:
    def __init__(self):
        logging.basicConfig(filename=LOG_PATH, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', datefmt='%m-%d %H:%M')

    def info(self, message):
        logging.info(message)


Server(Logger(), PORT).run()

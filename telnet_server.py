from constants import LOGIN_RESPONSE, DEFAULT_RESPONSE, XMLRPC_RESPONSE, CALENDAR_RESPONSE, HNAP1_RESPONSE
import socket


class TelnetServer:
    def __init__(self, logger, port):
        self.stopped = False
        self.request_max_size = 1234
        self.port = port
        self.logger = logger

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', self.port))
        sock.listen(1)
        sock.settimeout(2)
        while not self.stopped:
            try:
                csock, caddr = sock.accept()
                try:
                    req = csock.recv(self.request_max_size)
                    self.logger.info("Client[%s] request: %s\n" % (`caddr`, req))
                    first_header = req.splitlines()[0]
                    if '/login' in first_header:
                        csock.sendall(LOGIN_RESPONSE)
                    elif '/HNAP1' in first_header:
                        csock.sendall(HNAP1_RESPONSE)
                    elif 'calendar/install/index.php' in first_header:
                        csock.sendall(CALENDAR_RESPONSE)
                    elif 'xmlrpc.php' in first_header:
                        csock.sendall(XMLRPC_RESPONSE)
                    elif '/' in first_header:
                        csock.sendall(DEFAULT_RESPONSE)
                finally:
                    if csock:
                        csock.close()
            except socket.timeout:
                pass
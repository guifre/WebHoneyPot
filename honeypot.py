import logging
import threading

from telnet_server import TelnetServer
from web_server import WebServer

LOG_PATH = '/tmp/webhoneypot.log'
WEB_PORT = 80
TELNET_PORT = 23


class Server:
    def __init__(self, logger, web_port, telnet_port):
        self.logger = logger
        self.request_max_size = 2048
        self.stopped = False
        self.web_port = web_port
        self.telnet_port = telnet_port

        self.web_server = WebServer(self.logger, self.web_port)
        self.telnet_server = TelnetServer(self.logger, self.telnet_port)

    def stop(self):
        self.web_server.stopped = True
        self.telnet_server.stopped = True

    def run(self):
        threading.Thread(target=self.web_server.run).start()
        threading.Thread(target=self.telnet_server.run).start()


class Logger:
    def __init__(self):
        logging.basicConfig(filename=LOG_PATH, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', datefmt='%m-%d %H:%M')

    def info(self, message):
        logging.info(message)


if __name__ == "__main__":
    Server(Logger(), WEB_PORT, TELNET_PORT).run()

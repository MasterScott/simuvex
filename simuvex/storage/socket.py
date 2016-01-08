from ..storage.file import SimFile
from ..plugins.plugin import SimStatePlugin

class SimSocket(SimStatePlugin):
    def __init__(self, fd, send_fd, recv_fd):
        super(SimSocket, self).__init__()
        self.fd = fd
        self.send = send_fd
        self.recv = recv_fd

    @property
    def fd(self):
        return self.fd

    @property
    def recv(self):
        return self.recv

    @property
    def send(self):
        return self.send

    def __str__(self):
        return '<{} fd {} recv {} send {}>'.format(self.__class__.__name__,
                                                   self.fd,
                                                   self.recv,
                                                   self.send)

from ..storage.file import SimFile
from ..plugins.plugin import SimStatePlugin

class SimSocket():
    def __init__(self, new_fd, new_send_fd, new_recv_fd):
        self.fd = new_fd
        self.send_fd = new_send_fd
        self.recv_fd = new_recv_fd

    @property
    def fd(self):
        return self.fd

    @property
    def recv_fd(self):
        return self.recv_fd

    @property
    def send_fd(self):
        return self.send_fd

    def __str__(self):
        return '<{} fd {} recv {} send {}>'.format(self.__class__.__name__,
                                                   self.fd,
                                                   self.recv_fd,
                                                   self.send_fd)

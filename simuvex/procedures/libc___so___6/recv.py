import simuvex
import logging

logging.getLogger('simuvex.plugins.posix.sockets')

######################################
# recv
######################################

class recv(simuvex.SimProcedure):
    #pylint:disable=arguments-differ

    def run(self, fd, dst, length):
        fd = int(self.state.se.any_int(fd))
        recv_fd = self.state.posix.sockets[fd].recv_fd
        bytes_recvd = self.state.posix.read(recv_fd, dst, self.state.se.any_int(length))

        return bytes_recvd

import simuvex
import logging

l = logging.getLogger('simuvex.plugins.posix.sockets')

######################################
# send
######################################

class send(simuvex.SimProcedure):
    #pylint:disable=arguments-differ

    def run(self, fd, src, length):
        fd = int(self.state.se.any_int(fd))
        send_fd = self.state.posix.sockets[fd].send_fd
        data = self.state.memory.load(src, length)
        length = self.state.posix.write(send_fd, data, length)
        return length


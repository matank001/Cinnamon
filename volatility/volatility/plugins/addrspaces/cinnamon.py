import socket
import volatility.addrspace as addrspace

MAX_READ = 2048

class Cinnamon(addrspace.BaseAddressSpace):

    def __init__(self, base, config, layered = False, **kwargs):
        addrspace.BaseAddressSpace.__init__(self, base, config, **kwargs)
        self.as_assert(base == None or layered, 'Must be first Address Space')
        self.as_assert("::" in config.LOCATION, 'Location is not of cinnamon format IP::PORT')

        IP, PORT = config.LOCATION.split("::")
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((IP, int(PORT)))

        self.socket.send("hola")
        self.swapper = int(self.socket.recv(MAX_READ))

    def is_valid_address(self, addr):
        return (0x1000 <= addr <= 0x9ffff) or (0x200000 <= addr <= 0xf7ffffff) or (0x100000000 <= addr <= 0x330ffffff)

    def read(self, addr, length):

        if not self.is_valid_address(addr):
            return None

        data = ""
        while length > 0:
            current_read_length = min(MAX_READ, length)
            self.socket.send("v" + str(addr) + "v" + str(current_read_length))
            current_data = self.socket.recv(current_read_length)
            data += current_data
            length -= current_read_length

        return data

    def zread(self, addr, length):
        data = self.read(addr, length)
        if data is None:
            data = "\x00" * length
        elif len(data) != length:
            data += "\x00" * (length - len(data))
        return data

    def close(self):
        self.socket.close()
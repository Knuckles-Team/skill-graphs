# disabled promiscuous mode
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

```

The next example shows how to use the socket interface to communicate to a CAN network using the raw socket protocol. To use CAN with the broadcast manager protocol instead, open a socket with:
Copy```
socket.socket(socket.AF_CAN, socket.SOCK_DGRAM, socket.CAN_BCM)

```

After binding (`CAN_RAW`) or connecting ([`CAN_BCM`](https://docs.python.org/3/library/socket.html#socket.CAN_BCM "socket.CAN_BCM")) the socket, you can use the [`socket.send()`](https://docs.python.org/3/library/socket.html#socket.socket.send "socket.socket.send") and [`socket.recv()`](https://docs.python.org/3/library/socket.html#socket.socket.recv "socket.socket.recv") operations (and their counterparts) on the socket object as usual.
This last example might require special privileges:
Copy```
import socket
import struct

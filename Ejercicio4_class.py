
import socket as s

class ServidorTCP:
    ip = ''
    port = ''
    salir = False


    def __init__(self,ip =  '127.0.0.1', port = 35491):
        self.servidorSocket = s.socket()
        self.servidorSocket.bind((ip, port))
        self.servidorSocket.listen()
        print('Esperando conexion')
        while not self.salir:
            (self.clienteCon, self.clienteAddr) = self.servidorSocket.accept()
            print('Conexion Realizada')

            while True:
                self.recibido = self.servRecibir()

                if self.recibido == b'exit':
                    print('conexion cerrada')
                    self.clienteCon.close()
                    break
                elif self.recibido == b'exit all':
                    print('conexion cerrada')
                    self.clienteCon.close()
                    self.salir = True
                    break
                elif self.recibido != b'':
                    self.servEscribir("Recibido en Servidor")

    def servEscribir(self, mensaje):
        self.clienteCon.send(mensaje.encode())

    def servRecibir(self):
        self.data = self.clienteCon.recv(1024)
        print(f'El mensaje recibido desde el cliente fue : {self.data}')
        return self.data



class ClienteTCP:

    def __init__(self,ip =  '127.0.0.1', port = 35491):
        self.cliente = s.socket()
        self.cliente.connect((ip, port))


    def clntEscribir(self, mensaje):
        bytess = mensaje.encode()
        self.cliente.send(bytess)

    def clntRecibir(self):
        self.data = self.cliente.recv(1024)
        print(self.data)

        if self.data == b'':
            print('Conexion se termino')
            self.cliente.close()



class ServidorUDP:

    ip = ""
    port = ""

    def __init__(self, ip = '127.0.0.1', port = 12345):
        self.socketServidor = s.socket(s.AF_INET, s.SOCK_DGRAM)
        self.socketServidor.bind((ip,port))
        self.salir = False

        while not self.salir:
            print('esperando paquetes')

            self.data, self.addr = self.servRecibir()

            if self.data == b'exit':

                self.salir = True;
                self.servEscribir('exit', self.addr)
                print('conexion cerrada')
                self.socketServidor.close()
            else:

                self.servEscribir('mensaje recibido en servidor', self.addr)



    def servEscribir(self, mensaje, addr):
        self.socketServidor.sendto(mensaje.encode(), addr)

    def servRecibir(self):
        data, addr = self.socketServidor.recvfrom(1024)
        print(f'recibi un mensaje: {data} de {addr}')
        return data, addr

class ClienteUDP:

    def __init__(self, ip='127.0.0.1', port=12345):
        self.cliente = s.socket(s.AF_INET, s.SOCK_DGRAM)
        self.addr = ip, port

    def clntEscribir(self, mensaje, addr):
        self.cliente.sendto(mensaje.encode(), addr)


    def clntRecibir(self):
        data, addr = self.cliente.recvfrom((1024))
        print(f'recibido {data} desde {addr}')
        if data == b'exit':
            print('Conexion se termino')
            self.cliente.close()

        return data, addr

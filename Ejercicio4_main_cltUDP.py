import Ejercicio4_class

cliente = Ejercicio4_class.ClienteUDP()
cliente.clntEscribir("primer mensaje", cliente.addr)
cliente.clntRecibir()
cliente.clntEscribir("segundo mensaje", cliente.addr)
cliente.clntRecibir()
cliente.clntEscribir("Tercer mensaje", cliente.addr)
cliente.clntRecibir()
cliente.clntEscribir('exit', cliente.addr)
cliente.clntRecibir()



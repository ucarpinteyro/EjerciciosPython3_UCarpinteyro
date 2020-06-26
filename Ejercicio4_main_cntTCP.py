import Ejercicio4_class

cliente = Ejercicio4_class.ClienteTCP()
cliente.clntEscribir("primer mensaje")
cliente.clntRecibir()
cliente.clntEscribir("segundo mensaje")
cliente.clntRecibir()
cliente.clntEscribir("Tercer mensaje")
cliente.clntRecibir()
cliente.clntEscribir('exit')
cliente.clntRecibir()

cliente2 = Ejercicio4_class.ClienteTCP()
cliente2.clntEscribir("primer mensaje22")
cliente2.clntRecibir()
cliente2.clntEscribir("segundo mensaje22")
cliente2.clntRecibir()
cliente2.clntEscribir('exit all')
cliente2.clntRecibir()

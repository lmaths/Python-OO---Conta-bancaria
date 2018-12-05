from cliente import Cliente
from conta import Conta

cliente1 = Cliente('Guilherme', '135.755.47.10', 21)


conta_do_guilherme = Conta(cliente1, 50)

print(conta_do_guilherme.consulta_saldo())

conta_do_guilherme.depositar(1000)

print(conta_do_guilherme.saldo)

conta_do_guilherme.sacar(50)
conta_do_guilherme.depositar(1000)
conta_do_guilherme.depositar(200)
conta_do_guilherme.sacar(500)
conta_do_guilherme.depositar(300)
conta_do_guilherme.sacar(200)


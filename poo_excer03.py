"""### 🏦 **Exercício 3 – Classe `ContaBancaria`**

Crie uma classe `ContaBancaria` com:

- Atributos: `titular`, `saldo`
    
- Métodos:
    
    - `depositar(valor)`
        
    - `sacar(valor)` (verifique se há saldo suficiente)
        
    - `exibir_saldo()`
        
- Crie uma conta e simule alguns depósitos e saques."""

class ContaBancaria:
    def __init__(self, titular, saldo, contasConfiaveis = None):
        self.titular = titular
        self.saldo = saldo
        if contasConfiaveis is None:
            contasConfiaveis = []
        self.contasConfiaveis = contasConfiaveis

    def exibir_infos(self):
        print(f'Nome do titular: {self.titular}\nSaldo: R${self.saldo}\nContas de confiana: {self.contasConfiaveis}')

    def depositar(self, valor):
        valor = int(input("Qual valor deseja depositar na conta? "))
        self.saldo += valor
        print(f"Agora você tem {self.saldo}")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Parece que você tá pobrinho, não tem esse dinheiro não amigão kkkkk")
        else:
            self.saldo -= valor
            print(f"Olha só, parece que você tem o saldo, você sacou R${valor} e agora você tem R${self.saldo} sobrando")

    def definirContasConfiaveis(self):
        qtdContasAmigo = int(input("Qual a quantidade de contas amigos deseja adicionar?"))
        for i in range(qtdContasAmigo):
            contaAmigo = input("Qual nome do titula da conta que quer adicionar?")
            if contaAmigo not in self.contasConfiaveis:
                self.contasConfiaveis.append(contaAmigo.upper())
            else:
                print("Essa conta já está na lista")

        print(self.contasConfiaveis)

    def transferir(self):
        valor = int(input("Qual valor da transferência deseja realizar?\n" ))
        if valor > self.saldo:
            print("Tá querendo transferir dinheiro que tu não não é???\n")
        else:
            contaPraSerTransferida = input(f"Quantia aceita. Para quem deseja enviar?\nContas de confianca: {self.contasConfiaveis}")
            saldoFinal = self.saldo - valor
            ## agora aqui eu preciso verificar se a pessoa pra quem o usuário quer enviar existe na lista de contas confiáveis.
            for i in range(len(self.contasConfiaveis)):
                if (self.contasConfiaveis[i] == contaPraSerTransferida.upper()):
                    print(f"Nome {contaPraSerTransferida.upper()} encontrado na posição {i}\n")
                    print(f"{contaPraSerTransferida.upper()} agora tem R${valor}\n")
                    print(f"{self.titular} tem agora agora R${saldoFinal}\n")


conta_01 = ContaBancaria("Melina da Silva", 100)

conta_01.exibir_infos()

conta_01.definirContasConfiaveis()

conta_01.transferir()

conta_01.exibir_infos()
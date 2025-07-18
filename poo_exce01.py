class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def exibir_dados(self):
        print(f"Meu nome é {self.nome} tenho {self.idade} anos e este é meu email para contato: {self.email}")
        
    def maior_idade(self):
        if self.idade >= 18:
            print(f"parabéns, você agora pode dirigir (e ser preso também)")
        else:
            print(f"menor de idade kkkkk limpa bunda com ajuda ainda né?")

pessoa01 = Pessoa("John Columbine", 16, 'jhoncolumbine.louco@gmail.com')
pessoa01.exibir_dados()
pessoa01.maior_idade()

pessoa02 = Pessoa("Maria Policial", 32, 'mariazinha.poucabala@gmail.com')
pessoa02.exibir_dados()
pessoa02.maior_idade()

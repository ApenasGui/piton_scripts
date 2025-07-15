class Arma:
    def __init__(self, nome, trava, tambor, municao):
        self.nome = nome # nome do trabuco
        self.trava = trava # travado
        self.tambor = tambor # sem bala no tambor
        self.municao = municao # municao no cartucho

    def exibir_infos(self):
        print(self.nome, self.trava, self.tambor, self.municao)

    def recarregar(self):
        print(self.nome + " foi recarregada")
        self.municao = 10

    def engatilhar(self):
        if self.tambor == False:
            print("Arma engatilhada")
            self.municao -= 1
            self.tambor = True
            
        else:
            print("Arma já tem munição no tambor")
        
    def atirar(self):
        if self.trava == True:
            print("Arma está com a trava ativada")

        if self.trava == False:
            if self.municao <= 0 or self.tambor == False:
                print("Não tem bala")

            else:
                print("Tiro dado")
                self.tambor = False
                self.municao = self.municao - 1
                self.tambor = True

                if self.municao <= 0:
                    print("Não tem mais munição no cartucho")





pistola_1911 = Arma("1911",False, False, 10);
pistola_1911.exibir_infos()
pistola_1911.atirar()
pistola_1911.recarregar()
pistola_1911.atirar()
pistola_1911.engatilhar()
pistola_1911.atirar()
pistola_1911.atirar()
pistola_1911.exibir_infos()
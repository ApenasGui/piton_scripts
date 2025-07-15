"""Exercício 5 – Composição e Menu Interativo (Avançado)
Objetivo: Aplicar composição e interação com o usuário.

Descrição:
Crie duas classes: Livro e Biblioteca.

A classe Livro deve ter: título, autor e ano.

A classe Biblioteca deve conter uma lista de livros e métodos para:

adicionar_livro()

remover_livro()

listar_livros()

Implemente um menu no terminal para o usuário interagir com a biblioteca."""


class Biblioteca:
    def __init__(self, livro):
        self.livro = []

    def adicionar_livro(self, livro):
        self.livro.append(livro) 
    def remover_livro(self, livro):
        if livro not in self.livro:
            print("Livro não encontrado")

        else:
            self.livro.remove(livro)
    def listar_livro(self):
        if not self.livro:
            print("Não há nenhum livro na biblioteca")
        else:
            print(self.livro)

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
          return f"{self.titulo (self.autor) - self.ano}"
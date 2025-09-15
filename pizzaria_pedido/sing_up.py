from argon2 import PasswordHasher
from validation import validar_email

"""
aqui eu vou tentar fazer um sistema de cadastro simples, vamos ver se eu consigo
fazer sem que seja necessário muita pesquisa por fora

"""
passHash = PasswordHasher()

class User:
    def __init__(self, firstName, lastName, userCpf, userEmail, userPassword):
        self.firstName = firstName
        self.lastName = lastName
        self.userCpf = userCpf
        self.userEmail = userEmail
        self.userPassword = userPassword

    def create_user():
        firstName = input('Digite seu primeiro nome:\n')
        lastName = input('Digite seu sobrenome:\n')
        userCpf = input('Digite seu CPF (somente os números):\n')
        userEmail = input('Digite seu email:\n')
        validar_email(userEmail)
        # aqui a gente vai criar um loop pra testar o email até ele ser True, então traduzindo a função seria assim>
        # enquanto não for válido a variável validar_email(), vamos fazer a condição abaixo
        # não precisa nem colocar o break
        while not validar_email(userEmail):
            print('Email inválido, tente novamente')
            userEmail = input('Digite seu email:\n')
            testando_email = validar_email(userEmail)
        print('Email válido')

        userPassword = input('Digite sua senha: no mínimo 6 digitos, 1 número e uma letra maiúscula:\n')

        return firstName, lastName, userCpf, userEmail, userPassword
    
def hashPw(password):
    return passHash.hash(password)

clientes = []

first_access = input('Você já é cliente nosso? Caso não seja, eu te ajudarei no cadastro: \n')
if first_access == 'sim':
    print(f'Olá, bem vindo de volta, você será redirecionado para escolher sua pizza')
elif first_access == 'não':
    user_id01 = User.create_user()
    clientes.append(user_id01)

print(clientes)
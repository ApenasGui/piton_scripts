print('------------------- Porta Mac ----------------------')

userMac = input('Insira aqui seu MAC Address: \n')

porta_mac01 = '0A:1B:2C:3D:4E:5F'
porta_mac02 = '1A:2B:3C:4D:5E:6F'
porta_mac03 = '2A:3B:4C:5D:6E:7F'
porta_mac04 = '4A:3B:4C:5D:6E:7F'

if userMac == porta_mac01:
    print(f'Seu MAC Adress {userMac} está na porta 1')
elif userMac == porta_mac02:
    print(f'Seu MAC Adress de número {userMac} está na porta 2')
elif userMac == porta_mac03:
    print(f'Seu MAC está na porta 3')
elif userMac == porta_mac04:
    print(f'Seu Mac está na porta 4')
else:
    print('MAC informado não encontrado. Por favor, tente novamente.')
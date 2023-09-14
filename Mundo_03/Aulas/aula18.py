'''
dado = list()
dado.append('Matheus')
dado.append(20)
galera = []
galera.append(dado[:])
dado[0] = 'Maria'
dado[1] = 22
galera.append(dado[:])
print(galera)
'''

galera = [['João', 19], ['Ana', 33], ['Paula', 14], ['Lucas', 29]]
print(galera)
print(galera[2])
print(galera[2][1])

print('\33[1:35mCom FOR')
for pessoa in galera:
    #print(pessoa)
    #print(pessoa[0])
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')

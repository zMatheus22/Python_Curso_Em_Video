# Faça um programa que leia uma frase pelo teclado e mostre:
# -> Quantas vezes aparece a letra "A".
# -> Em que posição ela a primeira vez.
# -> Em que posição ela aparece a última vez.

print('===== Desafio 026 =====')
frase = str(input("Digite uma frase: ")).strip()
frase = frase.upper()
letra = "A"
quantidade = frase.count(letra)
primeira = frase.find(letra)
ultimo = frase.rfind(letra)

print('Quantidade da letra "{}" frase é de {}'.format(letra, quantidade))
print('Primeira possição da letra "{}" é na possição {}'.format(letra, primeira + 1))
print('Última possição da letra "{}" é na  possição {}'.format(letra, ultimo + 1))

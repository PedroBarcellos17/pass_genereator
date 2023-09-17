import string
import random

caracteres = string.ascii_letters + string.digits + string.punctuation
while True:
    try:
        tamanho = int(input('Insira o tamanho da senha:'))
        break
    except ValueError:
        print('Entrada inválida. Por favor, insira um número inteiro.')
senha = ''.join(random.choice(caracteres) for i in range(tamanho))
print(f'Sua senha é essa: {senha}')
repetir = str(
    input('Se deseja criar uma nova senha aperte[S], se não quiser aperte outra tecla:')).upper()[0]

while repetir in 'S':
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    print(f'Sua senha é essa: {senha}')
    repetir = str(
        input('Se deseja criar uma nova senha aperte[S]:')).upper()[0]

if repetir != 'S':
    print('Acabou, obrigado por usar esse gerador de senhas!!')

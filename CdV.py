def soma_modular(caracter, chave):
    if 'A' <= caracter <= 'Z':
        indice = ord(caracter) - ord('A')
        cifra = (indice + ord(chave) - ord('A')) % 26
        return chr(cifra + ord('A'))
    
    elif 'a' <= caracter <= 'z':
        indice = ord(caracter) - ord('a')
        cifra = (indice + ord(chave) - ord('a')) % 26
        return chr(cifra + ord('a'))
    
    else:
        return caracter

def subtracao_modular(caracter, chave):
    if 'A' <= caracter <= 'Z':
        indice = ord(caracter) - ord('A')
        cifra = (indice - (ord(chave) - ord('A'))) % 26
        return chr(cifra + ord('A'))
    
    elif 'a' <= caracter <= 'z':
        indice = ord(caracter) - ord('a')
        cifra = (indice - (ord(chave) - ord('a'))) % 26
        return chr(cifra + ord('a'))
    
    else:
        return caracter

print('-_-_- Cifra de Vegenere -_-_-')

print('(1) Criptografar\n(2) Descriptografar\n->', end='')
cripto = input()

print('Texto: ', end='')
texto = input()

print('Chave: ', end='')
chave = input()

lista_texto = list(texto)
lista_chave = list(chave)

match cripto:
    case '1':
        for i in range (len(lista_texto)):
            lista_texto[i] = soma_modular(lista_texto[i], lista_chave[i])
    case '2':
        for i in range (len(lista_texto)):
            lista_texto[i] = subtracao_modular(lista_texto[i], lista_chave[i])

texto = ''.join(lista_texto)
print('Cifra:', texto)
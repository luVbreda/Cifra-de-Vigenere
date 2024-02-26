# função que soma os caracteres sem ultrapssar o alfabeto
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

# função que subtrai os caracteres sem retrogradar o alfabeto
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

# pequena visualização gráfica para o usuário
print('-_-_-_-  Cifra de Vigenere (Python)  -_-_-_-')
print('" Lembre-se de utilizar o texto inteiramente')
print('   em letras maiusculas ou minúsculas. ')
print('   Esta regra também vale para a chave "')

cripto = '' # iniciando a variavel com nada, só para ser usada mais tarde
print('(1) Criptografar\n(2) Descriptografar')
while (cripto !='1'and cripto !='2'): # ciclo com while para repetir a captação da variável caso o user não digite '1' ou '2'
    print('->', end='')
    cripto = input()

print('Texto: ', end='')
texto = input()

print('Chave: ', end='')
chave = input()

# corrigindo o tamanho da chave caso seja menor que o texto a ser criptografado/descriptografado (caso seja maior não há problema)
if len(chave) < len(texto):
    chave = chave * (len(texto) // len(chave)) + chave[:len(texto)%len(chave)]

# criando uma lista com as strings para trabalhar individualmente cada char
lista_texto = list(texto)
lista_chave = list(chave)

# fazendoa  operação a partir da opção escolhida
match cripto:
    case '1':
        for i in range (len(lista_texto)):
            lista_texto[i] = soma_modular(lista_texto[i], lista_chave[i])
    case '2':
        for i in range (len(lista_texto)):
            lista_texto[i] = subtracao_modular(lista_texto[i], lista_chave[i])

# juntando a lista do texto para melhor visualização na impressão
texto = ''.join(lista_texto)
print('Cifra:', texto)
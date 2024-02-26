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
    
# EXPLICANDO O FUNCIONAMENTO DAS FUNÇÕES:
#   A função usa um caracter do texto (T), e um caracter da chave (C).
#   No inicio da função, a mesma verifica se o caracter está entre
#   'A' e 'Z' ou 'a' e 'z', a fim de evitar criptografar espaços vazios
#   e números. Após isso, uma variavel auxiliar chamada 'indice' é criada.
#   'indice' recebe o número equivalente a variável (T) na tabela ascii
#   subtraído da valor de 'A' na tabela ascii. Portanto, se (T) recebe 'F',
#   o valor de 'indice' será 'F' (70 na tabela ascii) - 'A' (65 na tabela
#   ascii), logo, 'indice' tera o valor de 5 (int). Após isso, uma variável
#   auxiliar de nome 'cifra' é criada. 'cifra' recebe o valor do resto da
#   divisão de 'indice' + (C) - valor de 'A' na tabela ascii por 26.
#   Ou seja, seguindo o exemplo anterior e levando em consideração que o
#   caracter contido em (C) é 'H', temos: cifra = (5+72-65)%26, o que nos
#   leva a -> cifra = 12. Ao final da função, é retornado um caracter
#   que é a soma de 'cifra' com 'A', para voltar ao alfabeto na tabela
#   ascii, portanto, a função retornará 12 + 65 = 77 = 'M' na tabela ascii.
#   Resumindo: o caracter F com a chave H dará output M.
    
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
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// função que soma os caracteres sem ultrapssar o alfabeto
char soma_modular(char caracter, char chave){
    if ('A' <= caracter && caracter <= 'Z'){
        char indice = caracter - 'A';
        char cifra = (indice + chave - 'A') % 26;
        return (cifra + 'A');
    }
    else if('a' <= caracter && caracter <= 'z'){
        char indice = caracter - 'a';
        char cifra = (indice + chave - 'a') % 26;
        return (cifra + 'a');
    }
    return caracter;
}

// função que subtrai os caracteres sem retrogradar o alfabeto
char subtracao_modular(char caracter, char chave){
    if ('A' <= caracter && caracter <= 'Z'){
        char indice = caracter - 'A';
        char cifra = (indice - chave - 'A') % 26;
        return (cifra + 'A');
    }
    else if('a' <= caracter && caracter <= 'z'){
        char indice = caracter - 'a';
        char cifra = (indice - chave - 'a') % 26;
        return (cifra + 'a');
    }
    return caracter;
}

/* EXPLICANDO O FUNCIONAMENTO DAS FUNÇÕES:
    A função usa um caracter do texto (T), e um caracter da chave (C).
    No inicio da função, a mesma verifica se o caracter está entre
    'A' e 'Z' ou 'a' e 'z', a fim de evitar criptografar espaços vazios
    e números. Após isso, uma variavel auxiliar chamada 'indice' é criada.
    'indice' recebe o número equivalente a variável (T) na tabela ascii
    subtraído da valor de 'A' na tabela ascii. Portanto, se (T) recebe 'F',
    o valor de 'indice' será 'F' (70 na tabela ascii) - 'A' (65 na tabela
    ascii), logo, 'indice' tera o valor de 5 (int). Após isso, uma variável
    auxiliar de nome 'cifra' é criada. 'cifra' recebe o valor do resto da
    divisão de 'indice' + (C) - valor de 'A' na tabela ascii por 26.
    Ou seja, seguindo o exemplo anterior e levando em consideração que o
    caracter contido em (C) é 'H', temos: cifra = (5+72-65)%26, o que nos
    leva a -> cifra = 12. Ao final da função, é retornado um caracter
    que é a soma de 'cifra' com 'A', para voltar ao alfabeto na tabela
    ascii, portanto, a função retornará 12 + 65 = 77 = 'M' na tabela ascii.
    Resumindo: o caracter F com a chave H dará output M. */

// criando as variaveis que serão usadas
char cripto = 'a', *texto, *chave;

int main(){
    // alocando memoria para o texto e a chave, ja que podem ter tamanhos grandes
    texto = (char *)malloc(100 * sizeof(char));
    chave = (char *)malloc(100 * sizeof(char));

    // pequena visualização gráfica para o usuário
    printf("-_-_-_-_-  Cifra de Vigenere (C)  -_-_-_-_-\n");
    printf("\" Lembre-se de utilizar o texto inteiramente\n");
    printf("   em letras maiusculas ou minusculas. \n");
    printf("   Esta regra tambem vale para a chave \"\n");

    printf("(1) Criptografar\n(2) Descriptografar\n");
    while(cripto != '1' && cripto != '2'){ // ciclo com while para repetir a captação da variável caso o user não digite '1' ou '2'
        printf("->");
        scanf(" %c", &cripto);
    }

    printf("Texto: ");
    scanf(" %[^\n]s", texto);

    printf("Chave: ");
    scanf(" %[^\n]s", chave);

    // corrigindo o tamanho da chave caso seja menor que o texto a ser criptografado/descriptografado (caso seja maior não há problema)
    while(strlen(chave) < strlen(texto)){
        chave = realloc (chave, strlen(chave) * 2 + 1);
        strncat(chave, chave, strlen(chave));
    }

    // fazendoa  operação a partir da opção escolhida
    switch (cripto){
        case '1':
            for (unsigned int i=0; i < strlen(texto); i++){
                texto[i] = soma_modular(texto[i], chave[i]);
            }
            break;
        case '2':
            for (unsigned int i=0; i < strlen(texto); i++){
                texto[i] = subtracao_modular(texto[i], chave[i]);
            }
            break;
    }

    printf("Cifra: %s\n", texto);

    // limpando a memória apos o uso das variaveis
    free(texto); 
    free(chave);

    return 0;
}
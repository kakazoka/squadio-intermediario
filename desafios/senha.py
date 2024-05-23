def verificar_forca_senha(senha):

    comprimento_minimo = 8
    tem_letra_maiuscula = False
    tem_letra_minuscula = False
    tem_numero = False
    tem_caractere_especial = False
    
    if len(senha) < comprimento_minimo:
        return f'Sua senha é muito curta. Recomenda-se no mínimo {comprimento_minimo} caracteres.'
    
    letra_maiuscula = ['A','B','C','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']    
    for letra in letra_maiuscula:
        if letra in senha:
            tem_letra_maiuscula = True
        if letra.lower() in senha:
            tem_letra_minuscula = True
            
    sequencias_comuns = ['123456', 'abcdef']
    for sequencia in sequencias_comuns:
        if sequencia in senha:
            return 'Sua senha contém uma sequência comum. Tente uma senha mais complexa.'
    
    palavras_comuns = ['password', '123456', 'qwerty']
    if senha in palavras_comuns:
        return 'Sua senha é muito comum. Tente uma senha mais complexa.'

    numeros = ['0','1','2','3','4','5','6','7','8','9']
    for numero in numeros:
        if numero in senha:
            tem_numero = True
    
    simbolos = ['~','!','@','#','$','%','^','&','*','(',')','-','+','/','?','>','<','/','|','=']
    for simbolo in simbolos:
        if simbolo in senha:
            tem_caractere_especial = True
    
    return 'Sua senha atende aos requisitos de segurança. Parabéns!' if len(senha) >= 8 and tem_letra_maiuscula and tem_letra_minuscula and tem_numero and tem_caractere_especial else 'Sua senha não atende aos requisitos de segurança.'

senha = input().strip()

resultado = verificar_forca_senha(senha)

print(resultado)

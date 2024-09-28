import re

# Corrigindo o padrão de regex
numero_telefone = re.compile(r'\d\d\d.\d\d\d.\d\d\d-\d\d')
cpf = 'testando alguma frase apenas para ver se realmente o padrao vai ser encontrado 078.451.799-14 nem liga pra esse numero besta '
verificar = numero_telefone.search(cpf)

# verificar resultado
print('CPF: ', verificar.group())


# Desafios Praticos
# use search() para encontrar o primeiro endereço de email em uma string

buscar_email = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.[a-zA-Z]{2,}')
emails= 'meu nome é valter e meu email é esse aqui do lado uai valtertert@gmail.com'
print(buscar_email.search(emails))

# use findall() para encontrar todas as palavras que começam com maiuscula
texto = 'Me chamo Sergio gosto de maconha sexo e Rock roll '
buscar_maiusculas = re.compile(r'[A-Z]{1,}')
print(buscar_maiusculas.findall(texto))

# use sub() para trocar espaços por hifens
texto2 = 'trocar espaços por hifens não é algo dificil'
trocando_caracteres = re.compile(r'\s+')
print(trocando_caracteres.sub('-', texto2))
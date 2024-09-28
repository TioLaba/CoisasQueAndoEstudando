import re

# compilar padrões com grupos
# use parenteses para separar os grupos
regex = re.compile(r'''([a-zA-Z0-9._%]+) # Nome do usuario  
                   @ # simbolo @ 
                   ([a-zA-Z]+) # Nome do dominio supomos que seja gmail ou hotmail
                   \.([a-zA-Z]{2,}) # Extensão do dominio, .com, .org e etc
                   ''', re.VERBOSE)

# Testar o padrão em um e-mail 
resultado = regex.search('valtertert@gmail.com')

if resultado:
    print("Nome do usuário:", resultado.group(1))
    print("Domínio:", resultado.group(2))
    print("Extensão:", resultado.group(3))


# 1. Grupos de Captura
# Criar um padrão que captura nome de usuário, domínio e extensão de e-mail
regex_captura = re.compile(r'''([a-zA-Z0-9._%+-]+)  # Nome do usuário
                                @                    # Símbolo @
                                ([a-zA-Z]+)          # Nome do domínio
                                \.([a-zA-Z]{2,})     # Extensão do domínio
                             ''', re.VERBOSE)

resultado_captura = regex_captura.search('usuario@exemplo.com')
if resultado_captura:
    print("\nGrupos de Captura:")
    print("Nome do usuário:", resultado_captura.group(1))  # Saída: usuario
    print("Domínio:", resultado_captura.group(2))          # Saída: exemplo
    print("Extensão:", resultado_captura.group(3))         # Saída: com

# 2. Grupos Não Capturantes
# Usar grupos não capturantes para ignorar a parte do domínio ao buscar o e-mail
regex_nao_captura = re.compile(r'(?:[a-zA-Z0-9._%+-]+)@(?!example\.com)([a-zA-Z]+\.[a-zA-Z]{2,})')

resultado_nao_captura = regex_nao_captura.search('usuario@teste.com')
if resultado_nao_captura:
    print("\nGrupos Não Capturantes:")
    print("Domínio (não exemplo.com):", resultado_nao_captura.group(1))  # Saída: teste.com

# 3. Nomes de Grupos
# Usar grupos nomeados para facilitar a leitura
regex_nomeado = re.compile(r'(?P<usuario>[a-zA-Z0-9._%+-]+)@(?P<dominio>[a-zA-Z]+)\.(?P<extensao>[a-zA-Z]{2,})')

resultado_nomeado = regex_nomeado.search('usuario@dominio.com')
if resultado_nomeado:
    print("\nGrupos Nomeados:")
    print("Nome do usuário:", resultado_nomeado.group('usuario'))   # Saída: usuario
    print("Domínio:", resultado_nomeado.group('dominio'))           # Saída: dominio
    print("Extensão:", resultado_nomeado.group('extensao'))         # Saída: com

# 4. Quantificadores em Grupos
# Capturar um padrão com números e letras
regex_quantificadores = re.compile(r'([a-zA-Z]+)(\d{1,3})')

resultado_quantificadores = regex_quantificadores.search('abc123')
if resultado_quantificadores:
    print("\nQuantificadores em Grupos:")
    print("Texto:", resultado_quantificadores.group(1))  # Saída: abc
    print("Número:", resultado_quantificadores.group(2))  # Saída: 123

# 5. Repetição de Grupos
# Captura sequências que se repetem
regex_repeticao = re.compile(r'([a-zA-Z]+) \1')  # Padrão de palavras repetidas

resultado_repeticao = regex_repeticao.search('Olá Olá')
if resultado_repeticao:
    print("\nRepetição de Grupos:")
    print("Palavra repetida encontrada:", resultado_repeticao.group())  # Saída: Olá Olá

import re

# 1. ? - corresponde a zero ou uma ocorrência do grupo anterior.
texto1 = 'col e cola'
regex_question = re.compile(r'col(?:a)?')
print("1. ? :")
print("Exemplo: 'col e cola' ->", regex_question.findall(texto1))  # Saída: ['col', 'cola']
print()

# 2. * - corresponde a zero ou mais ocorrências do grupo anterior.
texto2 = 'col colorido colacao'
regex_asterisco = re.compile(r'col.*')
print("2. * :")
print("Exemplo: 'col colorido colacao' ->", regex_asterisco.findall(texto2))  # Saída: ['col', 'colorido', 'colacao']
print()

# 3. + - corresponde a uma ou mais ocorrências do grupo anterior.
texto3 = 'col colorido coleção'
regex_mais = re.compile(r'col.+')
print("3. + :")
print("Exemplo: 'col colorido coleção' ->", regex_mais.findall(texto3))  # Saída: ['colorido', 'coleção']
print()

# 4. {n} - corresponde a exatamente n ocorrências do grupo anterior.
texto4 = 'aa aaa aaaa'
regex_exactly_n = re.compile(r'a{3}')
print("4. {n} :")
print("Exemplo: 'aa aaa aaaa' ->", regex_exactly_n.findall(texto4))  # Saída: ['aaa']
print()

# 5. {n,} - corresponde a n ou mais ocorrências do grupo anterior.
texto5 = 'a aa aaa a a a a aaaa'
regex_n_ou_mais = re.compile(r'a{2,}')
print("5. {n,} :")
print("Exemplo: 'a aa aaa a a a a aaaa' ->", regex_n_ou_mais.findall(texto5))  # Saída: ['aa', 'aaa', 'aaaa']
print()

# 6. {,m} - corresponde a zero até m ocorrências do grupo anterior.
texto6 = ' a aa aaa'
regex_zero_a_m = re.compile(r'a{,3}')
print("6. {,m} :")
print("Exemplo: ' a aa aaa' ->", regex_zero_a_m.findall(texto6))  # Saída: ['', 'a', 'aa', 'aaa']
print()

# 7. {n,m} - corresponde a no mínimo n e no máximo m ocorrências do grupo anterior.
texto7 = 'a aa aaa aaaa'
regex_n_a_m = re.compile(r'a{2,4}')
print("7. {n,m} :")
print("Exemplo: 'a aa aaa aaaa' ->", regex_n_a_m.findall(texto7))  # Saída: ['aa', 'aaa', 'aaaa']
print()

# 8. {n,m}? ou *? ou +? - faz uma correspondência nongreedy do grupo anterior.
texto8 = 'dasdasdasd<tag1>asdasdasd e dasdasd <tag2> sadjaskjdbasjk'
regex_nongreedy = re.compile(r'<.*?>')
print("8. {n,m}? ou *? ou +? :")
print("Exemplo: 'dasdasdasd<tag1>asdasdasd e dasdasd <tag2> sadjaskjdbasjk' ->", regex_nongreedy.findall(texto8))  # Saída: ['<tag1>', '<tag2>']
print()

# 9. ^spam - a string deve começar com spam.
texto9 = 'qual quer spam e mais texto'
regex_start_spam = re.compile(r'^spam')
print("9. ^spam :")
print("Exemplo: 'spam e mais texto' ->", regex_start_spam.findall(texto9))  # Saída: ['spam']
print()

# 10. spam$ - a string deve terminar com spam.
texto10 = 'texto spam'
regex_end_spam = re.compile(r'spam$')
print("10. spam$ :")
print("Exemplo: 'texto spam' ->", regex_end_spam.findall(texto10))  # Saída: ['spam']
print()

# 11. . - corresponde a qualquer caractere, exceto caracteres de quebra de linha.
texto11 = 'aab axb a b'
regex_ponto = re.compile(r'a.b')
print("11. . :")
print("Exemplo: 'aab axb a b' ->", regex_ponto.findall(texto11))  # Saída: ['aab', 'axb']
print()

# 12. \d, \w e \s - correspondem a dígito, caractere de palavra ou caractere de espaço, respectivamente.
texto12 = '1234'
regex_d = re.compile(r'\d')
print("12. \\d :")
print("Exemplo: '1234' ->", regex_d.findall(texto12))  # Saída: ['1', '2', '3', '4']

texto12_2 = 'a1 b'
regex_w = re.compile(r'\w')
print("12. \\w :")
print("Exemplo: 'a1 b' ->", regex_w.findall(texto12_2))  # Saída: ['a', '1', 'b']

texto12_3 = 'a b'
regex_s = re.compile(r'\s')
print("12. \\s :")
print("Exemplo: 'a b' ->", regex_s.findall(texto12_3))  # Saída: [' ']
print()

# 13. \D, \W e \S - correspondem a qualquer caractere, exceto dígito, caractere de palavra ou caractere de espaço, respectivamente.
texto13 = '!@# 123'
regex_D = re.compile(r'\D')
print("13. \\D :")
print("Exemplo: '!@# 123' ->", regex_D.findall(texto13))  # Saída: ['!', '@', '#', ' ']

texto13_2 = '!@# a1'
regex_W = re.compile(r'\W')
print("13. \\W :")
print("Exemplo: '!@# a1' ->", regex_W.findall(texto13_2))  # Saída: ['!', '@', '#']

texto13_3 = 'a b'
regex_S = re.compile(r'\S')
print("13. \\S :")
print("Exemplo: 'a b' ->", regex_S.findall(texto13_3))  # Saída: ['a', 'b']
print()

# 14. [abc] - corresponde a qualquer caractere que estiver entre os colchetes.
texto14 = 'abcde'
regex_colchetes = re.compile(r'[abc]')
print("14. [abc] :")
print("Exemplo: 'abcde' ->", regex_colchetes.findall(texto14))  # Saída: ['a', 'b', 'c']
print()

# 15. [^abc] - corresponde a qualquer caractere que não esteja entre os colchetes.
texto15 = 'abcde'
regex_nao_colchetes = re.compile(r'[^abc]')
print("15. [^abc] :")
print("Exemplo: 'abcde' ->", regex_nao_colchetes.findall(texto15))  # Saída: ['d', 'e']

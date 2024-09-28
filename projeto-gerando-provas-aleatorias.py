# Projeto guiado do capitulo 2 do livro 
# python automatizando tarefas massantes
from random import shuffle, sample  # Importando funções shuffle e sample do módulo random

# Dicionário com estados brasileiros e suas capitais
estados_brasileiros = {
    "Acre": "Rio Branco",
    "Alagoas": "Maceió",
    "Amapá": "Macapá",
    "Amazonas": "Manaus",
    "Bahia": "Salvador",
    "Ceará": "Fortaleza",
    "Distrito Federal": "Brasília",
    "Espírito Santo": "Vitória",
    "Goiás": "Goiânia",
    "Maranhão": "São Luís",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Minas Gerais": "Belo Horizonte",
    "Pará": "Belém",
    "Paraíba": "João Pessoa",
    "Paraná": "Curitiba",
    "Pernambuco": "Recife",
    "Piauí": "Teresina",
    "Rio de Janeiro": "Rio de Janeiro",
    "Rio Grande do Norte": "Natal",
    "Rio Grande do Sul": "Porto Alegre",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Santa Catarina": "Florianópolis",
    "São Paulo": "São Paulo",
    "Sergipe": "Aracaju",
    "Tocantins": "Palmas"
}

# Queremos 35 provas diferentes, então criaremos um loop
for pergunta in range(1):
    # Criamos então os arquivos com as provas e os gabaritos das respostas
    # Abrindo arquivos com codificação utf-8
    arquivo_prova_perguntas = open('capitaisperguntas%s.txt' % (pergunta + 1), 'w', encoding='utf-8')
    arquivo_prova_respostas = open('capitaisrespostas%s.txt' % (pergunta + 1), 'w', encoding='utf-8')

    # Aqui vamos escrever o cabeçalho da prova
    arquivo_prova_perguntas.write('Nome:\t\t\t\t\t\t\t\t\t\tData:\t\t\t2°TB\n\n')  # Cabeçalho com campos para nome e data
    arquivo_prova_perguntas.write(('' * 20) + 'Capitais brasileiras Prova de Geografia %s' % (pergunta + 1))  # Título da prova
    arquivo_prova_perguntas.write('\n\n')  # Adicionando quebras de linha

    # Vamos embaralhar a ordem dos estados 
    estados = list(estados_brasileiros.keys())  # Criando uma lista dos estados
    shuffle(estados)  # Embaralhando a lista de estados

    # Vamos criar as opções de resposta
    # Vamos percorrer todos os estados em loop, criando uma pergunta para cada um
    for numero_pergunta in range(1, 13):  # Mudando para o tamanho da lista de estados
        resposta_correta = estados_brasileiros[estados[numero_pergunta]]  # Obtendo a capital correta do estado atual
        resposta_errada = list(estados_brasileiros.values())  # Criando uma lista com todas as capitais
        del resposta_errada[resposta_errada.index(resposta_correta)]  # Removendo a capital correta da lista de respostas erradas
        resposta_errada = sample(resposta_errada, 3)  # Selecionando aleatoriamente 3 respostas erradas
        opcoes_resposta = resposta_errada + [resposta_correta]  # Adicionando a resposta correta às opções
        shuffle(opcoes_resposta)  # Embaralhando as opções de resposta

        # Vamos gravar as perguntas e as opções de resposta no arquivo da prova
        arquivo_prova_perguntas.write(f'{numero_pergunta + 1} - Qual a Capital do Estado de {estados[numero_pergunta]} ?\n')  # Escrevendo a pergunta
        for i in range(4):  # Iterando sobre as 4 opções de resposta
            arquivo_prova_perguntas.write(' %s. %s\n' % ('ABCD'[i], opcoes_resposta[i]))  # Escrevendo cada opção no arquivo
        arquivo_prova_perguntas.write('\n')  # Adicionando uma quebra de linha após cada pergunta

        # Vamos gravar as respostas no arquivo gabarito
        arquivo_prova_respostas.write('%s. %s\n' % (numero_pergunta + 1, 'ABCD'[opcoes_resposta.index(resposta_correta)]))  # Escrevendo o gabarito

    # Fechando os arquivos após a criação das provas e gabaritos
    arquivo_prova_perguntas.close()  # Fechando o arquivo de perguntas
    arquivo_prova_respostas.close()  # Fechando o arquivo de respostas

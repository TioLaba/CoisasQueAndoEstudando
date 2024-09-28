from collections import Counter
import re

def analisa_frequencia(texto: str, n: int) -> list:
    # Remove pontuação e transforma tudo em minúsculas
    limpar_pontuacao = re.sub(r'[^\w\s]', '', texto)
    
    # Divide o texto em palavras
    palavras = limpar_pontuacao.lower().split()
    
    # Conta a frequência das palavras
    contador = Counter(palavras)
    
    # Retorna as n palavras mais comuns, ordenadas pela frequência e alfabeticamente
    return sorted(contador.items(), key=lambda item: (-item[1], item[0]))[:n]

# Exemplo de uso
texto_usuario = "Olá, mundo! Como Como Como vai? Tudo bem, e você?"
resultado = analisa_frequencia(texto_usuario, 3)
print(resultado)



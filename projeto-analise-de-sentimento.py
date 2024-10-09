from transformers import pipeline

# Criar um pipeline de análise de sentimentos
sentiment_analysis = pipeline("sentiment-analysis")

# Testar com um exemplo
resultado = sentiment_analysis("eu não gosto de pessoas !")
print(resultado)  # Exibe o rótulo e a pontuação
print('pronto')
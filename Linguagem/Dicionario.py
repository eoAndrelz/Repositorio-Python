import json

def analisar_sentimentos(dados):
  """Analisa os sentimentos em uma lista de dicionários.

  Args:
    dados: Uma lista de dicionários, onde cada dicionário representa um comentário.

  Returns:
    Um dicionário com a contagem de cada sentimento e suas proporções.
  """

  # Inicializa contadores
  contagem_sentimentos = {}
  for sentimento in ["Positivo", "Negativo", "Neutro"]:
      contagem_sentimentos[sentimento] = 0

  # Conta os sentimentos
  for comentario in dados:
      sentimento = comentario.get("Sentimento", "Desconhecido")
      if sentimento in contagem_sentimentos:
          contagem_sentimentos[sentimento] += 1

  # Calcula as proporções
  total_comentarios = sum(contagem_sentimentos.values())
  proporcoes = {sentimento: count / total_comentarios for sentimento, count in contagem_sentimentos.items()}

  return contagem_sentimentos, proporcoes

def carregar_dados(arquivo):
  with open(arquivo, 'r') as f:
      return json.load(f)

# Dados de exemplo
dados = [
    {"Autor": "Joao", "Comentario": "Estou tão feliz hoje!", "Sentimento": "Positivo"},
    {"Autor": "Maria", "Comentario": "Este filme é tão triste. ", "Sentimento": "Negativo"},
    {"Autor": "Carlos ", "Comentario": "Que dia chuvoso entediante... ", "Sentimento": "Positivo"},
    {"Autor": "Ana ", "Comentario": "Adorei a nova música da banda! ", "Sentimento": "Negativo"},
    {"Autor": "Roberto ", "Comentario": "Eureka, consegui resolver este problema  ", "Sentimento": "Positivo"},
]

contagem, proporcoes = analisar_sentimentos(dados)

# Imprime os resultados
print("Contagem de sentimentos:")
for sentimento, count in contagem.items():
    print(f"- {sentimento}: {count}")

print("\nProporções de sentimentos:")
for sentimento, proporcao in proporcoes.items():
    print(f"- {sentimento}: {proporcao:.2f}")

# Mostra apenas os comentários positivos
print("\nComentários positivos:")
for comentario in dados:
    if comentario.get("Sentimento") == "Positivo":
        print(f"- {comentario['Autor']}: {comentario['Comentario']}")

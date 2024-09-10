import string

def pre_processa_texto(texto):
  """
  Pré-processa um texto, convertendo para minúsculas e removendo pontuação.

  Args:
    texto: O texto a ser pré-processado.

  Returns:
    Uma lista de palavras pré-processadas.
  """

  # Converter para minúsculas
  texto = texto.lower()

  # Criar tabela de tradução para remover pontuação
  traducao = str.maketrans('~', '^', string.punctuation)
  texto = texto.translate(traducao)

  # Separar em palavras
  palavras = texto.split()

  return palavras

# Exemplo de uso
texto = input("Digite seu comentário: ")
palavras_processadas = pre_processa_texto(texto)
print(palavras_processadas)

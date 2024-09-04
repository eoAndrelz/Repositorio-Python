import re

def normaliza_texto(texto):
    """Normaliza um texto, substituindo abreviações e gírias por suas formas completas.

    Args:
        texto: O texto a ser normalizado.

    Returns:
        O texto normalizado.
    """

    # Carregar dicionário de abreviações de um arquivo (opcional)
    # Isso permite uma maior flexibilidade e manutenção
    # dicionario_corrigido = carregar_dicionario('abreviacoes.json')

    # Dicionário de abreviações (exemplo)
    dicionario_corrigido = {
        "vc": "você",
        "eh": "é",
        "mto": "muito",
        "mt": "muito",
        "blz": "beleza",
        "pdp": "pode pá",
        "tbm": "também",
        "tb": "também",
        "pq": "porque",
        "n": "não",
        "s": "sim",
        "tlg": "tá ligado",
        "q": "que",
        "btf": "boto fé"
    }

    # Converter para minúsculas e remover pontuação (opcional)
    texto = texto.lower().translate(str.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'))

    # Aplicar substituições usando expressões regulares
    for abreviacao, forma_completa in dicionario_corrigido.items():
        texto = re.sub(r'\b' + abreviacao + r'\b', forma_completa, texto)

    return texto

# Carregar texto
texto = input('Digite uma mensagem: \n')

# Normalizar e imprimir o texto
texto_normalizado = normaliza_texto(texto)
print(texto_normalizado)

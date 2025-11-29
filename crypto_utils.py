from cryptography.fernet import Fernet

def carregar_chave():
    with open("filekey.key", "rb") as chave_arquivo:
        return chave_arquivo.read()

def criptografar_arquivo(caminho_arquivo):
    chave = carregar_chave()
    fernet = Fernet(chave)

    with open(caminho_arquivo, "rb") as arquivo:
        dados = arquivo.read()

    dados_cripto = fernet.encrypt(dados)

    with open(caminho_arquivo, "wb") as arquivo:
        arquivo.write(dados_cripto)

    print(f"Arquivo {caminho_arquivo} criptografado!")

from cryptography.fernet import Fernet, InvalidToken

def descriptografar_arquivo(caminho_arquivo):
    chave = carregar_chave()
    fernet = Fernet(chave)

    with open(caminho_arquivo, "rb") as arquivo:
        dados_cripto = arquivo.read()

    try:
        dados_originais = fernet.decrypt(dados_cripto)
    except InvalidToken:
        print("Erro: o arquivo não está criptografado com essa chave ou foi corrompido.")
        return

    with open(caminho_arquivo, "wb") as arquivo:
        arquivo.write(dados_originais)

    print(f"Arquivo {caminho_arquivo} descriptografado!")

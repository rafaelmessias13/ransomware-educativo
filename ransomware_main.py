from crypto_utils import criptografar_arquivo, descriptografar_arquivo

def menu():
    print("=== MENU ===")
    print("1 - Criptografar arquivo")
    print("2 - Descriptografar arquivo")
    opcao = input("Escolha uma opção (1 ou 2): ")
    return opcao

if __name__ == "__main__":
    caminho = "arquivos_teste/teste.txt"
    escolha = menu()

    if escolha == "1":
        criptografar_arquivo(caminho)
    elif escolha == "2":
        descriptografar_arquivo(caminho)
    else:
        print("Opção inválida.")
2
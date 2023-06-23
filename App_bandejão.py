import os
import qrcode
import random

# Função para exibir o menu
def exibir_menu():
    print("==== Menu ====")
    print("1. Login Administrador")
    print("2. Login Aluno")
    print("3. Sair")

# Função para realizar o login do administrador
def fazer_login_admin():
    nome = input("Digite o nome do administrador: ")
    senha = input("Digite a senha do administrador: ")

    with open(r"C:\Users\chamo\OneDrive\Área de Trabalho\Trabalho_final_laboratório\admin.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(":")
            if len(dados) == 2 and nome == dados[0] and senha == dados[1]:
                print("Login do administrador bem-sucedido!")
                return True

    print("Nome de usuário ou senha inválidos.")
    return False

# Função para realizar o login do aluno
def fazer_login_aluno():
    nome = input("Digite o nome do aluno: ")
    senha = input("Digite a senha do aluno: ")  # Solicita a senha do aluno

    with open(r"C:\Users\chamo\OneDrive\Área de Trabalho\Trabalho_final_laboratório\alunos.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(":")
            if len(dados) == 3 and nome == dados[0] and senha == dados[1]:
                print("Login do aluno bem-sucedido!")
                return nome  # Retorna o nome do aluno
        print("Nome de usuário ou senha inválidos.")
        return None  # Retorna None se o login falhar

# ... outras funções ...

# Função para exibir o cardápio
def exibir_cardapio():
    with open(r"C:\Users\chamo\OneDrive\Área de Trabalho\Trabalho_final_laboratório\cardapio.txt", "r") as arquivo:
        print("==== Cardápio ====")
        print(arquivo.read())

# Função para checar saldo do bandejão
def checar_saldo_bandejao():
    with open(r"C:\Users\chamo\OneDrive\Área de Trabalho\Trabalho_final_laboratório\bandejao.txt", "r") as arquivo:
        saldo_bandejao = float(arquivo.read())
    print(f"Saldo total do bandejão: R$ {saldo_bandejao:.2f}")

# Função para checar saldo do aluno
def checar_saldo_aluno(aluno):
    with open(r"C:\Users\chamo\OneDrive\Área de Trabalho\Trabalho_final_laboratório\alunos.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(":")
            if aluno == dados[0]:
                print(f"Saldo do aluno {aluno}: R$ {dados[2]}")
                return True
    print("Aluno não encontrado.")
    return False

# Função para realizar a recarga por valor
def recarga_por_valor(aluno):
    valor = float(input("Digite o valor da recarga: "))
    metodo_pagamento = input("Digite o método de pagamento (cartao ou pix): ")

    if metodo_pagamento == "cartao":
        dados_cartao = input("Digite os dados do cartão: ")
        print("Recarga por valor realizada com sucesso.")
        gerar_comprovante_recarga(aluno, valor, metodo_pagamento, dados_cartao)
    elif metodo_pagamento == "pix":
        codigo_pix = gerar_codigo_pix()
        print(f"Recarga por valor realizada com sucesso. Código PIX: {codigo_pix}")
        gerar_comprovante_recarga(aluno, valor, metodo_pagamento, codigo_pix)
    else:
        print("Método de pagamento inválido.")

# Função para realizar a recarga por refeição
def recarga_por_refeicao(aluno):
    refeicoes = int(input("Digite o número de refeições: "))
    valor_refeicao = 1.50
    valor_total = refeicoes * valor_refeicao
    metodo_pagamento = input("Digite o método de pagamento (cartao ou pix): ")

    if metodo_pagamento == "cartao":
        dados_cartao = input("Digite os dados do cartão: ")
        print("Recarga por refeição realizada com sucesso.")
        gerar_comprovante_recarga(aluno, valor_total, metodo_pagamento, dados_cartao)
    elif metodo_pagamento == "pix":
        codigo_pix = gerar_codigo_pix()
        print(f"Recarga por refeição realizada com sucesso. Código PIX: {codigo_pix}")
        gerar_comprovante_recarga(aluno, valor_total, metodo_pagamento, codigo_pix)
    else:
        print("Método de pagamento inválido.")

# Função para gerar um código PIX aleatório
def gerar_codigo_pix():
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    codigo_pix = "".join(random.choice(caracteres) for _ in range(10))
    return codigo_pix

# Função para gerar o comprovante de recarga
def gerar_comprovante_recarga(aluno, valor, metodo_pagamento, dados_pagamento):
    comprovante = f"Aluno: {aluno}\nValor: R$ {valor:.2f}\nMétodo de pagamento: {metodo_pagamento}\nDados de pagamento: {dados_pagamento}"
    print("\n==== Comprovante de Recarga ====")
    print(comprovante)
    gerar_qrcode(comprovante)

# Função para gerar um QR Code
def gerar_qrcode(texto):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(texto)
    qr.make(fit=True)

    imagem = qr.make_image(fill_color="black", back_color="white")
    imagem.save("qrcode.png")
    print("\nQR Code gerado com sucesso.")

# Função principal
def main():
    aluno = None  # Variável para armazenar o nome do aluno logado

    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":  # Login do administrador
            if fazer_login_admin():
                while True:
                    print("\n==== Menu Administrador ====")
                    print("1. Exibir Cardápio")
                    print("2. Checar saldo do bandejão")
                    print("3. Voltar")

                    opcao_admin = input("Digite a opção desejada: ")

                    if opcao_admin == "1":  # Exibir Cardápio
                        exibir_cardapio()
                    elif opcao_admin == "2":  # Checar saldo do bandejão
                        checar_saldo_bandejao()
                    elif opcao_admin == "3":  # Voltar
                        break
                    else:
                        print("Opção inválida. Por favor, tente novamente.")
        elif opcao == "2":  # Login do aluno
            aluno = fazer_login_aluno()  # Armazena o nome do aluno logado
            if aluno:
                while True:
                    print(f"\n==== Menu Aluno: {aluno} ====")
                    print("1. Checar saldo")
                    print("2. Recarga por valor")
                    print("3. Recarga por refeição")
                    print("4. Voltar")

                    opcao_aluno = input("Digite a opção desejada: ")

                    if opcao_aluno == "1":  # Checar saldo
                        checar_saldo_aluno(aluno)
                    elif opcao_aluno == "2":  # Recarga por valor
                        recarga_por_valor(aluno)
                    elif opcao_aluno == "3":  # Recarga por refeição
                        recarga_por_refeicao(aluno)
                    elif opcao_aluno == "4":  # Voltar
                        aluno = None  # Limpa o nome do aluno logado
                        break
                    else:
                        print("Opção inválida. Por favor, tente novamente.")
        elif opcao == "3":  # Sair
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Executa a função principal
if __name__ == "__main__":
    main()

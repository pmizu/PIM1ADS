def etapa_1():
    print("Bem-vindo ao nosso sistema!")

    while True:
        nome = input("Por favor, digite seu nome: ")
        idade = input("Agora, digite sua idade: ")

        if idade.isdigit():
            idade = int(idade)
            if idade <= 16:
                break
            else:
                print(
                    "Apenas usuários com idade de até 16 anos podem se cadastrar. Tente novamente.")
        else:
            print("Entrada inválida! Por favor, digite um número.")

    return nome, idade


def etapa_2():
    resposta = input(
        "Você autoriza o uso de seus dados para análises estatísticas? (Sim/Não): ").strip().lower()

    if resposta == "sim":
        return True
    elif resposta == "não":
        print("Entendido! Seus dados não serão utilizados. Obrigado por participar.")
        return False
    else:
        print("Entrada inválida! Responda apenas com 'Sim' ou 'Não'.")
        return etapa_2()


def etapa_3():
    print("\n📌 O que é Tecnologia da Informação?")
    print("Tecnologia da Informação (TI) envolve o uso de sistemas computacionais, software, redes e infraestrutura digital para coletar, processar, armazenar e distribuir informações.")
    print("Ela é essencial em praticamente todas as áreas da sociedade, desde comunicação e entretenimento até saúde, negócios e segurança.")
    print("Se tornou uma das áreas mais importantes para o desenvolvimento e inovação no mundo moderno.")


def etapa_4():
    while True:
        print("\n📌 Escolha uma forma de representação de algoritmos:")
        print("1. Pseudocódigo")
        print("2. Fluxograma")

        escolha = input(
            "\nDigite o número correspondente à sua escolha: ").strip()

        if escolha == "1":
            print("\nVocê escolheu: Pseudocódigo. Ele é uma representação textual e estruturada do algoritmo, usando uma linguagem próxima do português (ou inglês) com comandos simples.")
            print("Exemplo:")
            print("Início")
            print("   Ler A")
            print("   Ler B")
            print("   Soma ← A + B")
            print("   Escrever 'Resultado:', Soma")
        elif escolha == "2":
            print("\nVocê escolheu: Fluxograma. O Fluxograma é uma representação gráfica do algoritmo usando símbolos visuais padronizados (como retângulos, losangos e setas) para mostrar o fluxo das ações.")
            print("Exemplo (fluxograma textual):")
            print(
                "[Início] → [Ler A] → [Ler B] → [Soma = A + B] → [Escrever Resultado] → [Fim]")
        else:
            print(
                "Opção inválida! Por favor, escolha 1 para Pseudocódigo ou 2 para Fluxograma.")
            continue

        while True:
            comando = input(
                "\nDigite 'avançar' para prosseguir ou 'voltar' para escolher novamente: ").strip().lower()
            if comando == "avançar":
                return
            elif comando == "voltar":
                break
            else:
                print(
                    "Comando inválido! Digite 'avançar' para seguir ou 'voltar' para retornar à escolha.")


def etapa_5():
    while True:
        resposta = input(
            "\nDeseja sair do sistema? (Sim/Não): ").strip().lower()
        if resposta == "sim":
            print("\nSaindo do sistema... Reiniciando cadastro.\n")
            return False  # Retorna à etapa 1
        elif resposta == "não":
            print("\nVoltando para a etapa anterior...\n")
            return True  # Retorna à etapa 4
        else:
            print("Entrada inválida! Responda apenas com 'Sim' ou 'Não'.")


def main():
    while True:
        nome, idade = etapa_1()
        if etapa_2():
            etapa_3()
            while True:
                etapa_4()
                if etapa_5():
                    continue  # Volta para etapa 4
                else:
                    break  # Reinicia cadastro


main()


def etapa_5():
    while True:
        resposta = input(
            "\nDeseja sair do sistema? (Sim/Não): ").strip().lower()
        if resposta == "sim":
            print("\nSaindo do sistema... Reiniciando cadastro.\n")
            return False  # Retorna à etapa 1
        elif resposta == "não":
            print("\nVoltando para a etapa anterior...\n")
            return True  # Retorna à etapa 4
        else:
            print("Entrada inválida! Responda apenas com 'Sim' ou 'Não'.")


def main():
    while True:
        nome, idade = etapa_1()
        if etapa_2():
            etapa_3()
            while True:
                etapa_4()
                if etapa_5():
                    continue  # Volta para etapa 4
                else:
                    break  # Reinicia cadastro


main()

import os
import sys

def clear():
    os.system("clear")

def login():
    clear()
    print("LOGIN")
    print("---------")
    print("")
    user = input("Usuario: ")
    password = input("Senha: ")

    if user == user_cadastrado and password == senha_cadastrada:
        print("Login bem-sucedido!")
    else:
        print("Credenciais incorretas!")
        sys.exit()

def cadastro():
    clear()
    new_user = input("Digite seu nome de usuário: ")
    new_password = input("Digite sua senha: ")

    global user_cadastrado, senha_cadastrada
    user_cadastrado = new_user
    senha_cadastrada = new_password

    print("Cadastro bem-sucedido!")
    print("")
    input("Pressione ENTER para continuar...")
    login()


user_cadastrado = ''
senha_cadastrada = ''

while True:
    print("")
    print(f"Olá! Seja bem-vindo(a) ao portal TECHMED")
    print("")
    input("Pressione ENTER para continuar...")
    clear()

    print('1 - Fazer Login')
    print('2 - Fazer Cadastro')
    print("")
    op = input('Escolha uma opção (1 ou 2): ')

    if op == '1':
        login()
    elif op == '2':
        cadastro()
    else:
        print('Opção inválida.')
        sys.exit()

    clear()


    print("Escolha uma das opções para seguir: ")
    print("1 - Informações sobre nossos serviços")
    print("2 - Entre em contato conosco")
    print("3 - Conheça os integrantes da equipe")
    print("4 - Acesse o nosso website")
    print("")

    op = int(input("Digite a opção desejada: "))

    match op:
        case 1:
            clear()
            print(f"Boa escolha {user_cadastrado}! Sobre qual produto você deseja obter informações?")
            print("")
            print("1 - Plataforma de Telessaúde Centralizada")
            print("2 - Dispositivo de monitoramento remoto")
            print("3 - Inteligência Artificial para Diagnóstico Preliminar")
            print("4 - Programas de Educação em Saúde Personalizados")
            print("5 - Voltar para o início")
            print("")

            produto = int(input("Digite a opção desejada: "))

            match produto:
                case 1:
                    clear()
                    print(f"A Plataforma de Telessaúde Centralizada do TechMed é a espinha dorsal de nosso sistema, oferecendo ")
                    print("uma gama abrangente de serviços de saúde virtual. Integramos videochamadas, chat e consultas remotas para ")
                    print("garantir atendimento médico acessível a qualquer momento e em qualquer lugar. Essa abordagem inovadora não apenas")
                    print("reduz a necessidade de deslocamento, mas também permite uma interação mais próxima entre pacientes e ")
                    print("profissionais de saúde, promovendo um cuidado mais personalizado e eficiente.")
                    print("")

                    input("Pressione ENTER para continuar...")

                    clear()
                    print(f"Obrigado pelo acesso {user_cadastrado}! Você deseja voltar ao menu inicial ou finalizar o programa?")
                    print("")
                    print("1 - Voltar ao menu inicial")
                    print("2 - Encerrar o programa.")
                    print("")

                    i = int(input("Digite a opção desejada: "))

                    if (i == 1):
                        clear()
                    if (i == 2):
                        clear()
                        sys.exit()
                case 2:
                    clear()
                    print(f"No coração do TechMed estão os Dispositivos de Monitoramento Remoto, que capacitam os pacientes a ")
                    print("monitorar suas condições de saúde em tempo real. Essa integração de tecnologia permite a coleta de dados vitais, ")
                    print("proporcionando aos profissionais de saúde uma visão abrangente e imediata do estado de saúde dos pacientes. Isso ")
                    print("não apenas agiliza a tomada de decisões clínicas, mas também permite intervenções precoces, especialmente em ")
                    print("casos de condições crônicas.")
                    print("")
                    input("Pressione ENTER para continuar...")

                    clear()
                    print(f"Obrigado pelo acesso {user_cadastrado}! Você deseja voltar ao menu inicial ou finalizar o programa?")
                    print("")
                    print("1 - Voltar ao menu inicial")
                    print("2 - Encerrar o programa.")
                    print("")

                    i = int(input("Digite a opção desejada: "))

                    if (i == 1):
                        clear()
                    if (i == 2):
                        clear()
                        sys.exit()
                case 3:
                    clear()
                    print(f"A implementação de algoritmos de Inteligência Artificial (IA) é um diferencial fundamental do ")
                    print("TechMed. Esses algoritmos realizam análises preliminares de sintomas, permitindo diagnósticos rápidos e ")
                    print("eficientes. Ao utilizar dados históricos e informações em tempo real, a IA do TechMed é uma ferramenta valiosa ")
                    print("para profissionais de saúde, proporcionando insights adicionais que podem orientar decisões de tratamento.")
                    print("")

                    input("Pressione ENTER para continuar...")

                    clear()
                    print(f"Obrigado pelo acesso {user_cadastrado}! Você deseja voltar ao menu inicial ou finalizar o programa?")
                    print("")
                    print("1 - Voltar ao menu inicial")
                    print("2 - Encerrar o programa.")
                    print("")

                    i = int(input("Digite a opção desejada: "))

                    if (i == 1):
                        clear()
                    if (i == 2):
                        clear()
                        sys.exit()
                case 4:
                    clear()
                    print(f"Os Programas de Educação em Saúde Personalizados do TechMed são desenvolvidos para capacitar os ")
                    print("pacientes a gerenciar proativamente sua saúde. Oferecemos recursos educacionais adaptados às necessidades ")
                    print("individuais, entregues através da plataforma. Isso não apenas melhora a compreensão das condições de saúde, mas")
                    print("também incentiva a adoção de comportamentos saudáveis, fortalecendo a parceria entre pacientes e profissionais ")
                    print("de saúde.")
                    print("")

                    input("Pressione ENTER para continuar...")

                    clear()
                    print(f"Obrigado pelo acesso {user_cadastrado}! Você deseja voltar ao menu inicial ou finalizar o programa?")
                    print("")
                    print("1 - Voltar ao menu inicial")
                    print("2 - Encerrar o programa.")
                    print("")

                    i = int(input("Digite a opção desejada: "))

                    if (i == 1):
                        clear()
                    if (i == 2):
                        clear()
                        sys.exit()
                case 5:
                    clear()
                  

        case 2:
            clear()
            print(f"Ok {user_cadastrado}. Por qual canal deseja entrar em contato?")
            print("")
            print("")
            print("1 - Telefone")
            print("2 - Whatsapp")
            print("3 - E-mail")
            print("4 - Website")
            print("")
            print("")

            canal = int(input("Digite a opção desejada: "))

            match canal:
                case 1:
                    clear()
                    print("Para entrar em contato conosco via telefone, basta ligar no número abaixo para ser atendido por um dos nossos funcionários:")
                    print("")
                    print("0800-1234-4321")
                    print("")
                    print("")
                    input("Pressione ENTER para continuar...")

                    clear()
                    print(f"Obrigado pelo acesso {user_cadastrado}! Você deseja voltar ao menu inicial ou finalizar o programa?")
                    print("")
                    print("1 - Voltar ao menu inicial")
                    print("2 - Encerrar o programa.")
                    print("")

                    i = int(input("Digite a opção desejada: "))

                    if (i == 1):
                        clear()
                    if (i == 2):
                        clear()
                        sys.exit()
                case 2:
                    clear()
                    print("Para entrar em contato conosco via Whatsapp, basta salvar o número abaixo e enviar uma mensagem com seu user_cadastrado e sua dúvida:")
                    print("")
                    print("11 91234-4321")
                    print("")
                    print("")
                    input("Pressione ENTER para continuar...")

                    clear()
                    print(f"Obrigado pelo acesso {user_cadastrado}! Você deseja voltar ao menu inicial ou finalizar o programa?")
                    print("")
                    print("1 - Voltar ao menu inicial")
                    print("2 - Encerrar o programa.")
                    print("")

                    i = int(input("Digite a opção desejada: "))

                    if (i == 1):
                        clear()
                    if (i == 2):
                        clear()
                        sys.exit()
                case 3:
                    clear()
                    print("Para entrar em contato conosco via E-mail, basta enviar sua mensagem com seu user_cadastrado e sua dúvida no endereço abaixo:")
                    print("")
                    print("techmedcomp@gmail.com")
                    print("")
                    print("")
                    input("Pressione ENTER para continuar...")

                    clear()
                    print(f"Obrigado pelo acesso {user_cadastrado}! Você deseja voltar ao menu inicial ou finalizar o programa?")
                    print("")
                    print("1 - Voltar ao menu inicial")
                    print("2 - Encerrar o programa.")
                    print("")

                    i = int(input("Digite a opção desejada: "))

                    if (i == 1):
                        clear()
                    if (i == 2):
                        clear()
                        sys.exit()
                case 4:
                    clear()
                    print("Para entrar em contato conosco através do nosso website, basta acessar o link a seguir:")
                    print("")
                    print("https://techmedcomp.42web.io")
                    print("")
                    print("")
                    input("Pressione ENTER para continuar...")

                    clear()
                    print(f"Obrigado pelo acesso {user_cadastrado}! Você deseja voltar ao menu inicial ou finalizar o programa?")
                    print("")
                    print("1 - Voltar ao menu inicial")
                    print("2 - Encerrar o programa.")
                    print("")

                    i = int(input("Digite a opção desejada: "))

                    if (i == 1):
                        clear()
                    if (i == 2):
                        clear()
                        sys.exit()
                    


            clear()
            print(f"Obrigado pelo acesso {user_cadastrado}! Você deseja voltar ao menu inicial ou finalizar o programa?")
            print("")
            print("1 - Voltar ao menu inicial")
            print("2 - Encerrar o programa.")
            print("")

            i = int(input("Digite a opção desejada: "))

            if (i == 1):
                clear()
            if (i == 2):
                clear()
                sys.exit()
        case 3:
            clear()
            print(f"Segue abaixo nossas redes sociais:")
            print("")
            print("[RM554328] - João Santos - @jvs4nt")
            print("[RM552671] - Willian Dantas - @danielwod_")
            print("[RM553324] - Ryan Azanha - @ryanazanha_")

            print("")

            input("Pressione ENTER para continuar...")

            clear()
            print(f"Obrigado pelo acesso {user_cadastrado}! Você deseja voltar ao menu inicial ou finalizar o programa?")
            print("")
            print("1 - Voltar ao menu inicial")
            print("2 - Encerrar o programa.")
            print("")

            i = int(input("Digite a opção desejada: "))

            if (i == 1):
                clear()
            if (i == 2):
                clear()
                sys.exit()
        case 4:
            clear()
            print(f"Que bom que deseja acessar o nosso website {user_cadastrado}! Basta acessar do seu navegador o link a seguir...")
            print("")
            print("Link: https://techmedcomp.42web.io")
            print("")
            print("")
            input("Pressione ENTER para continuar...")

            clear()

            print(f"Obrigado pelo acesso {user_cadastrado}! Você deseja voltar ao menu inicial ou finalizar o programa?")
            print("")
            print("1 - Voltar ao menu inicial")
            print("2 - Encerrar o programa.")
            print("")

            i = int(input("Digite a opção desejada: "))

            if (i == 1):
                clear()
            if (i == 2):
                clear()
                sys.exit()

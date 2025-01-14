from funcoes import * 

def main():
    registro = []
    while True:
        print("\n")
        tela()
        op = int(input("Digite uma opcao: "))

        if op == 1:
            print("\n")
            print("=- Cadastro -=")
            nome = input("Nome: ")
            cpf = input("CPF: ")
            data_nasc = input("Data de nascimento: ")
            telefone = input("Telefone: ")
            registro = cadastrar_paciente(registro, nome, cpf, data_nasc, telefone)

        elif op == 2:
            print("\n")
            print("=- Lista de pacientes -=")
            pacientes_cadastrados(registro)

        elif op == 3:
            print("\n")
            print("=- Atualizar pacientes -=")
            alt_cpf = input("Digite o CPF do paciente: ")
            novo_nome = input("Nome: ")
            nova_data = input("Data de nascimento: ")
            novo_tel = input("Telefone: ")

            alterar_paciente(registro, alt_cpf, novo_nome, nova_data, novo_tel)

        elif op == 4:
            print("\n")
            print("=- Remover paciente -=")
            rmv_cpf = input("Digite o CPF do paciente: ") 
        
            remover_paciente(registro, rmv_cpf)
        
        elif op == 5:
            print("Saindo..")
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
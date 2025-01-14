def tela():
    print("=- CONSULTÓRIO MÉDICO -=")
    print("[1] Cadastrar paciente")
    print("[2] Pacientes cadastrados")
    print("[3] Atualizar pacientes")
    print("[4] Remover pacientes")
    print("[5] Sair")

def formatar_cpf(cpf):
    # remove os caracteres do cpf
    cpf = cpf.replace(".", "").replace("-", "").replace(" ", "")
    # verifica o tamanho
    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    else:
        return "CPF inválido"
    
def formatar_telefone(telefone):
    # remove os caracteres do telefone
    telefone = telefone.replace("-", "").replace("(", "").replace(")", "").replace(" ", "")
    # verifica o tamanho
    if len(telefone) == 11:
        return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    elif len(telefone) == 10:
        return f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}"
    
def cadastrar_paciente(registro, nome, cpf, data_nasc, telefone):

    cpf_formatado = formatar_cpf(cpf)
    telefone_formatado = formatar_telefone(telefone)

    # verifica se ja tem algum cadastro c o cpf ou telefone passado
    for paciente in registro:
        if cpf_formatado == paciente[2] or telefone_formatado == paciente[4]:
            print("CPF ou telefone já cadastrado")
            return registro
        
    # incrementa o id a cada registro
    id = len(registro) + 1
    # adiciona os atributos na entidade
    paciente = [id, nome, cpf_formatado, data_nasc, telefone_formatado]
    # coloca a entidade na lista registro
    registro.append(paciente)
    print("Paciente cadastrado com sucesso!")

    return registro

def pacientes_cadastrados(registro):
    # verifica se tem algum paciente cadastrado
    if registro:
        # percorre as colunas da lista registro
        for col in registro:
            # formata cpf e telefone
            cpf = formatar_cpf(col[2])
            tel = formatar_telefone(col[4])
            print(f"ID: {col[0]:<3} | Nome: {col[1]} | CPF: {cpf} | Data de Nascimento: {col[3]} | Telefone: {tel}")
    else:
        print("Não há pacientes cadastrados.")

def remover_paciente(registro, cpf):

    cpf_formatado = formatar_cpf(cpf)
    # verifica se tem registro
    if registro:
        # Procura o paciente pelo CPF
        for i, paciente in enumerate(registro):
            # Se o CPF for encontrado
            if paciente[2] == cpf_formatado:
                # remove o paciente da lista usando o indice
                del registro[i]
                print(f"Paciente com o CPF {cpf_formatado} foi removido.")
                return  # encerra a funcao
        print("Paciente não encontrado.")
    else:
        print("Não há pacientes cadastrados.")


def alterar_paciente(registro, cpf, nome, data_nasc, telefone):
    cpf_formatado = formatar_cpf(cpf)
    novo_tel = formatar_telefone(telefone)
    # verifica se tem registros
    if registro:
        # procura o paciente pelo cpf
        for paciente in registro:

            if paciente[2] == cpf_formatado:   
                paciente[1] = nome
                paciente[3] = data_nasc
                paciente[4] = novo_tel 
                print(f"Dados do paciente {paciente[0]} atualizados.") # mostra o id do paciente alterado
                return  # encerra a função
            else:
                print("Paciente não encontrado.")
    else:
        print("Não há pacientes cadastrados.")  

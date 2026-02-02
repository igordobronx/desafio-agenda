def adicionar_contato(contatos, nome_contato, telefone_contato):
    novo_contato = {"nome": nome_contato, "telefone": telefone_contato, "status": False  }
    contatos.append(novo_contato)
    print(f"\ncontato {nome_contato} com telefone {telefone_contato} adicionado com sucesso")
    return

def visualizar_contato(contatos):
    print("\nlista de contatos: \n")
    if not contatos:
        print("sua agenda esta vazia.")
        return
    
    for indice, contato in enumerate(contatos, start=1):
        status = "✓" if contato["status"] else " "
        nome = contato["nome"]
        tel = contato["telefone"]
    
        print(f"{indice}. [{status}] Nome: {nome} / Telefone: {tel}")

def atualizar_contato(contatos):
    visualizar_contato(contatos)
    if not contatos:
        return
    indice_contato = int(input("digite o numero do contato que voce deseja editar: "))
    indice_ajustado = int(indice_contato) - 1

    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
        novo_nome = input("digite o novo nome: ")
        novo_tel = input("digite o novo telefone: ")

        contatos[indice_ajustado]["nome"] = novo_nome
        contatos[indice_ajustado]["telefone"] = novo_tel

        print(f"\ncontato {indice_contato} adicionado com sucesso.\n")
    else:
        print("indice de contato invalido.")
    return

def favoritar_contatos(contatos):
    visualizar_contato(contatos)
    indice_contato = int(input("digite o numero do contato que voce quer favoritar: "))

    
    indice_ajustado = int(indice_contato) - 1
    contatos[indice_ajustado]["status"] = True
    
    print(f"indice {indice_contato} favoritado com sucesso...")

def deletar_contatos(contatos):
    visualizar_contato(contatos)
    if not contatos:
        return
    #1-pedir o indice:
    indice_contato = int(input("digite o numero do contato que voce deseja deletar:"))
    indice_ajustado = indice_contato - 1

    #2- ver se o indice existe:
    if 0 <= indice_ajustado < len(contatos):
        #remover usando o pop
        contato_removido = contatos.pop(indice_ajustado)
        print(f"\n o contato {contato_removido['nome']} foi removido com sucesso.")
    else:
        print("\n numero invalido de contato.")


contatos = []

while True:

    print("\n Contatos do Igão \n")
    print("1- Adicionar contato")
    print("2- Ver contatos")
    print("3- atualizar contatos")
    print("4- deletar contatos")
    print("5- Marcar favorito")
    print("6- sair")

    escolha = input("escolha um numero/opcao: ")

    if escolha ==  "1":
        nome_contato = input("digite o nome do contato: ")
        telefone_contato = input("digite o telefone do contato: ")
        adicionar_contato(contatos, nome_contato, telefone_contato)

    elif escolha == "2":
        visualizar_contato(contatos)

    elif escolha == "3":
        atualizar_contato(contatos)

    elif escolha == "4":
        deletar_contatos(contatos)

    elif escolha == "5":
        favoritar_contatos(contatos)




    elif escolha == "6":
        print("Voce escolheu sair...")
        break


print("\nAgenda de contatos finalizada\n")
from database import (
    criar_tabela, salvar_pet, listar_pets, deletar_pet, 
    atualizar_pet, salvar_agendamento, listar_agendamentos
)

criar_tabela()

def menu():
    while True:
        print("\n--- 🐾 SISTEMA PETSHOP 🐾 ---")
        print("1. Cadastrar novo Pet")
        print("2. Listar todos os Pets")
        print("3. Deletar um Pet")
        print("4. Editar dados do Pet")
        print("5. Agendar Serviço (Banho/Tosa)") # Nova!
        print("6. Ver Agenda de Serviços")       # Nova!
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- 📝 CADASTRO DE PET ---")
            nome = input("Nome do pet: ")
            especie = input("Espécie (ex: Cachorro, Gato): ")
            raca = input("Raça: ")
            idade = int(input("Idade: "))
            responsavel = input("Nome do Dono (Responsável): ")
            telefone = input("Telefone de contato: ")
            salvar_pet(nome, especie, raca, idade, responsavel, telefone)

        elif opcao == "2":
            print("\n--- 📋 LISTA DE PETS CADASTRADOS ---")
            pets = listar_pets()
            if not pets:
                print("Nenhum pet cadastrado ainda.")
            else:
                for pet in pets:
                    print(f"ID: {pet[0]} | Nome: {pet[1]} | Espécie: {pet[2]} | Raça: {pet[3]} | Idade: {pet[4]} anos | Dono: {pet[5]} | Tel: {pet[6]}")

        elif opcao == "3":
            print("\n--- 🗑️ REMOVER PET ---")
            pets = listar_pets()
            if not pets:
                print("Não há pets cadastrados para deletar.")
            else:
                for pet in pets:
                    print(f"ID: {pet[0]} | Nome: {pet[1]} ({pet[2]})")
                id_escolhido = int(input("\nDigite o ID do pet que deseja deletar: "))
                deletar_pet(id_escolhido)

        elif opcao == "4":
            print("\n--- 🔄 EDITAR DADOS DO PET ---")
            pets = listar_pets()
            if not pets:
                print("Não há pets cadastrados para editar.")
            else:
                for pet in pets:
                    print(f"ID: {pet[0]} | Nome: {pet[1]} | Idade: {pet[4]} anos | Tel: {pet[6]}")
                id_escolhido = int(input("\nDigite o ID do pet que deseja atualizar: "))
                nova_idade = int(input("Digite a nova idade do pet: "))
                novo_telefone = input("Digite o novo telefone de contato: ")
                atualizar_pet(id_escolhido, nova_idade, novo_telefone)

        elif opcao == "5":
            print("\n--- 📅 AGENDAR SERVIÇO ---")
            pets = listar_pets()
            if not pets:
                print("Cadastre um pet antes de agendar um serviço.")
            else:
                for pet in pets:
                    print(f"ID: {pet[0]} | Nome: {pet[1]} (Dono: {pet[5]})")
                
                id_pet = int(input("\nDigite o ID do pet: "))
                servico = input("Tipo de serviço (Banho / Tosa / Consulta): ")
                data_hora = input("Data e Hora (ex: 10/10 às 14:00): ")
                
                salvar_agendamento(id_pet, servico, data_hora)

        elif opcao == "6":
            print("\n--- 📋 AGENDA DO PETSHOP ---")
            agenda = listar_agendamentos()
            if not agenda:
                print("Nenhum serviço agendado para os próximos dias.")
            else:
                for agendamento in agenda:
                    print(f"Agendamento Nº: {agendamento[0]} | Pet: {agendamento[1]} | Serviço: {agendamento[2]} | Horário: {agendamento[3]}")

        elif opcao == "7":
            print("Obrigado por usar o sistema do PetShop! Até logo! 👋")
            break
            
        else:
            print("❌ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
Python
def main():
    tarefas = []
    while True:
        print("\n--- GERENCIADOR DE TAREFAS ---")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tarefa = input("Digite a tarefa: ")
            tarefas.append({"nome": tarefa, "concluida": False})
        elif opcao == "2":
            for i, t in enumerate(tarefas):
                status = "[x]" if t["concluida"] else "[ ]"
                print(f"{i+1}. {status} {t['nome']}")
        elif opcao == "3":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
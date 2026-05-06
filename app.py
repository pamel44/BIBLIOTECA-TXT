#sistema de biblioteca console
while True:
    print("/n ====sistema de biblioteca====")
    print("1- cadastrar livro")
    print("2- listar livros")
    print("3- sair")
    
    opcao = input("escolha uma opcao: ")

    if opcao == "1":
        titulo = input("digite o titulo do livro: ")
        autor = input("digite o autor: ")

        arquivo = open("livros.txt", "a")
        arquivo.write(titulo + "-" + autor+" /n")
        arquivo.close()

        print("livro cadastrado !")


from classes import Livro

livro1 = Livro ('Aprendendo Python', 'José', 2011)
livro2 = Livro ('Machine Learning com Python', 'Carlos', 2015)


def main():
    Livro.listar_livros()

if __name__ == '__main__':
    main()
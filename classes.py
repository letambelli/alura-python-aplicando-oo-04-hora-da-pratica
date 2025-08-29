class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano_publicacao} '
    
    @classmethod
    def listar_livros(cls):
        print(f'{'Título'.ljust(40)} | {'Autor'.ljust(25)} | {'Ano de Publicação'.ljust(25)}')
        for livro in cls.livros:
            print(f'{livro._titulo.ljust(40)} | {livro._autor.ljust(25)} | {str(livro._ano_publicacao).ljust(25)} | {livro._disponivel}')

    @classmethod
    def emprestar_livro(self):
        return 'Disponível' if self._disponivel else 'Não '

class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.membros = []

    def adicionar_livro(self, livro):
        self.catalogo.append(livro)

    def adicionar_membro(self, membro):
        self.membros.append(membro)

    def emprestar_livro(self, membro, livro):
        if not livro.emprestado:
            livro.emprestado = True
            membro.adicionar_ao_historico(livro)
            print(f"Livro '{livro.titulo}' emprestado ao membro '{membro.nome}'.")
        else:
            print(f"Livro '{livro.titulo}' já está emprestado.")

    def devolver_livro(self, livro):
        if livro.emprestado:
            livro.emprestado = False
            print(f"Livro '{livro.titulo}' foi devolvido.")
        else:
            print(f"Livro '{livro.titulo}' não está emprestado.")

    def pesquisar_livro_por_titulo(self, titulo):
        for livro in self.catalogo:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None

    def pesquisar_livro_por_autor(self, autor):
        for livro in self.catalogo:
            if livro.autor.lower() == autor.lower():
                return livro
        return None

    def pesquisar_livro_por_id(self, id):
        for livro in self.catalogo:
            if livro.id == id:
                return livro
        return None

    def __str__(self):
        return f"Biblioteca com {len(self.catalogo)} livros e {len(self.membros)} membros."


class Livro:
    def __init__(self, titulo, autor, id):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.emprestado = False

    def __str__(self):
        return f"ID: {self.id}, Título: {self.titulo}, Autor: {self.autor}, Emprestado: {self.emprestado}"



class Membro:
    numero_de_membros = 0

    def __init__(self, nome):
        self.nome = nome
        self.historico_de_livros = []
        Membro.numero_de_membros += 1

    def adicionar_ao_historico(self, livro):
        self.historico_de_livros.append(livro)

    def __str__(self):
        return f"Nome: {self.nome}, Histórico de Livros: {[livro.titulo for livro in self.historico_de_livros]}"




biblioteca = Biblioteca()

livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1)
livro2 = Livro("1984", "George Orwell", 2)


biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)


membro1 = Membro("Alice")
membro2 = Membro("Bob")


biblioteca.adicionar_membro(membro1)
biblioteca.adicionar_membro(membro2)

biblioteca.emprestar_livro(membro1, livro1)
biblioteca.devolver_livro(livro1)
biblioteca.emprestar_livro(membro2, livro2)

livro_pesquisado = biblioteca.pesquisar_livro_por_titulo("1984")
print(livro_pesquisado)

print(biblioteca)
print(membro1)
print(membro2)

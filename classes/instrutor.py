class Instrutor:

    def __init__(
        self,
        nome,
        sobrenome,
        data_nascimento,
        endereco,
        telefone,
        id = None
        ):
        
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.telefone = telefone
        self.id = id

    def __str__(self) -> str:
        return f"""\nNome: {self.nome}\nSobrenome: {self.sobrenome}\ndata_nascimento: {self.data_nascimento}\nendereco: {self.endereco}\ntelefone: {self.telefone}\nid: {self.id}"""
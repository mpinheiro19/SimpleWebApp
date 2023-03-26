class Cliente:

    def __init__(
        self,
        nome,
        sobrenome,
        data_nascimento,
        endereco,
        telefone,
        email,
        tipo_plano,
        data_inicio,
        ativo,
        id = None
        ):
        
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.tipo_plano = tipo_plano
        self.data_inicio = data_inicio
        self.ativo = ativo
        self.id = id

    def __str__(self) -> str:
        return f"""\nNome: {self.nome}\nSobrenome: {self.sobrenome}\ndata_nascimento: {self.data_nascimento}\nendereco: {self.endereco}\ntelefone: {self.telefone}\ne-mail: {self.email}\nPlano: {self.tipo_plano}\nInicio Relacionamento: {self.data_inicio}\nAtivo: {self.ativo}\nid: {self.id}"""
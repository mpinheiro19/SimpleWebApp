class Atividade:

    def __init__(
        self,
        nome,
        instrutor,
        data_atividade,
        duracao,
        capacidade,
        tipo_plano,
        ativo,
        id=None
        ):
        
        self.nome = nome
        self.instrutor = instrutor
        self.data_atividade = data_atividade
        self.duracao = duracao
        self.capacidade = capacidade
        self.tipo_plano = tipo_plano
        self.ativo = ativo
        self.id = id

    def __str__(self) -> str:
        return f"""\nNome: {self.nome}\nInstrutor: {self.instrutor}\ndata_atividade: {self.data_atividade}\nDuração: {self.duracao}\nCapacidade: {self.capacidade}\nPlano: {self.tipo_plano}\nAtivo: {self.ativo}\nid: {self.id}"""

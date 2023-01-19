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

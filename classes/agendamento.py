class Agendamento:

    def __init__(self, atividade, cliente, id=None):

        self.atividade = atividade
        self.cliente = cliente
        self.id = id

    def __str__(self):

        return f"\nid: {self.id}\nAtividade: {self.atividade}\nCliente: {self.cliente}"
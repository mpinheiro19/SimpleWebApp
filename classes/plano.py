class TipoPlano:

    def __init__(self, plano, id = None):
        self.plano = plano
        self.id = id

    def __str__(self) -> str:
        return f"Plano: {self.plano}; id: {self.id}\n"
class CfdiTrasladado:
    trasladado = {}
    def __init__(self):
        self.base = None
        self.impuesto = None
        self.tipo_factor = None
        self.tasa_cuota = None
        self.importe = None
    
    def get_trasladado(self):
        return self.trasladado
class CfdiTrasladado:
    trasladado = {}

    def __init__(self, base, impuesto, tipo_factor, tasa_cuota, importe):
        self.base = base
        self.impuesto = impuesto
        self.tipo_factor = tipo_factor
        self.tasa_cuota = tasa_cuota
        self.importe = impuesto
        self.trasladado = {
            '@Base': self.base,
            '@Impuesto': self.impuesto,
            '@TipoFactor': self.tipo_factor,
            '@TasaOCuota': self.tasa_cuota,
            '@Importe': self.importe
        }

    def get_trasladado(self):
        return self.trasladado

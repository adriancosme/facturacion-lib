class CfdiRentencion:

    retencion = {}

    def __init__(self):
        self.base = None
        self.impuesto = None
        self.tipo_factor = None
        self.tasa_cuota = None
        self.importe = None

    def set_base(self, base):
        self.base = base
        self.retencion['cfdi:Retencion'].update(
            {'@Base': self.base})

    def set_impuesto(self, impuesto):
        self.impuesto = impuesto
        self.retencion['cfdi:Retencion'].update(
            {'@Impuesto': self.impuesto})

    def set_tipo_factor(self, tipo_factor):
        self.tipo_factor = tipo_factor
        self.retencion['cfdi:Retencion'].update(
            {'@TipoFactor': self.tipo_factor})

    def set_tasa_cuota(self, tasa_cuota):
        self.tasa_cuota = tasa_cuota
        self.retencion['cfdi:Retencion'].update(
            {'@TasaOCuota': self.tasa_cuota})

    def set_importe(self, importe):
        self.importe = importe
        self.retencion['cfdi:Retencion'].update(
            {'@Importe': self.importe})

    def get_retencion(self):
        return self.retencion

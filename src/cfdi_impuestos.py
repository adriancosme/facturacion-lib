class CfdiImpuestos:
    impuestos = {}

    def __init__(self):
        self.cfdi_trasladados = None
        self.cfdi_retenciones = None

    def set_trasladados(self, trasladados):
        self.cfdi_trasladados = trasladados

    def set_retenciones(self, retenciones):
        self.cfdi_retenciones = retenciones

    def get_impuesto(self):
        return self.impuestos

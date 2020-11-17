class CfdiImpuestos:
    impuestos = {}

    def __init__(self):
        self.total_impuestos_retenidos = '',
        self.total_impuestos_trasladados = ''
        self.cfdi_traslados = ''
        self.cfdi_retenciones = ''

    def set_traslados(self, trasladados):
        self.cfdi_traslados = trasladados
        self.impuestos.update(
            {'cfdi:Traslados': {'cfdi:Traslado': self.cfdi_traslados}})

    def set_retenciones(self, retenciones):
        self.cfdi_retenciones = retenciones
        self.impuestos.update(
            {'cfdi:Retenciones': {'cfdi:Retencion': self.cfdi_traslados}})

    def set_total_tmpuestos_retenidos(self, total_retenidos):
        self.total_impuestos_retenidos = total_retenidos
        if self.total_impuestos_retenidos:
            self.impuestos.update(
                {'@TotalImpuestosRetenidos': self.total_impuestos_retenidos})

    def set_total_impuestos_trasladados(self, total_trasladados):
        self.total_impuestos_trasladados = total_trasladados
        if self.total_impuestos_trasladados:
            self.impuestos.update(
                {'@TotalImpuestosTrasladados': self.total_impuestos_trasladados})

    def get_impuesto(self):
        return self.impuestos

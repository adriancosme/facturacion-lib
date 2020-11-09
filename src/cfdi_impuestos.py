class CfdiImpuestos:
    impuesto = {
        '@TotalImpuestosRetenidos': '99',
        '@TotalImpuestosTrasladados': 'as',
        'cfdi:Traslados': {
            'cfdi:Traslado': [{}, {}]
        },
        'cfdi:Retenciones': {
            'cfdi:Retencion': [{}, {}]
        }
    }

    def __init__(self):
        self.cfdi_trasladados = None
        self.cfdi_retenciones = None

    def getImpuesto(self):
        return self.impuesto

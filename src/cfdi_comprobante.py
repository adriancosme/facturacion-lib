class CfdiComprobante:

    def __init__(self, version, fecha, sello, no_certificado, certificado, sub_total, moneda, total, tipo_comprobante, lugar_expedicion):
        self.xmlns = ''
        self.schema_location = []
        self.version = version
        self.serie = ''
        self.folio = ''
        self.fecha = fecha
        self.sello = sello
        self.forma_pago = ''
        self.no_certificado = no_certificado
        self.certificado = certificado
        self.condiciones_pago = ''
        self.sub_total = sub_total
        self.descuento = ''
        self.moneda = moneda
        self.tipo_cambio = ''
        self.total = total
        self.tipo_comprobante = tipo_comprobante
        self.metodo_pago = ''
        self.lugar_expedicion = lugar_expedicion
        self.confirmacion = ''
        self.cfdi_relacionados = ''
        self.cfdi_emisor = ''
        self.cfdi_receptor = ''
        self.cfdi_conceptos = []
        self.cfdi_impuestos = []
        self.cfdi_complemento = []
        self.addenda = ''

    def emisor(self, emisor):
        self.cfdi_emisor = emisor

    def receptor(self, receptor):
        self.cfdi_receptor = receptor

    def add_complemento(self, complemento):
        self.cfdi_complemento.append(complemento)

    def add_schema_location(self, schema):
        self.schema_location.append(schema)

    def comprobante_dict(self):
        return {
            'cfdi:Comprobante': {
                '@xmlns': self.xmlns
            }
        }

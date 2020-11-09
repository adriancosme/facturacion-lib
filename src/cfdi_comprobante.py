import json


class CfdiComprobante:
    concepts = []
    impuestos = {}

    def __init__(self, version, fecha, sello, no_certificado, certificado, sub_total, moneda, total, tipo_comprobante,
                 lugar_expedicion):
        self.xmlns = ['http://www.sat.gob.mx/cfd/3', 'http://www.w3.org/2001/XMLSchema-instance']
        self.schema_location = ['http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd']
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

    def concepto(self, concept):
        self.concepts.append(concept.getConcept())

    def imp(self, tax):
        print(tax.getImpuesto())
        self.impuestos.update(tax.getImpuesto())

    def comprobante_dict(self):
        print(self.concepts)
        return {
            'cfdi:Comprobante': {
                '@xmlns:xsi': self.xmlns[0],
                '@xmlns:cfdi': self.xmlns[1],
                '@xsi:schemaLocation': self.schema_location[0],
                'cfdi:CfdiRelacionados': self.cfdi_relacionados,
                'cfdi:Emisor': self.cfdi_emisor,
                'cfdi:Receptor': self.cfdi_receptor,
                'cfdi:Conceptos': self.cfdi_conceptos,
                'cfdi:Impuestos': self.cfdi_impuestos
            }
        }

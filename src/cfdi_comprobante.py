import json


class CfdiComprobante:
    concepts = []
    impuestos = {}

    def __init__(self, version, fecha, sello, no_certificado, certificado, sub_total, moneda, total, tipo_comprobante,
                 lugar_expedicion):
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

    def concepto(self, concept):
        self.concepts.append(concept.getConcept())

    def imp(self, tax):
        print(tax.getImpuesto())
        self.impuestos.update(tax.getImpuesto())

    def comprobante_dict(self):
        print(self.concepts)
        return {
            'cfdi:Comprobante': {
                '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
                '@xmlns:cfdi': 'http://www.sat.gob.mx/cfd/3',
                '@xsi:schemaLocation': 'http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd',
                'cfdi:Conceptos': {
                    'cfdi:Concepto': self.concepts
                },
                'cfdi:Impuestos': self.impuestos
            }
        }

import pkg_resources
from lxml import etree as ET
from xmltodict import parse


class CfdiComprobante:
    comprobante = {'cfdi:Comprobante': {
    }}
    concepts = []

    def __init__(self, version, fecha, sello, no_certificado, certificado, sub_total, moneda, total, tipo_comprobante,
                 lugar_expedicion):
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
        self.cfdi_impuestos = ''
        self.cfdi_complemento = []
        self.addenda = ''

    def add_xmlns(self, prefix, value):
        if prefix is 'xsi':
            self.comprobante['cfdi:Comprobante'].update(
                {'@xmlns:xsi': value})
        elif prefix is 'cfdi':
            self.comprobante['cfdi:Comprobante'].update(
                {'@xmlns:cfdi': value})
        else:
            raise Exception('Sin namespace')

    def add_schema_location(self, value):
        self.comprobante['cfdi:Comprobante'].update(
            {'@xsi:schemaLocation': value})

    def set_attr(self):
        if self.version:
            self.comprobante['cfdi:Comprobante'].update(
                {'@Version': self.version})
        else:
            raise Exception('El atributo version es requerido')
        if self.serie:
            self.comprobante['cfdi:Comprobante'].update(
                {'@Serie': self.serie})
        if self.folio:
            self.comprobante['cfdi:Comprobante'].update(
                {'@Folio': self.folio})
        if self.fecha:
            self.comprobante['cfdi:Comprobante'].update(
                {'@Fecha': self.fecha})
        else:
            raise Exception('El atributo fecha es requerido')
        if self.sello:
            self.comprobante['cfdi:Comprobante'].update(
                {'@Sello': self.sello})
        else:
            raise Exception('El atributo sello es requerido')
        if self.forma_pago:
            self.comprobante['cfdi:Comprobante'].update(
                {'@FormaPago': self.forma_pago})
        if self.no_certificado:
            self.comprobante['cfdi:Comprobante'].update(
                {'@NoCertificado': self.no_certificado})
        else:
            raise Exception('El atributo certificado es requerido')
        if self.certificado:
            self.comprobante['cfdi:Comprobante'].update(
                {'@Certificado': self.certificado})
        else:
            raise Exception('El atributo certificado es requerido')
        if self.condiciones_pago:
            self.comprobante['cfdi:Comprobante'].update(
                {'@CondicionesDePago': self.condiciones_pago})
        if self.sub_total:
            self.comprobante['cfdi:Comprobante'].update(
                {'@SubTotal': self.sub_total})
        else:
            raise Exception('El atributo subtotal es requerido')
        if self.descuento:
            self.comprobante['cfdi:Comprobante'].update(
                {'@Descuento': self.descuento})
        if self.moneda:
            self.comprobante['cfdi:Comprobante'].update(
                {'@Moneda': self.moneda})
        else:
            raise Exception('El atributo subtotal es requerido')
        if self.tipo_cambio:
            self.comprobante['cfdi:Comprobante'].update(
                {'@TipoCambio': self.tipo_cambio})
        if self.total:
            self.comprobante['cfdi:Comprobante'].update(
                {'@Total': self.total})
        else:
            raise Exception('El atributo total es requerido')
        if self.tipo_comprobante:
            self.comprobante['cfdi:Comprobante'].update(
                {'@TipoDeComprobante': self.tipo_comprobante})
        else:
            raise Exception('El atributo total es requerido')
        if self.metodo_pago:
            self.comprobante['cfdi:Comprobante'].update(
                {'@MetodoPago': self.metodo_pago})
        if self.lugar_expedicion:
            self.comprobante['cfdi:Comprobante'].update(
                {'@LugarExpedicion': self.lugar_expedicion})
        if self.confirmacion:
            self.comprobante['cfdi:Comprobante'].update(
                {'@Confirmacion': self.confirmacion})

    def set_sello(self, sello):
        self.sello = sello
        self.comprobante['cfdi:Comprobante'].update(
            {'@Sello': self.sello})

    def set_no_certificado(self, no_certificado):
        self.no_certificado = no_certificado
        self.comprobante['cfdi:Comprobante'].update(
            {'@NoCertificado': self.no_certificado})

    def set_certificado(self, certificado):
        self.certificado = certificado
        self.comprobante['cfdi:Comprobante'].update(
            {'@Certificado': self.certificado})

    def set_serie(self):
        self.comprobante['cfdi:Comprobante'].update(
            {'@Serie': self.serie})

    def emisor(self, emisor):
        self.cfdi_emisor = emisor
        self.comprobante['cfdi:Comprobante'].update(
            {'cfdi:Emisor': self.cfdi_emisor})

    def receptor(self, receptor):
        self.cfdi_receptor = receptor
        self.comprobante['cfdi:Comprobante'].update(
            {'cfdi:Receptor': self.cfdi_receptor})

    def add_complemento(self, complemento):
        self.cfdi_complemento.append(complemento)

    def concepto(self, concept):
        self.concepts.append(concept.getConcept())
        self.comprobante['cfdi:Comprobante'].update(
            {'cfdi:Conceptos': {'cfdi:Concepto': self.concepts}})

    def impuesto(self, impuesto):
        self.cfdi_impuestos = impuesto
        self.comprobante['cfdi:Comprobante'].update(
            {'cfdi:Impuestos': self.cfdi_impuestos})

    def generate_cadena_original(self, xml):
        xlst_file = pkg_resources.resource_filename(
            __name__, 'resources/cadenaoriginal_3_3.xslt')
        dom = ET.fromstring(xml)
        xslt = ET.parse(xlst_file)
        transform = ET.XSLT(xslt)
        return str(transform(dom))

    def comprobante_dict(self):
        return self.comprobante

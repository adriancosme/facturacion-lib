import Comprobante
import Emisor
import Receptor
import Concepto
from jinja2 import Template
import pkg_resources
import lxml.etree as ET


class Cfdi:
    def __init__(self, Comprobante):
        self.__comprobante = Comprobante
        self.__xml = {'comprobante': {
            'version': self.__comprobante.version,
            'serie': self.__comprobante.serie,
            'folio': self.__comprobante.folio,
            'fecha': self.__comprobante.fecha,
            'forma_pago': self.__comprobante.forma_pago,
            'no_certificado': self.__comprobante.no_certificado,
            'condiciones_pago': self.__comprobante.condiciones_pago,
            'sub_total': self.__comprobante.sub_total,
            'descuento': self.__comprobante.descuento,
            'moneda': self.__comprobante.moneda,
            'total': self.__comprobante.total,
            'tipo_comprobante': self.__comprobante.tipo_comprobante,
            'metodo_pago': self.__comprobante.metodo_pago,
            'lugar_expedicion': self.__comprobante.lugar_expedicion
        },
            'emisor': {
                'rfc': '',
                'nombre': '',
                'regimen_fiscal': ''
        },
            'receptor': {'rfc': '', 'nombre': '', 'regimen_fiscal': ''},
            'conceptos': [],
            'impuestos': {}}

    def emisor(self, emisor):
        self.__xml.update({'emisor': {
                          'rfc': emisor.rfc, 'nombre': emisor.nombre, 'regimen_fiscal': emisor.regimen_fiscal}})

    def receptor(self, receptor):
        self.__xml.update({'receptor': {
                          'rfc': receptor.rfc, 'nombre': receptor.nombre, 'uso_cfdi': receptor.uso_cfdi}})

    def concepto(self, conceptos):
        self.__xml['conceptos'].append(conceptos)

    def get_cfdi(self):
        jinja_file = pkg_resources.resource_filename(
            __name__, 'resources/cfdi.jinja')
        with open(jinja_file, 'r') as template:
            jinja_tmpl_str = template.read()      
        tmpl = Template(jinja_tmpl_str)
        self.xml = tmpl.render(data=self.__xml).encode('utf-8')
        xml_obj = ET.parse(self.xml)
        print(xml_obj)

    def get_cadena_original(self, xml):
        xlst_file = pkg_resources.resource_filename(
            __name__, 'resources/cadenaoriginal_3_3.xslt')
        dom = ET.fromstring(xml)
        xslt = ET.parse(xlst_file)
        transform = ET.XSLT(xslt)
        return str(transform(dom))

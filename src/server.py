from flask import Flask
from flask import Response

from src.cfdi_impuestos import CfdiImpuestos
from src.cfdi_comprobante import CfdiComprobante
from src.cfdi_concepto import CfdiConcepto
from src.cfdi_emisor import CfdiEmisor
from src.cfdi_receptor import CfdiReceptor
import xmltodict
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    comprobante = CfdiComprobante('3.3', '2014-07-08T12:16:50', 'asd', 'asd', 'asd', 16148.04, 'MXN', 17207.35, 'I',
                                  'Mexico')
    comprobante.add_xmlns('xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    comprobante.add_xmlns('cfdi', 'http://www.sat.gob.mx/cfd/3')
    comprobante.add_schema_location(
        'http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd')
    comprobante.serie = 'I'
    comprobante.folio = 'ACACUN-27'
    comprobante.forma_pago = 'Pago en una sola exhibición'
    comprobante.condiciones_pago = 'Contado'
    comprobante.descuento = '645.92'
    comprobante.metodo_pago = 'En efectivo'
    comprobante.set_attr()

    emisor = CfdiEmisor()
    emisor.set_rfc('XAXX010101000')
    emisor.set_nombre('nombre')
    emisor.set_regimen_fiscal('601')
    receptor = CfdiReceptor()
    receptor.set_rfc('XAXX010101000')
    receptor.set_uso_cfdi('G01')
    comprobante.emisor(emisor.emisor_dict())
    comprobante.receptor(receptor.receptor_dict())

    dictComprobante = comprobante.comprobante_dict()
    concepto = CfdiConcepto({
        "ClaveProdServ": 'ClaveProdServ',
        "NoIdentificacion": 'NoIdentificacion',
        "Cantidad": 'cantidad',
        "ClaveUnidad": 'ClaveUnidad',
        "Unidad": 'Unidad',
        "Descripcion": 'Descripcion',
        "ValorUnitario": 'ValorUnitario',
        "Importe": 'Importe',
        "Descuento": 'Descuento',
    })
    comprobante.concepto(concepto)
    impues = CfdiImpuestos()
    # print(impues.getImpuesto())
    comprobante.impuesto(impues.get_impuesto)
    xml = xmltodict.unparse(dictComprobante, pretty=True)
    return Response(xml, mimetype='text/xml')

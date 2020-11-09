from flask import Flask
from flask import Response

from src.cfdi_impuestos import CfdiImpuestos
from src.cfdi_comprobante import CfdiComprobante
from src.cfdi_concepto import CfdiConcepto
import xmltodict
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    comprobante = CfdiComprobante('3.3', '2014-07-08T12:16:50', 'asd', 'asd', 'asd', 16148.04, 'MXN', 17207.35, 'I',
                                  'Mexico')
    comprobante.folio = 'ACACUN-27'
    comprobante.forma_pago = 'Pago en una sola exhibición'
    comprobante.condiciones_pago = 'Contado'
    comprobante.descuento = '645.92'
    comprobante.metodo_pago = 'En efectivo'

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
    #print(impues.getImpuesto())
    comprobante.imp(impues)
    xml = xmltodict.unparse(dictComprobante, pretty=True)
    print(xmltodict.unparse(dictComprobante, pretty=True))
    return Response(xml, mimetype='text/xml')

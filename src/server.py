import base64
from flask import Flask
from flask import Response
import pkg_resources
from src.cfdi_impuestos import CfdiImpuestos
from src.cfdi_comprobante import CfdiComprobante
from src.cfdi_concepto import CfdiConcepto
from src.cfdi_emisor import CfdiEmisor
from src.cfdi_receptor import CfdiReceptor
from src.cfdi_trasladado import CfdiTrasladado
from src.cfdi_retencion import CfdiRentencion
from datetime import datetime
from src.openssl import Openssl
from pathlib import Path
import xmltodict

app = Flask(__name__)
app.debug = True

certificate = open('src/resources/certs/CSD/30001000000400002336.cer', 'rb')
cer = base64.b64encode(certificate.read())
key_file = open(
    'src/resources/certs/CSD/CSD_BERENICE_XIMO_QUEZADA_XIQB891116QE4_20190528_180213.key', 'rb')
key = base64.b64encode(key_file.read())
pwd = '12345678a'


@app.route('/')
def main():
    comprobante = CfdiComprobante('3.3', str(datetime.now().isoformat())[:19], 'asf', 'asf', 'asf', 16148.04, 'MXN', 17207.35, 'I',
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
    impues_concepto = CfdiImpuestos()
    concepto_traslado = CfdiTrasladado(
        '2250000', '002', 'Tasa', '0.160000', '360000')
    concepto_retenciones = CfdiRentencion(
        '2250000', '002', 'Tasa', '0.160000', '360000')
    impues_concepto.set_traslados(concepto_traslado.get_trasladado())
    impues_concepto.set_retenciones(concepto_retenciones.get_retencion())
    concepto.impuestos(impues_concepto.get_impuesto())
    comprobante.concepto(concepto)
    comprobante.concepto(concepto)
    impues = CfdiImpuestos()
    traslado = CfdiTrasladado('2250000', '002', 'Tasa', '0.160000', '360000')
    retenciones = CfdiRentencion(
        '2250000', '002', 'Tasa', '0.160000', '360000')        
    impues.set_traslados(traslado.get_trasladado())
    impues.set_retenciones(retenciones.get_retencion())
    impues.set_total_impuestos_trasladados('12512')
    impues.set_total_tmpuestos_retenidos('2151251')
    comprobante.impuesto(impues.get_impuesto())
    openssl = Openssl()
    no_cert = openssl.get_no_cert(cer)
    xml = xmltodict.unparse(dictComprobante)
    cadena = pkg_resources.resource_filename(
        __name__, 'resources/cadenaoriginal_3_3.xslt')
    sello = openssl.get_sello(key, pwd, xml, cadena)
    comprobante.set_no_certificado(no_cert)
    comprobante.set_sello(str(sello).replace("b'", ""))
    comprobante.set_certificado(str(cer).replace("b'", ""))
    xml = xmltodict.unparse(dictComprobante)
    return Response(xml, mimetype='text/xml')


if __name__ == '__main__':
    app.run(host='0.0.0.0')

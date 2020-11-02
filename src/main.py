from cfdi_comprobante import CfdiComprobante
from cfdi_emisor import CfdiEmisor
from cfdi_receptor import CfdiReceptor
from xmler import dict2xml
comprobante = CfdiComprobante('3.3','2014-07-08T12:16:50', 'asd', 'asd', 'asd', 16148.04, 'MXN', 17207.35, 'I', 'Mexico')
comprobante.folio = 'ACACUN-27'
comprobante.forma_pago = 'Pago en una sola exhibición'
comprobante.condiciones_pago = 'Contado'
comprobante.descuento = '645.92'
comprobante.metodo_pago = 'En efectivo'

emisor = CfdiEmisor('XAXX010101000', '601')
receptor = CfdiReceptor('XAXX010101000', 'G01')

comprobante.emisor(emisor)
comprobante.receptor(receptor)

result = comprobante.print_xml()
print(result)
dict2xml(result)


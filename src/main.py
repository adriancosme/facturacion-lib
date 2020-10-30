from Cfdi import Cfdi
from Comprobante import Comprobante
from Emisor import Emisor
from Receptor import Receptor
from Concepto import Concepto
import dictfier

comprobante = Comprobante()
comprobante.version = '3.3'
comprobante.serie = 'E'
comprobante.folio = 'ACACUN-27'
comprobante.fecha = '2014-07-08T12:16:50'
comprobante.forma_pago = 'Pago en una sola exhibición'
comprobante.condiciones_pago = 'Contado'
comprobante.sub_total = '16148.04'
comprobante.descuento = '645.92'
comprobante.moneda = 'MXN'
comprobante.total = '17207.35'
comprobante.tipo_comprobante = 'I'
comprobante.metodo_pago = 'En efectivo'
comprobante.lugar_expedicion = 'Mexico'
cfd = Cfdi(comprobante)

emisor = Emisor('XAXX010101000', 'EMPRESA SA DE CV', '601')
receptor = Receptor('XAXX010101000', 'PUBLICO EN GENERAL', 'G01')
concepto = Concepto('1', 'S10', '1.0', 'P', 'Pieza',
                    'Descripcion', '12.0', '12.0', '0.0')
cfd.emisor(emisor)
cfd.receptor(receptor)
cfd.concepto(concepto)
cfd.get_cfdi()

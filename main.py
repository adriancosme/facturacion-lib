from sys import version
from sample import Comprobante, EmisorType

comprobante = Comprobante()
emisor = EmisorType()
emisor.set_Rfc('XAXX010101000')
emisor.set_RegimenFiscal('601')
comprobante.set_Emisor(emisor)
with open('outfile.xml', 'wt') as xmlfile:
    comprobante.export(outfile=xmlfile, level=0)
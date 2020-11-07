import json


class CfdiConcepto:
    concepto = {
        '@ClaveProdServ': '',
        # '@NoIdentificacion': '',
        '@Cantidad': '',
        '@ClaveUnidad': '',
        # '@Unidad': '',
        '@Descripcion': '',
        '@ValorUnitario': '',
        '@Importe': '',
        # '@Descuento': '',
    }
    existComplemnt = False;

    def __init__(self, object):
        object = json.loads(object)
        if object['ClaveProdServ']:
            self.concepto.update({'@ClaveProdServ': object['ClaveProdServ']})
        else:
            raise Exception("Must include ClaveProdServ in object ")
        if object['Cantidad']:
            self.concepto.update({'@Cantidad': object['Cantidad']})
        else:
            raise Exception("Must include Cantidad in object ")

        if object['ClaveUnidad']:
            self.concepto.update({'@ClaveUnidad': object['ClaveUnidad']})
        else:
            raise Exception("Must include ClaveUnidad in object")

        if object['Descripcion']:
            self.concepto.update({'@Descripcion': object['Descripcion']})
        else:
            raise Exception("Must include Descripcion in object ")

        if object['ValorUnitario']:
            self.concepto.update({'@ValorUnitario': object['ValorUnitario']})
        else:
            raise Exception("Must include ValorUnitario in object ")

        if object['Importe']:
            self.concepto.update({'@Importe': object['Importe']})
        else:
            raise Exception("Must include Importe in object ")

        self.cfdi_impuestos = None
        self.cfdi_info_aduanera = None
        self.cfdi_cuenta_predial = None
        self.cfdi_complemento_concepto = None
        self.cfdi_parte = None

    def complemento(self, data):
        return ''

    def traslado(self, dtraslado):
        return ''

    def retencion(self, retencion):
        return ''

    def getConcept(self):
        return self.concepto

    def isComplement(self):
        return self.existComplemnt;

    def getComplementProperties(self):
        return ''

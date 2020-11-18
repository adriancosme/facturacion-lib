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
    existComplemnt = False

    def __init__(self, object):
        # print(object)
        # object = json.loads(object)
        if 'ClaveProdServ' in object:
            self.concepto.update(
                {'@ClaveProdServ': object.get('ClaveProdServ')})
        else:
            raise Exception("Must include ClaveProdServ in object ")

        if 'NoIdentificacion' in object:
            self.concepto.update(
                {'@NoIdentificacion': object.get('NoIdentificacion')})

        if 'Cantidad' in object:
            self.concepto.update({'@Cantidad': object.get('Cantidad')})
        else:
            raise Exception("Must include Cantidad in object ")

        if 'ClaveUnidad' in object:
            self.concepto.update({'@ClaveUnidad': object.get('ClaveUnidad')})
        else:
            raise Exception("Must include ClaveUnidad in object")

        if 'Unidad' in object:
            self.concepto.update({'@Unidad': object.get('Unidad')})

        if 'Descripcion' in object:
            self.concepto.update({'@Descripcion': object.get('Descripcion')})
        else:
            raise Exception("Must include Descripcion in object ")

        if 'ValorUnitario' in object:
            self.concepto.update(
                {'@ValorUnitario': object.get('ValorUnitario')})
        else:
            raise Exception("Must include ValorUnitario in object ")

        if 'Importe' in object:
            self.concepto.update({'@Importe': object.get('Importe')})
        else:
            raise Exception("Must include Importe in object ")

        if 'Descuento' in object:
            self.concepto.update({'@Descuento': object.get('Descuento')})

        self.cfdi_impuestos = None
        self.cfdi_info_aduanera = None
        self.cfdi_cuenta_predial = None
        self.cfdi_complemento_concepto = None
        self.cfdi_parte = None

    def complemento(self, data):
        return ''

    def impuestos(self, impuestos):
        self.cfdi_impuestos = impuestos
        self.concepto.update({'cfdi:Impuestos': self.cfdi_impuestos})

    def getConcept(self):
        return self.concepto

    def isComplement(self):
        return self.existComplemnt

    def getComplementProperties(self):
        return ''

class CfdiEmisor:
    emisor = {}

    def __init__(self):
        self.rfc = ''
        self.nombre = ''
        self.regimen_fiscal = ''

    def set_rfc(self, rfc):
        self.rfc = rfc
        self.emisor.update({'@Rfc': self.rfc})

    def set_nombre(self, nombre):
        self.nombre = nombre
        self.emisor.update({'@Nombre': self.nombre})

    def set_regimen_fiscal(self, regimen_fiscal):
        self.regimen_fiscal = regimen_fiscal
        self.emisor.update({'@RegimenFiscal': self.regimen_fiscal})

    def emisor_dict(self):
        return self.emisor

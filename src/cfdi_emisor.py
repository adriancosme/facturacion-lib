class CfdiEmisor:
    def __init__(self, rfc, regimen_fiscal):
        self.emisor = []
        self.rfc = rfc
        self.nombre = None
        self.regimen_fiscal = regimen_fiscal

    def set_nombre(self, nombre):
        self.nombre = nombre

    def parse_dict_from(self, lst):
        return {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}

    def emisor_dict(self):
        return {
            '@Rfc': self.rfc,            
            '@RegimenFiscal': self.regimen_fiscal
        }

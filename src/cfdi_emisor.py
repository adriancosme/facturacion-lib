class CfdiEmisor:
    def __init__(self, rfc, regimen_fiscal):
        self.rfc = rfc
        self.nombre = None
        self.regimen_fiscal = regimen_fiscal

    def set_nombre(self, nombre):
        self.nombre = nombre

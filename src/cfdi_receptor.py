class CfdiReceptor:
    receptor = {}

    def __init__(self):
        self.rfc = None
        self.nombre = None
        self.residencia_fiscal = None
        self.num_reg_id_trib = None
        self.uso_cfdi = None

    def set_rfc(self, rfc):
        self.rfc = rfc
        self.receptor.update({'@Rfc': self.rfc})

    def set_nombre(self, nombre):
        self.nombre = nombre
        self.receptor.update({'@Nombre': self.nombre})

    def set_residencia_fiscal(self, residencia_fiscal):
        self.residencia_fiscal = residencia_fiscal
        self.receptor.update({'@ResidenciaFiscal': self.residencia_fiscal})

    def set_num_reg_id_trib(self, num_reg_id_trib):
        self.num_reg_id_trib = num_reg_id_trib
        self.receptor.update({'@NumRegIdTrib': self.num_reg_id_trib})

    def set_uso_cfdi(self, uso_cfdi):
        self.uso_cfdi = uso_cfdi
        self.receptor.update({'@UsoCFDI': self.uso_cfdi})

    def receptor_dict(self):
        return self.receptor

class CfdiReceptor:
    def __init__(self, rfc, uso_cfdi):
        self.rfc = rfc
        self.nombre = None
        self.residencia_fiscal = None
        self.num_reg_id_trib = None
        self.uso_cfdi = uso_cfdi

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_residencia_fiscal(self, residencia_fiscal):
        self.residencia_fiscal = residencia_fiscal
    
    def set_num_reg_id_trib(self, num_reg_id_trib):
        self.num_reg_id_trib = num_reg_id_trib

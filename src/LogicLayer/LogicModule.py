from LogicLayer.BeneficiarySourceType.service import BeneficiarySourceTypeService
from LogicLayer.BeneficiarySource.service import BeneficiarySourceService
class LogicModule:
    def __init__(self):
        self.beneficiarySourceTypeService = BeneficiarySourceTypeService();

        self.beneficiarySource = BeneficiarySourceService()
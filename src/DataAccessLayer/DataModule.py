from DataAccessLayer.FundingSource.repository import FundingSourceRepository
from DataAccessLayer.FundingSource.model import FundingSource
from DataAccessLayer.FundingSourceType.repository import FundingSourceTypeRepository
from DataAccessLayer.FundingSourceType.model import FundingSourceType
from DataAccessLayer.FundingSourceProperty.repository import FundingSourcePropertyRepository
from DataAccessLayer.FundingSourceProperty.model import FundingSourceProperty
from DataAccessLayer.Funding.model import Funding
from DataAccessLayer.Funding.repository import FundingRepository
from DataAccessLayer.FundingGroupType.model import FundingGroupType
from DataAccessLayer.FundingGroupType.repository import FundingGroupTypeRepository
from DataAccessLayer.FundingGroup.model import FundingGroup
from DataAccessLayer.FundingGroup.repository import FundingGroupRepository
from DataAccessLayer.User.model import User
from DataAccessLayer.User.repository import UserRepository
from DataAccessLayer.Issuer.model import Issuer
from DataAccessLayer.Issuer.repository import IssuerRepository
from DataAccessLayer.Role.repository import RoleRepository
from DataAccessLayer.Role.model import Role
from DataAccessLayer.BeneficiarySourceType.repository import BeneficiarySourceTypeRepository
from DataAccessLayer.BeneficiarySourceType.model import BeneficiarySourceType


class DataModule:

    def __init__(self):
        self.fundingSourceRepository = FundingSourceRepository(FundingSource)

        self.fundingSourceTypeRepository = FundingSourceTypeRepository(FundingSourceType)

        self.fundingSourcePropertyRepository = FundingSourcePropertyRepository(FundingSourceProperty)

        self.fundingRepository = FundingRepository(Funding)

        self.fundingGroupRepository = FundingGroupRepository(FundingGroup)

        self.fundingGroupTypeRepository = FundingGroupTypeRepository(FundingGroupType)

        self.userRepository = UserRepository(User)

        self.issuerRepository = IssuerRepository(Issuer)

        self.roleRepository = RoleRepository(Role)
        
        self.beneficiarySourceTypeRepository = BeneficiarySourceTypeRepository(BeneficiarySourceType)

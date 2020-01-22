from DataAccessLayer.FundingSource.repository import FundingSourceRepository
from DataAccessLayer.FundingSource.model import FundingSource
from DataAccessLayer.FundingSourceType.repository import FundingSourceTypeRepository
from DataAccessLayer.FundingSourceType.model import FundingSourceType
from DataAccessLayer.FundingSourceProperty.repository import FundingSourcePropertyRepository
from DataAccessLayer.FundingSourceProperty.model import FundingSourceProperty
from DataAccessLayer.User.model import User
from DataAccessLayer.User.repository import UserRepository
from DataAccessLayer.Issuer.model import Issuer
from DataAccessLayer.Issuer.repository import IssuerRepository
from DataAccessLayer.Role.repository import RoleRepository
from DataAccessLayer.Role.model import Role


class DataModule:

    def __init__(self):
        self.fundingSourceRepository = FundingSourceRepository(FundingSource)

        self.fundingSourceTypeRepository = FundingSourceTypeRepository(FundingSourceType)

        self.fundingSourcePropertyRepository = FundingSourcePropertyRepository(FundingSourceProperty)

        self.userRepository = UserRepository(User)

        self.issuerRepository = IssuerRepository(Issuer)

        self.roleRepository = RoleRepository(Role)

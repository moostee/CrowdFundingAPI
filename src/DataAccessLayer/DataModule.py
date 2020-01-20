from DataAccessLayer.FundingSource.repository import FundingSourceRepository
from DataAccessLayer.FundingSource.model import FundingSource
from DataAccessLayer.FundingSourceType.repository import FundingSourceTypeRepository
from DataAccessLayer.FundingSourceType.model import FundingSourceType
from DataAccessLayer.FundingSourceProperty.repository import FundingSourcePropertyRepository
from DataAccessLayer.FundingSourceProperty.model import FundingSourceProperty


class DataModule:

    def  __init__(self):

      self.fundingSourceRepository = FundingSourceRepository(FundingSource)

      self.fundingSourceTypeRepository = FundingSourceTypeRepository(FundingSourceType)

      self.fundingSourcePropertyRepository = FundingSourcePropertyRepository(FundingSourceProperty)

    

    
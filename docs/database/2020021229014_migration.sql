-- Remove field issuer from fundingsource
--
SET CONSTRAINTS "DataAccessLayer_fund_issuer_id_fe5db4af_fk_DataAcces" IMMEDIATE; ALTER TABLE "DataAccessLayer_fundingsource" DROP CONSTRAINT "DataAccessLayer_fund_issuer_id_fe5db4af_fk_DataAcces";
ALTER TABLE "DataAccessLayer_fundingsource" DROP COLUMN "issuer_id" CASCADE;
--
-- Alter field defaultCycleDuration on fundinggrouptype
--
ALTER TABLE "DataAccessLayer_fundinggrouptype" ALTER COLUMN "defaultCycleDuration" TYPE varchar(4), ALTER COLUMN "defaultCycleDuration" DROP NOT NULL;  
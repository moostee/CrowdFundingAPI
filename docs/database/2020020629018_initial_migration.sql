--
-- Create model Role
--
CREATE TABLE "DataAccessLayer_role" ("createdAt" timestamp with time zone NOT NULL, "updatedAt" timestamp with time zone NOT NULL, "isDeleted" boolean NOT NULL, "id" uuid NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL UNIQUE);

--
-- Create model Issuer
--
CREATE TABLE "DataAccessLayer_issuer" ("createdAt" timestamp with time zone NOT NULL, "updatedAt" timestamp with time zone NOT NULL, "isDeleted" boolean NOT NULL, "id" uuid NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL UNIQUE, "referenceTypeMaxChar" smallint NOT NULL CHECK ("referenceTypeMaxChar" >= 0), "referenceType" varchar(32) NOT NULL);

--
-- Create model User
--
CREATE TABLE "DataAccessLayer_user" ("createdAt" timestamp with time zone NOT NULL, "updatedAt" timestamp with time zone NOT NULL, "isDeleted" boolean NOT NULL, "id" uuid NOT NULL PRIMARY KEY, "userId" uuid NOT NULL, "firstName" varchar(100) NOT NULL, "lastName" varchar(100) NOT NULL, "phoneNumber" varchar(100) NOT NULL UNIQUE);

--
-- Create model FundingGroupType
--
CREATE TABLE "DataAccessLayer_fundinggrouptype" ("createdAt" timestamp with time zone NOT NULL, "updatedAt" timestamp with time zone NOT NULL, "isDeleted" boolean NOT NULL, "id" uuid NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL UNIQUE, "hasFixedIndividualAmount" boolean NOT NULL, "hasFixedGroupAmount" boolean NOT NULL, "hasMaturityDate" boolean NOT NULL, "maxUser" smallint NOT NULL CHECK ("maxUser" >= 0), "minUser" smallint NOT NULL CHECK ("minUser" >= 0), "isAutomatedCycle" boolean NOT NULL, "defaultCycleDuration" varchar(10) NOT NULL, "hasRollingBeneficiary" boolean NOT NULL, "hasFixedDefaultCycle" boolean NOT NULL, "canJoinClosedGroup" boolean NOT NULL, "description" varchar(256) NOT NULL, "config" jsonb NOT NULL);

--
-- Create model FundingGroup
--
CREATE TABLE "DataAccessLayer_fundinggroup" ("createdAt" timestamp with time zone NOT NULL, "updatedAt" timestamp with time zone NOT NULL, "isDeleted" boolean NOT NULL, "id" uuid NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL, "totalCycles" smallint NOT NULL CHECK ("totalCycles" >= 0), "currentCycle" smallint NOT NULL CHECK ("currentCycle" >= 0), "startDate" date NOT NULL, "nextCycleDate" date NULL, "cycleDuration" varchar(10) NULL, "code" varchar(50) NOT NULL, "isClosed" boolean NOT NULL, "individualAmount" numeric(19, 2) NULL, "currency" varchar(10) NULL, "targetGroupAmount" numeric(19, 2) NULL, "targetGroupDate" date NULL, "debitBeneficiary" boolean NOT NULL, "failureAction" varchar(64) NOT NULL, "description" varchar(256) NOT NULL);

--
-- Create model FundingSourceType
--
CREATE TABLE "DataAccessLayer_fundingsourcetype" ("createdAt" timestamp with time zone NOT NULL, "updatedAt" timestamp with time zone NOT NULL, "isDeleted" boolean NOT NULL, "id" uuid NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL UNIQUE, "config" jsonb NOT NULL);

--
-- Create model BeneficiarySourceType
--
CREATE TABLE "DataAccessLayer_beneficiarysourcetype" ("createdAt" timestamp with time zone NOT NULL, "updatedAt" timestamp with time zone NOT NULL, "isDeleted" boolean NOT NULL, "id" uuid NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL UNIQUE);

--
-- Create model BeneficiarySource
--
CREATE TABLE "DataAccessLayer_beneficiarysource" ("createdAt" timestamp with time zone NOT NULL, "updatedAt" timestamp with time zone NOT NULL, "isDeleted" boolean NOT NULL, "id" uuid NOT NULL PRIMARY KEY, "destinationNumber" varchar(20) NOT NULL);

--
-- Create model BeneficiarySourceProperty
--
CREATE TABLE "DataAccessLayer_beneficiarysourceproperty" ("createdAt" timestamp with time zone NOT NULL, "updatedAt" timestamp with time zone NOT NULL, "isDeleted" boolean NOT NULL, "id" uuid NOT NULL PRIMARY KEY, "propertyType" varchar(100) NOT NULL, "propertyValue" varchar(100) NOT NULL, "beneficiarySource_id" uuid NOT NULL);

--
-- Create model FundingSource
--
CREATE TABLE "DataAccessLayer_fundingsource" ("createdAt" timestamp with time zone NOT NULL, "updatedAt" timestamp with time zone NOT NULL, "isDeleted" boolean NOT NULL, "id" uuid NOT NULL PRIMARY KEY, "sourceNumber" varchar(20) NOT NULL);

--
-- Create model FundingSourceProperty
--
CREATE TABLE "DataAccessLayer_fundingsourceproperty" ("createdAt" timestamp with time zone NOT NULL, "updatedAt" timestamp with time zone NOT NULL, "isDeleted" boolean NOT NULL, "id" uuid NOT NULL PRIMARY KEY, "propertyName" varchar(100) NOT NULL, "propertyValue" varchar(100) NOT NULL, "fundingSource_id" uuid NOT NULL);

--
-- Create model Funding
--
CREATE TABLE "DataAccessLayer_funding" ("createdAt" timestamp with time zone NOT NULL, "updatedAt" timestamp with time zone NOT NULL, "isDeleted" boolean NOT NULL, "id" uuid NOT NULL PRIMARY KEY, "cycle" smallint NOT NULL CHECK ("cycle" >= 0), "amount" numeric(19, 2) NOT NULL, "currency" varchar(50) NOT NULL, "dueDate" date NOT NULL, "status" varchar(64) NOT NULL);

--
-- Create model FundingTransaction
--
CREATE TABLE "DataAccessLayer_fundingtransaction" ("createdAt" timestamp with time zone NOT NULL, "updatedAt" timestamp with time zone NOT NULL, "isDeleted" boolean NOT NULL, "id" uuid NOT NULL PRIMARY KEY, "amount" double precision NOT NULL, "currency" varchar(100) NOT NULL, "paymentTransactionRef" varchar(255) NOT NULL, "status" varchar(100) NOT NULL, "issuerResponseCode" varchar(100) NOT NULL, "issuerPaymentReference" varchar(100) NOT NULL, "issuerRemark" varchar(255) NOT NULL, "funding_id" uuid NOT NULL, "fundingSource_id" uuid NOT NULL, "issuer_id" uuid NOT NULL, "user_id" uuid NOT NULL);

--
-- Add field fundingSourceType to fundingsource
--
ALTER TABLE "DataAccessLayer_fundingsource" ADD COLUMN "fundingSourceType_id" uuid NOT NULL CONSTRAINT "DataAccessLayer_fund_fundingSourceType_id_a801fcf2_fk_DataAcces" REFERENCES "DataAccessLayer_fundingsourcetype"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "DataAccessLayer_fund_fundingSourceType_id_a801fcf2_fk_DataAcces" IMMEDIATE;

--
-- Add field issuer to fundingsource
--
ALTER TABLE "DataAccessLayer_fundingsource" ADD COLUMN "issuer_id" uuid NOT NULL CONSTRAINT "DataAccessLayer_fund_issuer_id_fe5db4af_fk_DataAcces" REFERENCES "DataAccessLayer_issuer"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "DataAccessLayer_fund_issuer_id_fe5db4af_fk_DataAcces" IMMEDIATE;

--
-- Add field user to fundingsource
--
ALTER TABLE "DataAccessLayer_fundingsource" ADD COLUMN "user_id" uuid NOT NULL CONSTRAINT "DataAccessLayer_fund_user_id_23dfc454_fk_DataAcces" REFERENCES "DataAccessLayer_user"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "DataAccessLayer_fund_user_id_23dfc454_fk_DataAcces" IMMEDIATE;

--
-- Create model FundingGroupUser
--
CREATE TABLE "DataAccessLayer_fundinggroupuser" ("createdAt" timestamp with time zone NOT NULL, "updatedAt" timestamp with time zone NOT NULL, "isDeleted" boolean NOT NULL, "id" uuid NOT NULL PRIMARY KEY, "userSequence" smallint NOT NULL CHECK ("userSequence" >= 0), "balance" numeric(19, 2) NOT NULL, "status" varchar(64) NOT NULL, "beneficiarySource_id" uuid NOT NULL, "fundingGroup_id" uuid NOT NULL, "fundingSource_id" uuid NOT NULL, "role_id" uuid NOT NULL, "user_id" uuid NOT NULL);

--
-- Add field fundingGroupType to fundinggroup
--
ALTER TABLE "DataAccessLayer_fundinggroup" ADD COLUMN "fundingGroupType_id" uuid NOT NULL CONSTRAINT "DataAccessLayer_fund_fundingGroupType_id_72823747_fk_DataAcces" REFERENCES "DataAccessLayer_fundinggrouptype"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "DataAccessLayer_fund_fundingGroupType_id_72823747_fk_DataAcces" IMMEDIATE;

--
-- Add field initiator to fundinggroup
--
ALTER TABLE "DataAccessLayer_fundinggroup" ADD COLUMN "initiator_id" uuid NOT NULL CONSTRAINT "DataAccessLayer_fund_initiator_id_2fcc25cc_fk_DataAcces" REFERENCES "DataAccessLayer_user"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "DataAccessLayer_fund_initiator_id_2fcc25cc_fk_DataAcces" IMMEDIATE;

--
-- Add field beneficiary to funding
--
ALTER TABLE "DataAccessLayer_funding" ADD COLUMN "beneficiary_id" uuid NOT NULL CONSTRAINT "DataAccessLayer_fund_beneficiary_id_2a0b7d17_fk_DataAcces" REFERENCES "DataAccessLayer_user"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "DataAccessLayer_fund_beneficiary_id_2a0b7d17_fk_DataAcces" IMMEDIATE;

--
-- Add field fundingGroup to funding
--
ALTER TABLE "DataAccessLayer_funding" ADD COLUMN "fundingGroup_id" uuid NOT NULL CONSTRAINT "DataAccessLayer_fund_fundingGroup_id_61b55d94_fk_DataAcces" REFERENCES "DataAccessLayer_fundinggroup"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "DataAccessLayer_fund_fundingGroup_id_61b55d94_fk_DataAcces" IMMEDIATE;

--
-- Add field beneficiarySourceType to beneficiarysource
--
ALTER TABLE "DataAccessLayer_beneficiarysource" ADD COLUMN "beneficiarySourceType_id" uuid NOT NULL CONSTRAINT "DataAccessLayer_bene_beneficiarySourceTyp_bc7d83b6_fk_DataAcces" REFERENCES "DataAccessLayer_beneficiarysourcetype"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "DataAccessLayer_bene_beneficiarySourceTyp_bc7d83b6_fk_DataAcces" IMMEDIATE;

--
-- Add field issuer to beneficiarysource
--
ALTER TABLE "DataAccessLayer_beneficiarysource" ADD COLUMN "issuer_id" uuid NOT NULL CONSTRAINT "DataAccessLayer_bene_issuer_id_1ca6d44c_fk_DataAcces" REFERENCES "DataAccessLayer_issuer"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "DataAccessLayer_bene_issuer_id_1ca6d44c_fk_DataAcces" IMMEDIATE;

--
-- Add field user to beneficiarysource
--

ALTER TABLE "DataAccessLayer_beneficiarysource" ADD COLUMN "user_id" uuid NOT NULL CONSTRAINT "DataAccessLayer_bene_user_id_bdb20c91_fk_DataAcces" REFERENCES "DataAccessLayer_user"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "DataAccessLayer_bene_user_id_bdb20c91_fk_DataAcces" IMMEDIATE;

CREATE INDEX "DataAccessLayer_beneficiarysourcetype_name_620b816c_like" ON "DataAccessLayer_beneficiarysourcetype" ("name" varchar_pattern_ops);

CREATE INDEX "DataAccessLayer_fundinggrouptype_name_0ca4b331_like" ON "DataAccessLayer_fundinggrouptype" ("name" varchar_pattern_ops);

CREATE INDEX "DataAccessLayer_fundingsourcetype_name_72d6d774_like" ON "DataAccessLayer_fundingsourcetype" ("name" varchar_pattern_ops);

CREATE INDEX "DataAccessLayer_issuer_name_cbbd1241_like" ON "DataAccessLayer_issuer" ("name" varchar_pattern_ops);

CREATE INDEX "DataAccessLayer_role_name_6c5eaa76_like" ON "DataAccessLayer_role" ("name" varchar_pattern_ops);

CREATE INDEX "DataAccessLayer_user_phoneNumber_1d206e5a_like" ON "DataAccessLayer_user" ("phoneNumber" varchar_pattern_ops);

ALTER TABLE "DataAccessLayer_fundingtransaction" ADD CONSTRAINT "DataAccessLayer_fund_funding_id_0d6c8e72_fk_DataAcces" FOREIGN KEY ("funding_id") REFERENCES "DataAccessLayer_funding" ("id") DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE "DataAccessLayer_fundingtransaction" ADD CONSTRAINT "DataAccessLayer_fund_fundingSource_id_141fa75e_fk_DataAcces" FOREIGN KEY ("fundingSource_id") REFERENCES "DataAccessLayer_fundingsource" ("id") DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE "DataAccessLayer_fundingtransaction" ADD CONSTRAINT "DataAccessLayer_fund_issuer_id_f10146e5_fk_DataAcces" FOREIGN KEY ("issuer_id") REFERENCES "DataAccessLayer_issuer" ("id") DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE "DataAccessLayer_fundingtransaction" ADD CONSTRAINT "DataAccessLayer_fund_user_id_bddeb0f1_fk_DataAcces" FOREIGN KEY ("user_id") REFERENCES "DataAccessLayer_user" ("id") DEFERRABLE INITIALLY DEFERRED;

CREATE INDEX "DataAccessLayer_fundingtransaction_funding_id_0d6c8e72" ON "DataAccessLayer_fundingtransaction" ("funding_id");

CREATE INDEX "DataAccessLayer_fundingtransaction_fundingSource_id_141fa75e" ON "DataAccessLayer_fundingtransaction" ("fundingSource_id");

CREATE INDEX "DataAccessLayer_fundingtransaction_issuer_id_f10146e5" ON "DataAccessLayer_fundingtransaction" ("issuer_id");

CREATE INDEX "DataAccessLayer_fundingtransaction_user_id_bddeb0f1" ON "DataAccessLayer_fundingtransaction" ("user_id");

ALTER TABLE "DataAccessLayer_fundingsourceproperty" ADD CONSTRAINT "DataAccessLayer_fund_fundingSource_id_c8564390_fk_DataAcces" FOREIGN KEY ("fundingSource_id") REFERENCES "DataAccessLayer_fundingsource" ("id") DEFERRABLE INITIALLY DEFERRED;

CREATE INDEX "DataAccessLayer_fundingsourceproperty_fundingSource_id_c8564390" ON "DataAccessLayer_fundingsourceproperty" ("fundingSource_id");

CREATE INDEX "DataAccessLayer_fundingsource_fundingSourceType_id_a801fcf2" ON "DataAccessLayer_fundingsource" ("fundingSourceType_id");

CREATE INDEX "DataAccessLayer_fundingsource_issuer_id_fe5db4af" ON "DataAccessLayer_fundingsource" ("issuer_id");

CREATE INDEX "DataAccessLayer_fundingsource_user_id_23dfc454" ON "DataAccessLayer_fundingsource" ("user_id");

ALTER TABLE "DataAccessLayer_fundinggroupuser" ADD CONSTRAINT "DataAccessLayer_fund_beneficiarySource_id_045ef031_fk_DataAcces" FOREIGN KEY ("beneficiarySource_id") REFERENCES "DataAccessLayer_beneficiarysource" ("id") DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE "DataAccessLayer_fundinggroupuser" ADD CONSTRAINT "DataAccessLayer_fund_fundingGroup_id_f9f6b668_fk_DataAcces" FOREIGN KEY ("fundingGroup_id") REFERENCES "DataAccessLayer_fundinggroup" ("id") DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE "DataAccessLayer_fundinggroupuser" ADD CONSTRAINT "DataAccessLayer_fund_fundingSource_id_d1af1591_fk_DataAcces" FOREIGN KEY ("fundingSource_id") REFERENCES "DataAccessLayer_fundingsource" ("id") DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE "DataAccessLayer_fundinggroupuser" ADD CONSTRAINT "DataAccessLayer_fund_role_id_9250ffc1_fk_DataAcces" FOREIGN KEY ("role_id") REFERENCES "DataAccessLayer_role" ("id") DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE "DataAccessLayer_fundinggroupuser" ADD CONSTRAINT "DataAccessLayer_fund_user_id_8941c4de_fk_DataAcces" FOREIGN KEY ("user_id") REFERENCES "DataAccessLayer_user" ("id") DEFERRABLE INITIALLY DEFERRED;

CREATE INDEX "DataAccessLayer_fundinggroupuser_beneficiarySource_id_045ef031" ON "DataAccessLayer_fundinggroupuser" ("beneficiarySource_id");

CREATE INDEX "DataAccessLayer_fundinggroupuser_fundingGroup_id_f9f6b668" ON "DataAccessLayer_fundinggroupuser" ("fundingGroup_id");

CREATE INDEX "DataAccessLayer_fundinggroupuser_fundingSource_id_d1af1591" ON "DataAccessLayer_fundinggroupuser" ("fundingSource_id");

CREATE INDEX "DataAccessLayer_fundinggroupuser_role_id_9250ffc1" ON "DataAccessLayer_fundinggroupuser" ("role_id");

CREATE INDEX "DataAccessLayer_fundinggroupuser_user_id_8941c4de" ON "DataAccessLayer_fundinggroupuser" ("user_id");

CREATE INDEX "DataAccessLayer_fundinggroup_fundingGroupType_id_72823747" ON "DataAccessLayer_fundinggroup" ("fundingGroupType_id");

CREATE INDEX "DataAccessLayer_fundinggroup_initiator_id_2fcc25cc" ON "DataAccessLayer_fundinggroup" ("initiator_id");

CREATE INDEX "DataAccessLayer_funding_beneficiary_id_2a0b7d17" ON "DataAccessLayer_funding" ("beneficiary_id");

CREATE INDEX "DataAccessLayer_funding_fundingGroup_id_61b55d94" ON "DataAccessLayer_funding" ("fundingGroup_id");

ALTER TABLE "DataAccessLayer_beneficiarysourceproperty" ADD CONSTRAINT "DataAccessLayer_bene_beneficiarySource_id_6bff0742_fk_DataAcces" FOREIGN KEY ("beneficiarySource_id") REFERENCES "DataAccessLayer_beneficiarysource" ("id") DEFERRABLE INITIALLY DEFERRED;

CREATE INDEX "DataAccessLayer_beneficiar_beneficiarySource_id_6bff0742" ON "DataAccessLayer_beneficiarysourceproperty" ("beneficiarySource_id");

CREATE INDEX "DataAccessLayer_beneficiar_beneficiarySourceType_id_bc7d83b6" ON "DataAccessLayer_beneficiarysource" ("beneficiarySourceType_id");

CREATE INDEX "DataAccessLayer_beneficiarysource_issuer_id_1ca6d44c" ON "DataAccessLayer_beneficiarysource" ("issuer_id");

CREATE INDEX "DataAccessLayer_beneficiarysource_user_id_bdb20c91" ON "DataAccessLayer_beneficiarysource" ("user_id");
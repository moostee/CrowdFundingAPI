# Generated by Django 3.0.2 on 2020-01-21 10:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeneficiarySourceType',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('isDeleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Funding',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('isDeleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cycle', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=19)),
                ('currency', models.CharField(max_length=50)),
                ('dueDate', models.DateField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FundingGroup',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('isDeleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('totalCycles', models.IntegerField()),
                ('currentCycle', models.IntegerField()),
                ('startDate', models.DateTimeField()),
                ('nextCycleDate', models.DateTimeField()),
                ('cycleDuration', models.CharField(max_length=10)),
                ('code', models.CharField(max_length=50)),
                ('isClosed', models.BooleanField(default=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=19)),
                ('currency', models.CharField(max_length=10)),
                ('targetGroupAmount', models.DecimalField(decimal_places=2, max_digits=19)),
                ('targetGroupDate', models.DateTimeField()),
                ('debitBeneficiary', models.BooleanField(default=False)),
                ('failureAction', models.CharField(choices=[('Continue', 'Continue Process'), ('Abort', 'Abort Process'), ('Hold', 'Hold Process')], max_length=64)),
                ('description', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FundingGroupType',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('isDeleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('hasFixedIndividualAmount', models.BooleanField()),
                ('hasFixedGroupAmount', models.BooleanField()),
                ('hasMaturityDate', models.BooleanField()),
                ('maxUser', models.IntegerField()),
                ('minUser', models.IntegerField()),
                ('isAutomatedCycle', models.BooleanField()),
                ('defaultCycleDuration', models.CharField(max_length=10)),
                ('hasRollingBeneficiary', models.BooleanField()),
                ('hasFixedDefaultCycle', models.BooleanField()),
                ('canJoinClosedGroup', models.BooleanField()),
                ('description', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FundingSource',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('isDeleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sourceNumber', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FundingSourceType',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('isDeleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Issuer',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('isDeleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('referenceType', models.CharField(max_length=50)),
                ('referenceTypeMaxChar', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('isDeleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('isDeleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('userId', models.UUIDField(editable=False)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FundingTransaction',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('isDeleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.FloatField(default=0.0)),
                ('currency', models.CharField(max_length=100)),
                ('paymentTransactionRef', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('pending', 'pending transaction'), ('successful', 'successful transaction'), ('failed', 'failed transaction')], default='pending', max_length=100)),
                ('issuerResponseCode', models.CharField(max_length=100)),
                ('issuerPaymentReference', models.CharField(max_length=100)),
                ('issuerRemark', models.CharField(max_length=255)),
                ('fundingId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.Funding')),
                ('fundingSourceId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.FundingSource')),
                ('issuerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.Issuer')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FundingSourcePropertyType',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('isDeleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default=False, max_length=50)),
                ('dataType', models.CharField(max_length=64)),
                ('fundingSourceTypeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.FundingSourceType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FundingSourceProperty',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('isDeleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('propertyValue', models.CharField(max_length=100)),
                ('fundingSourcePropertyTypeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.FundingSourcePropertyType')),
                ('fundingSourceTypeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.FundingSourceType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='fundingsource',
            name='fundingSourceTypeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.FundingSourceType'),
        ),
        migrations.AddField(
            model_name='fundingsource',
            name='issuerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.Issuer'),
        ),
        migrations.AddField(
            model_name='fundingsource',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.User'),
        ),
        migrations.CreateModel(
            name='FundingGroupUser',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('isDeleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('userSequence', models.IntegerField()),
                ('balance', models.DecimalField(decimal_places=2, max_digits=19)),
                ('status', models.CharField(choices=[('Pending', 'User approval pending'), ('Approved', 'User Approved'), ('Declined', 'User declined')], max_length=64)),
                ('fundingGroupId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.FundingGroup')),
                ('roleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.Role')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='fundinggroup',
            name='fundingGroupTypeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.FundingGroupType'),
        ),
        migrations.AddField(
            model_name='fundinggroup',
            name='initiatorId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.User'),
        ),
        migrations.AddField(
            model_name='funding',
            name='beneficiaryId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.User'),
        ),
        migrations.AddField(
            model_name='funding',
            name='fundingGroupId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.FundingGroup'),
        ),
        migrations.CreateModel(
            name='BeneficiarySourcePropertyType',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('isDeleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default=False, max_length=50)),
                ('dataType', models.CharField(max_length=64)),
                ('beneficiarySourceTypeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.BeneficiarySourceType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BeneficiarySourceProperty',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('isDeleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('propertyValue', models.CharField(max_length=100)),
                ('beneficiarySourcePropertyTypeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.BeneficiarySourcePropertyType')),
                ('beneficiarySourceTypeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.BeneficiarySourceType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BeneficiarySource',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('isDeleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('destinationNumber', models.CharField(max_length=20)),
                ('issuerId', models.UUIDField(editable=False)),
                ('beneficiarySourceTypeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.BeneficiarySourceType')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

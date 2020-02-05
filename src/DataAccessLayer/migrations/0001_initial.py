# Generated by Django 3.0.2 on 2020-02-05 13:18

import django.contrib.postgres.fields.jsonb
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
            name='BeneficiarySource',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('isDeleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('destinationNumber', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BeneficiarySourceType',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('isDeleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
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
                ('cycle', models.PositiveSmallIntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=19)),
                ('currency', models.CharField(max_length=50)),
                ('dueDate', models.DateField(blank=True)),
                ('status', models.CharField(choices=[('pending', 'Funding is pending'), ('active', 'Funding is active and yet to be paid'), ('completed', 'Funding has been paid and is completed')], default='pending', max_length=64)),
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
                ('totalCycles', models.PositiveSmallIntegerField(default=1)),
                ('currentCycle', models.PositiveSmallIntegerField(default=1)),
                ('startDate', models.DateField()),
                ('nextCycleDate', models.DateField(null=True)),
                ('cycleDuration', models.CharField(max_length=10, null=True)),
                ('code', models.CharField(max_length=50)),
                ('isClosed', models.BooleanField(default=False)),
                ('individualAmount', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('currency', models.CharField(max_length=10, null=True)),
                ('targetGroupAmount', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('targetGroupDate', models.DateField(null=True)),
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
                ('maxUser', models.PositiveSmallIntegerField()),
                ('minUser', models.PositiveSmallIntegerField()),
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
                ('name', models.CharField(max_length=100, unique=True)),
                ('config', django.contrib.postgres.fields.jsonb.JSONField()),
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
                ('name', models.CharField(max_length=100, unique=True)),
                ('referenceTypeMaxChar', models.PositiveSmallIntegerField()),
                ('referenceType', models.CharField(choices=[('alpha-numeric', 'Containing alphabets and numbers'), ('numeric', 'Containing only numbers'), ('alpha', 'Containing only alphabets')], max_length=32)),
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
                ('name', models.CharField(max_length=100, unique=True)),
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
                ('funding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.Funding')),
                ('fundingSource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.FundingSource')),
                ('issuer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.Issuer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.User')),
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
                ('propertyName', models.CharField(max_length=100)),
                ('propertyValue', models.CharField(max_length=100)),
                ('fundingSource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.FundingSource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='fundingsource',
            name='fundingSourceType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.FundingSourceType'),
        ),
        migrations.AddField(
            model_name='fundingsource',
            name='issuer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.Issuer'),
        ),
        migrations.AddField(
            model_name='fundingsource',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.User'),
        ),
        migrations.CreateModel(
            name='FundingGroupUser',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('isDeleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('userSequence', models.PositiveSmallIntegerField()),
                ('balance', models.DecimalField(decimal_places=2, max_digits=19)),
                ('status', models.CharField(choices=[('Pending', 'User approval pending'), ('Approved', 'User Approved'), ('Declined', 'User declined')], max_length=64)),
                ('beneficiarySource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.BeneficiarySource')),
                ('fundingGroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.FundingGroup')),
                ('fundingSource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.FundingSource')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.Role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='fundinggroup',
            name='fundingGroupType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.FundingGroupType'),
        ),
        migrations.AddField(
            model_name='fundinggroup',
            name='initiator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.User'),
        ),
        migrations.AddField(
            model_name='funding',
            name='beneficiary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beneficiary', to='DataAccessLayer.User'),
        ),
        migrations.AddField(
            model_name='funding',
            name='fundingGroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fundingGroup', to='DataAccessLayer.FundingGroup'),
        ),
        migrations.CreateModel(
            name='BeneficiarySourceProperty',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('isDeleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('propertyType', models.CharField(default=False, max_length=100)),
                ('propertyValue', models.CharField(max_length=100)),
                ('beneficiarySource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.BeneficiarySource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='beneficiarysource',
            name='beneficiarySourceType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.BeneficiarySourceType'),
        ),
        migrations.AddField(
            model_name='beneficiarysource',
            name='issuer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.Issuer'),
        ),
        migrations.AddField(
            model_name='beneficiarysource',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataAccessLayer.User'),
        ),
    ]

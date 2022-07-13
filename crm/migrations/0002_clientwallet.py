# Generated by Django 3.2.14 on 2022-07-08 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientWallet',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='crm.basemodel')),
                ('total_balance', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('available_balance', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('lien_balance', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('clients', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crm.client')),
            ],
            bases=('crm.basemodel',),
        ),
    ]

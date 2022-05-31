# Generated by Django 2.2.28 on 2022-05-13 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Espp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateField(verbose_name='Purchase Date')),
                ('exchange', models.CharField(choices=[('NASDAQ', 'NASDAQ'), ('NYSE', 'NYSE'), ('BSE', 'BSE'), ('NSE', 'NSE')], max_length=10)),
                ('symbol', models.CharField(max_length=20)),
                ('subscription_fmv', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Subscription FMV')),
                ('purchase_fmv', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Purchase FMV')),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Purchase Price')),
                ('shares_purchased', models.DecimalField(decimal_places=0, max_digits=20, verbose_name='Shares Purchased')),
                ('purchase_conversion_rate', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Purchase Conversion Rate')),
                ('total_purchase_price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Total Purchase Price')),
                ('shares_avail_for_sale', models.DecimalField(decimal_places=0, max_digits=20, verbose_name='Shares Available For Sale')),
                ('user', models.IntegerField()),
                ('goal', models.IntegerField(blank=True, null=True)),
                ('latest_conversion_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Latest Conversion Price')),
                ('latest_price', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Latest Price')),
                ('latest_value', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Latest Value')),
                ('as_on_date', models.DateField(blank=True, null=True, verbose_name='As On Date')),
                ('unrealised_gain', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Unrealised Gain')),
                ('realised_gain', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Realised Gain')),
                ('xirr', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='XIRR')),
            ],
            options={
                'unique_together': {('purchase_date', 'symbol')},
            },
        ),
        migrations.CreateModel(
            name='EsppSellTransactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans_date', models.DateField(verbose_name='Transaction Date')),
                ('price', models.DecimalField(decimal_places=4, max_digits=20, verbose_name='Price')),
                ('units', models.DecimalField(decimal_places=4, max_digits=20)),
                ('conversion_rate', models.DecimalField(decimal_places=2, default=1, max_digits=20, verbose_name='Conversion Rate')),
                ('trans_price', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='Total Price')),
                ('realised_gain', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Realised Gain')),
                ('notes', models.CharField(blank=True, max_length=80, null=True)),
                ('espp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='espp.Espp')),
            ],
            options={
                'unique_together': {('espp', 'trans_date')},
            },
        ),
    ]
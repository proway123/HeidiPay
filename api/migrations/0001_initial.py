# Generated by Django 3.1.6 on 2021-02-19 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(max_length=40)),
                ('card_number', models.IntegerField(max_length=16)),
                ('merchant_id', models.IntegerField(max_length=4)),
                ('merchant_name', models.CharField(max_length=50)),
                ('amount', models.IntegerField(default=0, max_length=16)),
                ('accepted', models.NullBooleanField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='TopUpEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(default='', max_length=40)),
                ('card_number', models.IntegerField(default=0, max_length=16)),
                ('method', models.CharField(default='', max_length=40)),
                ('amount', models.IntegerField(default=0, max_length=16)),
                ('accepted', models.NullBooleanField(default=None)),
            ],
        ),
    ]
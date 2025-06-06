# Generated by Django 5.2 on 2025-05-07 17:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('mg', models.PositiveIntegerField(blank=True, null=True)),
                ('expiry_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.CharField(choices=[('vitamins', 'Vitamins'), ('painkillers', 'Painkillers'), ('supplements', 'Supplements'), ('antibiotics', 'Antibiotics'), ('antiseptics', 'Antiseptics'), ('antacids', 'Antacids'), ('other', 'Other')], default='other', max_length=50)),
            ],
        ),
    ]

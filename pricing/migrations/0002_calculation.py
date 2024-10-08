# Generated by Django 5.0.6 on 2024-08-08 23:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(choices=[('BLACK_SCHOLES', 'Black-Scholes'), ('BINOMIAL', 'Binomial')], max_length=15)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('stock', models.IntegerField()),
                ('strike', models.IntegerField()),
                ('expiry', models.IntegerField()),
                ('rfr', models.IntegerField()),
                ('vol', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calculations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

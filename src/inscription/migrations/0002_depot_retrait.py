# Generated by Django 2.2.3 on 2019-07-26 09:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Retrait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operateur', models.CharField(max_length=200)),
                ('numero', models.TextField()),
                ('retrait_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Montant_retrait', models.DecimalField(decimal_places=2, default=False, max_digits=10)),
                ('Utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscription.Utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Depot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operateur', models.CharField(max_length=200)),
                ('numero', models.TextField()),
                ('depot_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Montant_depot', models.DecimalField(decimal_places=2, default=False, max_digits=10)),
                ('Utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscription.Utilisateur')),
            ],
        ),
    ]

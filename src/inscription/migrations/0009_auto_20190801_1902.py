# Generated by Django 2.2.3 on 2019-08-01 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0008_categorie_championat_equipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='choixMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.CharField(max_length=60)),
                ('ordered', models.BooleanField(default=False)),
                ('equipe', models.CharField(max_length=20)),
                ('cote', models.DecimalField(decimal_places=2, default=False, max_digits=10)),
                ('Utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscription.Utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Paris',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(blank=True, max_length=20, null=True)),
                ('coteTotal', models.DecimalField(decimal_places=2, default=False, max_digits=10)),
                ('Mise', models.DecimalField(decimal_places=2, default=False, max_digits=10)),
                ('Gain', models.DecimalField(decimal_places=2, default=False, max_digits=10)),
                ('statut', models.CharField(max_length=20)),
                ('Utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscription.Utilisateur')),
                ('selection', models.ManyToManyField(to='inscription.choixMatch')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('heure', models.TimeField()),
                ('v1', models.DecimalField(decimal_places=2, default=False, max_digits=10)),
                ('v2', models.DecimalField(decimal_places=2, default=False, max_digits=10)),
                ('x', models.DecimalField(decimal_places=2, default=False, max_digits=10)),
                ('Categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscription.Categorie')),
                ('Championat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscription.Championat')),
                ('equipe_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipe_1', to='inscription.Equipe')),
                ('equipe_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscription.Equipe')),
            ],
        ),
        migrations.AddField(
            model_name='choixmatch',
            name='matchid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscription.Match'),
        ),
    ]

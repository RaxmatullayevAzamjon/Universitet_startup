# Generated by Django 4.2.2 on 2023-06-20 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('asosiy', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Yonalish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('aktiv', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ustoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('jins', models.CharField(choices=[('erkak', 'erkak'), ('ayol', 'ayol')], max_length=20)),
                ('yosh', models.PositiveSmallIntegerField()),
                ('daraja', models.CharField(choices=[('Bakalavr', 'Bakalavr'), ('Magistr', 'Magistr')], max_length=20)),
                ('fan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.fan')),
            ],
        ),
        migrations.AddField(
            model_name='fan',
            name='yonalish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.yonalish'),
        ),
    ]

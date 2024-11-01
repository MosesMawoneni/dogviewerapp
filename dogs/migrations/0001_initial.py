# Generated by Django 5.1.2 on 2024-10-28 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('street', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='dogs/')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('owner', models.CharField(max_length=100)),
            ],
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-19 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('preco_custo', models.DecimalField(decimal_places=2, default='', max_digits=7)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]

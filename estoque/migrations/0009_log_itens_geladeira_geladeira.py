# Generated by Django 4.2.6 on 2023-10-30 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0008_alter_produto_unidade_medida_log_itens_geladeira_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='log_itens_geladeira',
            name='geladeira',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='estoque.geladeira'),
        ),
    ]
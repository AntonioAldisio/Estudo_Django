from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        # Dependências de outras migrações, se houver
    ]

    operations = [
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('codigo_imovel', models.CharField(max_length=50, primary_key=True)),
                ('limite_hospedes', models.IntegerField()),
                ('quantidade_banheiros', models.IntegerField()),
                ('aceita_animais', models.BooleanField()),
                ('valor_limpeza', models.DecimalField(max_digits=8, decimal_places=2)),
                ('data_ativacao', models.DateField(auto_now_add=False)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

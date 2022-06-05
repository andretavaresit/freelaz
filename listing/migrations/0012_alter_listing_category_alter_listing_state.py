# Generated by Django 4.0.4 on 2022-06-04 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0011_alter_listing_category_alter_listing_photo_main_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Marketing Digital', 'Marketing Digital'), ('Educação', 'Educação'), ('Atividade Física', 'Atividade Física'), ('Gastronomia', 'Gastronomia'), ('Tecnologia e Programação', 'Tecnologia e Programação'), ('Arte', 'Arte'), ('Negócios', 'Negócios'), ('Música e Áudio', 'Música e Áudio'), ('Serviços Gerais', 'Serviços Gerais'), ('Vídeo e Edição', 'Vídeo e Edição'), ('Design', 'Design')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('PR', 'Paraná'), ('TO', 'Tocantins'), ('BA', 'Bahia'), ('PE', 'Pernambuco'), ('ES', 'Espírito Santo'), ('AM', 'Amazonas'), ('AL', 'Alagoas'), ('AC', 'Acre'), ('SP', 'São Paulo'), ('AP', 'Amapá'), ('MA', 'Maranhão'), ('SE', 'Sergipe'), ('MT', 'Mato Grosso'), ('MG', 'Minas Gerais'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('PA', 'Pará'), ('DF', 'Distrito Federal'), ('RN', 'Rio Grande do Norte'), ('PB', 'Paraíba'), ('SC', 'Santa Catarina'), ('PI', 'Piauí'), ('RR', 'Roraima'), ('GO', 'Goiás'), ('MS', 'Mato Grosso do Sul'), ('RJ', 'Rio de Janeiro'), ('CE', 'Ceará')], max_length=100),
        ),
    ]

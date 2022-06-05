# Generated by Django 4.0.4 on 2022-06-04 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0009_alter_listing_category_alter_listing_state'),
        ('inquiry', '0004_alter_inquiry_listing_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='anuncio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='listing.listing'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='listing_id',
            field=models.IntegerField(),
        ),
    ]

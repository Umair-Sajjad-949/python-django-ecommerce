# Generated by Django 5.1.1 on 2024-09-24 10:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_categories_icon_alter_setting_favicon_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='products/')),
                ('short_desc', models.TextField()),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('is_trending', models.BooleanField()),
                ('is_featured', models.BooleanField()),
                ('status', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='website.categories')),
            ],
        ),
    ]

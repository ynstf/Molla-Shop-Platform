# Generated by Django 3.2.19 on 2023-11-15 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20231115_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='information',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_back',
            field=models.ImageField(default='/static/default_product.png', upload_to='products_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_cross',
            field=models.ImageField(default='/static/default_product.png', upload_to='products_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_side',
            field=models.ImageField(default='/static/default_product.png', upload_to='products_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_with_model',
            field=models.ImageField(default='/static/default_product.png', upload_to='products_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='shipping_roles',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='/static/default_category.png', upload_to='categories_images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='/static/default_product.png', upload_to='products_images/'),
        ),
    ]
# Generated by Django 3.0 on 2019-12-16 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191211_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.TextField(max_length=50)),
                ('price', models.IntegerField()),
                ('manufactured_data', models.DateField()),
                ('available', models.CharField(choices=[('YES', 'y'), ('NO', 'N')], max_length=5)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Stores')),
            ],
        ),
    ]

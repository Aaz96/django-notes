# Generated by Django 3.0 on 2019-12-12 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_item_name', models.CharField(default='arbitrry item', max_length=64)),
                ('cart_item_count', models.IntegerField(default=0)),
            ],
        ),
    ]
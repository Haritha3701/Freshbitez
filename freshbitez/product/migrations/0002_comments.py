# Generated by Django 4.1.7 on 2023-05-23 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('msg', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cmt', to='product.products')),
            ],
        ),
    ]
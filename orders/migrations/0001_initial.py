# Generated by Django 2.1.1 on 2018-12-22 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_res', '0002_auto_20181218_1956'),
        ('sells', '0008_auto_20181219_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
                ('sell_stuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='login_res.User')),
                ('stuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='login_res.User')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='sells.Product')),
            ],
        ),
    ]

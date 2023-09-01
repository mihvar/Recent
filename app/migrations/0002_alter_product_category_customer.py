# Generated by Django 4.2.3 on 2023-07-23 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('AIC', 'Amul Ice Cream'), ('DRIC', 'DoubleRainbow Ice Cream'), ('VLIC', 'Valdilal Ice Cream'), ('BRIC', 'BaskinRobbins Ice Cream'), ('BBIC', 'BlueBunny Ice Cream'), ('CMIC', 'CargillsMagic Ice Cream'), ('CBIC', 'CreamBell Ice Cream'), ('CRIC', 'CreamStone Ice Cream'), ('HIC', 'Havmor Ice Cream'), ('MDIC', 'MotherDiary Ice Cream')], max_length=10),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('mobile', models.IntegerField(default=0)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Maharashtra', 'Maharashtra'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Tripura', 'Tripura'), ('Telangana', 'Telangana'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra & Nagar Haveli and Daman & Diu', 'Dadra & Nagar Haveli and Daman & Diu'), ('Delhi', 'Delhi'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Ladakh', 'Ladakh'), ('Lakshadweep', 'Lakshadweep'), ('Puducherry', 'Puducherry')], max_length=100)),
                ('product_image', models.ImageField(upload_to='product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 4.1.dev20220429194355 on 2022-05-06 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="oder",
            name="size",
            field=models.CharField(default=True, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="size",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
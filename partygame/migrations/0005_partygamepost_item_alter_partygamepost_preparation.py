# Generated by Django 4.1 on 2023-03-06 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("partygame", "0004_partygamepost_preparation"),
    ]

    operations = [
        migrations.AddField(
            model_name="partygamepost",
            name="item",
            field=models.TextField(default=1, verbose_name="ゲームに必要なアイテム"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="partygamepost",
            name="preparation",
            field=models.TextField(verbose_name="開始前の準備"),
        ),
    ]

# Generated by Django 5.0 on 2024-03-14 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmanagement', '0003_alter_book_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(default='', upload_to='library_manage/books_image'),
        ),
    ]

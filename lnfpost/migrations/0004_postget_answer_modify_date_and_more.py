# Generated by Django 4.0.3 on 2023-12-06 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lnfpost', '0003_postget_answer_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='postget_answer',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='postget_question',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
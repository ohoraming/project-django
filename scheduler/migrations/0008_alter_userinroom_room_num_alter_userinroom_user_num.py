# Generated by Django 4.0.2 on 2022-03-22 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0007_alter_userinroom_room_num_alter_userinroom_user_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinroom',
            name='room_num',
            field=models.ForeignKey(db_column='room_num', on_delete=django.db.models.deletion.CASCADE, to='scheduler.room'),
        ),
        migrations.AlterField(
            model_name='userinroom',
            name='user_num',
            field=models.ForeignKey(db_column='user_num', on_delete=django.db.models.deletion.CASCADE, to='scheduler.user'),
        ),
    ]

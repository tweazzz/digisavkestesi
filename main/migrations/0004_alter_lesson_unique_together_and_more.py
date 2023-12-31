# Generated by Django 4.2.7 on 2023-12-26 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_oner_success_photo_alter_sport_success_photo'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='dopurok',
            name='faculative_name',
        ),
        migrations.AddField(
            model_name='dopurok',
            name='classroom2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classroom2', to='main.classrooms'),
        ),
        migrations.AddField(
            model_name='dopurok',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.subject'),
        ),
        migrations.AddField(
            model_name='dopurok',
            name='subject2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject2', to='main.subject'),
        ),
        migrations.AddField(
            model_name='dopurok',
            name='teacher2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher2', to='main.teacher'),
        ),
        migrations.AddField(
            model_name='schoolpasport',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='class',
            name='class_teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_teacher', to='main.teacher'),
        ),
        migrations.AlterField(
            model_name='jobhistory',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='jobhistory',
            name='job_characteristic',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='jobhistory',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.teacher'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='start_end_time',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='pandikolimpiada_success',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='specialityhistory',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.teacher'),
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='lesson_order',
        ),
    ]

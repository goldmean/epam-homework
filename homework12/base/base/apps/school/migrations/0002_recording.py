# Generated by Django 4.0 on 2022-01-03 22:02

from datetime import date

from django.db import migrations


def recording(apps, schema_editor):
    Student = apps.get_model('school', 'Student')
    Teacher = apps.get_model('school', 'Teacher')
    Homework = apps.get_model('school', 'Homework')
    HomeworkResult = apps.get_model('school', 'HomeworkResult')

    student = Student(first_name='Roman', last_name='Petrov')
    teacher = Teacher(first_name='Daniil', last_name='Shadrin')
    homework = Homework(
        text='Learn OOP', created=date.today(), deadline=date.today(),
    )
    homework_result = HomeworkResult(
        author=student,
        homework=homework,
        solution='I have done the homework',
        created=date.today(),
    )

    student.save()
    teacher.save()
    homework.save()
    homework_result.save()


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(recording)
    ]

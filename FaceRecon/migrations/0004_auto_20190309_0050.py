# Generated by Django 2.1.7 on 2019-03-09 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FaceRecon', '0003_usuario_treina'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procurados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('idade', models.IntegerField()),
                ('genre', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('telefone', models.CharField(max_length=50)),
                ('treina', models.BinaryField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FaceRecon.Usuario')),
            ],
        ),
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]
# Generated by Django 4.2.4 on 2023-08-21 04:37

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AreaCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Тошкент ш.', 1), ('Қорақалпоғистон', 2), ('Андижон', 3), ('Фарғона', 4), ('Наманган', 5), ('Самарқанд', 6), ('Бухоро', 7), ('Хоразм', 8), ('Сурхондарё', 9), ('Қашқадарё', 10), ('Жиззах', 11), ('Сирдарё', 12), ('Тошкент вил.', 13), ('Навоий', 14)], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('ЎЗБЕКИСТОН', 1), ('ЖАҲОН', 2), ('ИҚТИСОДИЁТ', 3), ('ЖАМИЯТ', 4), ('ФАН-ТЕХНИКА', 5), ('СПОРТ', 6), ('НУҚТАЙИ НАЗАР', 7), ('АУДИО', 8), ('PDP_ACADEMY, ', 9)], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_uz', models.CharField(max_length=200, null=True)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('text', models.TextField()),
                ('text_uz', models.TextField(null=True)),
                ('text_en', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('to_AreaCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.areacategory')),
                ('to_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'ordering': ['-data'],
            },
        ),
        migrations.AddField(
            model_name='areacategory',
            name='to_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.newscategory'),
        ),
    ]
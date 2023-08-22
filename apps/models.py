from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model, CharField, ForeignKey, CASCADE, TextField, ImageField, FileField, DateTimeField, \
    BooleanField
from django.utils.translation import gettext as _
# Create your models here.

news = [
    ('ЎЗБЕКИСТОН', 1),
    ('ЖАҲОН', 2),
    ('ИҚТИСОДИЁТ', 3),
    ('ЖАМИЯТ', 4),
    ('ФАН-ТЕХНИКА', 5),
    ('СПОРТ', 6),
    ('НУҚТАЙИ НАЗАР', 7),
    ('АУДИО', 8),
    ('PDP_ACADEMY, ', 9)

]


class NewsCategory(Model):
    rating = CharField(choices=news, max_length=50)

    def __str__(self):
        return self.rating.title


area = [
    ('Тошкент ш.', 1),
    ('Қорақалпоғистон', 2),
    ('Андижон', 3),
    ('Фарғона', 4),
    ('Наманган', 5),
    ('Самарқанд', 6),
    ('Бухоро', 7),
    ('Хоразм', 8),
    ('Сурхондарё', 9),
    ('Қашқадарё', 10),
    ('Жиззах', 11),
    ('Сирдарё', 12),
    ('Тошкент вил.', 13),
    ('Навоий', 14),
]


class User(AbstractUser):
    update_at = DateTimeField(auto_now=True)


class AreaCategory(Model):
    title = CharField(choices=area, max_length=50)
    to_title = ForeignKey(NewsCategory, CASCADE)

    def __str__(self):
        return self.title and self.to_title


class Post(Model):
    title = CharField(max_length=200)
    text = TextField()
    image = ImageField(blank=True)
    data = DateTimeField(auto_now_add=True)
    to_AreaCategory = ForeignKey(AreaCategory, CASCADE)
    to_author = ForeignKey(User, CASCADE)
    status = BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-data']
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def __str__(self):
        return self.title


class Postlike(Model):
    
    like = CharField(max_length=50)
    user = ForeignKey(User, on_delete=CASCADE, related_name='post_likes')
    post = ForeignKey(Post, on_delete=CASCADE, related_name='likes')

    def __str__(self):
        return self.like
# #Introduction model
#
# class Introduction(Model):
#     name = CharField(max_length=200 )
#     intro = CharField(max_length=200, blank=True)
#     video_link = CharField(max_length=200, blank=True)
#
#     def __str__(self):
#         return self.name


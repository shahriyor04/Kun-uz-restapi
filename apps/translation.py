from .models import Post

from modeltranslation.translator import TranslationOptions, register


@register(Post)
class PostTranslation(TranslationOptions):
    fields = [
        'title',
        'text'
    ]

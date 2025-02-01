from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='auto')
LANGUAGE_CODES = ['hi', 'bn']

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)

    def get_translation(self, lang_code):
        cache_key = f'faq_{self.pk}_question_{lang_code}'
        translation_text = cache.get(cache_key)

        if translation_text:
            return translation_text

        translation_text = getattr(self, f'question_{lang_code}', None)
        if translation_text:
            cache.set(cache_key, translation_text, timeout=60*60)
            return translation_text

        return self.question  # Default to English if no translation is found

    def save(self, *args, **kwargs):
        for lang in LANGUAGE_CODES:
            field_name = f'question_{lang}'
            if not getattr(self, field_name):
                try:
                    translated = translator.translate(self.question, target=lang)
                    setattr(self, field_name, translated)
                except Exception:
                    setattr(self, field_name, None)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question

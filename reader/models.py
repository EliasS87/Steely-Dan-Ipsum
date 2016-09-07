from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Paragraph(models.Model):

    text = models.CharField(max_length=30000, blank=True, null=True)
    number_of_paragraphs = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(9)], default=1)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Paragraph"
        verbose_name_plural = "Paragraphs"

    def __str__(self):
        return self.id

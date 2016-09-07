from django import forms
from . models import Paragraph


class ParagraphForm(forms.ModelForm):

    number_of_paragraphs = forms.IntegerField(max_value=9, min_value=1)

    class Meta:
        model = Paragraph
        fields = ('text', 'number_of_paragraphs',)

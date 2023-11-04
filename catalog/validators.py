import re

from django.core.exceptions import ValidationError


def validate_prohibited_words(value):
    prohibited_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
    for word in prohibited_words:
        if re.search(fr'\b{re.escape(word)}\b', value, re.IGNORECASE):
            raise ValidationError(f"The word '{word}' is prohibited in product name or description.")

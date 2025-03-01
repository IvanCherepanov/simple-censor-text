import re


class PatternCompilledRegex:
    """Подкласс для хранения скомпилированных регулярных выражений"""

    def __init__(self):
        self.patterns = {
            'names': re.compile(r'(?<!^)(?<![\.\!\?]\s)\b[A-ZА-Я][a-zа-я]+(?:\s[A-ZА-Я][a-zа-я]+)?\b'),
            'phones': re.compile(r'((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}'),
            'geo': re.compile(
    r'\b'
    r'(ул\.|улица|у\.|г\.|город|проспект|пр-т|проспекте|пер\.|переулок|переулке)'
    r'\s+'
    r'('
    r'[A-ZА-Яa-zа-я][a-zа-я]*'
    #r'(?:\s+[A-ZА-Яa-zа-я][a-zа-я]*)*'
    r')(?=\s|\.|,|$)',
    re.IGNORECASE
)
        }

    def get_all(self):
        """Возвращает все скомпилированные паттерны"""
        return self.patterns.values()


class TextCensor:
    def __init__(self):
        self.patterns = PatternCompilledRegex()

    def censor(self, text):
        """Цензурирует конфиденциальные данные"""
        result = text
        for pattern in self.patterns.get_all():
            result = pattern.sub('[censored]', result)
        return result

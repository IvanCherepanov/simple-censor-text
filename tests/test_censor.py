from unittest import TestCase

from app.domain.processors.main import TextCensor


class TestTextCensor(TestCase):
    def setUp(self):
        self.censor = TextCensor()

    def test_name_censorship(self):
        text = "Привет, Гарри Поттер! Меня зовут Том Реддл."
        result = self.censor.censor(text)
        self.assertEqual(result, "Привет, [censored]! Меня зовут [censored].")

    def test_phone_censorship(self):
        text = "Мой номер 8(926)123-45-67"  #+7(495)495-49-45
        result = self.censor.censor(text)
        self.assertEqual(result, "Мой номер [censored]")

    def test_geo_censorship(self):
        text = "Я живу на ул. ленина в кирпичном доме. Вокруг есть развитая инфрастуктура."
        result = self.censor.censor(text)
        print(result)
        self.assertEqual(result, "Я живу на [censored] в кирпичном доме. Вокруг есть развитая инфрастуктура.")

    def test_geo_censorship_2(self):
        text = "Я учусь на проспекте вернадского хорошо"
        result = self.censor.censor(text)
        self.assertEqual(result, "Я учусь на [censored] хорошо")
class FileHandlerCustom:
    def read(self, filename):
        """Читает содержимое файла"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            raise ValueError("Файл не найден")
        except Exception as e:
            raise ValueError(f"Ошибка при чтении файла: {str(e)}")

    def write(self, text, filename):
        """Сохраняет текст в файл"""
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(text)
        except Exception as e:
            raise ValueError(f"Ошибка при записи файла: {str(e)}")

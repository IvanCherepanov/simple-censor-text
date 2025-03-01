from app.adapters.file_operation.main import FileHandlerCustom
from app.domain.processors.main import TextCensor


def main():
    input_file = "../files/secret_letter.txt"
    output_file = "../files/censored_letter.txt"

    censor = TextCensor()
    handler = FileHandlerCustom()

    try:
        original_text = handler.read(input_file)
        censored_text = censor.censor(original_text)
        handler.write(censored_text, output_file)
        print(f"Обработанный текст сохранён в {output_file}")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
from faker import Faker

from app.config import FILES_INPUT_DIR


def show_greeting():
    faker = Faker("ru-RU")
    name = faker.name()
    phone_number = faker.phone_number()
    print(f"Hello {name}, your phone number {phone_number})")


def check_file_exists():
    gitkeep_file_path = FILES_INPUT_DIR.joinpath(".gitkeep")
    if gitkeep_file_path.exists():
        print(f"File exists: {gitkeep_file_path.as_uri()}")
    else:
        raise FileNotFoundError(f"File not found: {gitkeep_file_path.as_uri()}")


def main():
    show_greeting()
    check_file_exists()

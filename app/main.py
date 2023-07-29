from faker import Faker

from app.config import FILES_INPUT_DIR


def show_greeting():
    faker = Faker("ru-RU")
    name = faker.name()
    phone_number = faker.phone_number()
    print(f"Hello {name}, your phone number {phone_number})")


def main():
    show_greeting()


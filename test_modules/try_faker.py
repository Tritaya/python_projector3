
from faker import Faker

fake = Faker()


def create_user(name: str, password: str):
    print(fake.name())
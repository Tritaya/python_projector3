from faker import Faker

faker = Faker()

def create_user(name: str, password: str):
    # print(faker.name())
    # Task 1. name(login), password
    if not name:
        name = faker.name()
    if not password:
        password = faker.phone_number()
    print(f'user name is "{name}", password "{password}"')
    return name, password

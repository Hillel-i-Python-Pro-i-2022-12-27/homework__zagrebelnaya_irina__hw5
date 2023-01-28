from typing import NamedTuple
from random import randint
from faker import Faker


class User(NamedTuple):
    name: str
    email: str


fake = Faker()


def generate_entity() -> User:
    fake_name = fake.first_name()
    return User(name=fake_name, email=f"{fake_name}.{randint(100, 999)}@mail.com")


def generate_users(number):
    for _ in range(number):
        yield generate_entity()

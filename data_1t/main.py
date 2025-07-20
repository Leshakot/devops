import random
import faker


fake = faker.Faker('ru_RU')
def generate_name():
    names = fake.first_name()
    while len(names) < 4 or len(names) > 10:
        names = fake.first_name()
    return names

def generate_surname():
    return fake.last_name()

def generate_city():
    return fake.city()

def generate_age():
    return random.randint(1, 80)

data = []
for _ in range(20):
    name = generate_name()
    surname = generate_surname()
    city = generate_city()
    age = generate_age()
    data.append((name, surname, city, age))


with open('init.sql', 'w',  encoding='utf-8') as file:
    file.write("CREATE TABLE IF NOT EXISTS test_table (name VARCHAR(10), surname VARCHAR(50), city VARCHAR(50), age INT);\n")
    for name, surname, city, age in data:
        file.write(f"INSERT INTO test_table (name, surname, city, age) VALUES ('{name}', '{surname}', '{city}', {age});\n")

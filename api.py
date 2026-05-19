from fastapi import FastAPI
from random import randint, choice
import random

app = FastAPI()

FIRST_NAMES = [
    "Riz", "Adit", "Kenz", "Raf", "Niko",
    "Luna", "Miya", "Salsa", "Alya", "Vina"
]

PASSWORDS = [
    "gaming123",
    "freefire",
    "guest123",
    "indogamer",
    "password123"
]

SPECIAL_IDS = [
    "1111111111",
    "2222222222",
    "3333333333",
    "4444444444",
    "5555555555",
    "6666666666",
    "7777777777",
    "8888888888",
    "9999999999",
    "1234567890",
    "9876543210",
    "1122334455",
    "9988776655",
    "0000000000"
]


def generate_account(name, region):

    rare_chance = random.randint(1, 100)

    if rare_chance <= 8:
        account_id = random.choice(SPECIAL_IDS)
    else:
        account_id = str(randint(1000000000, 9999999999))

    uid = randint(100000000, 999999999)

    password = "LIPZX"

    return {
        "uid": uid,
        "account_id": account_id,
        "password": password,
        "region": region,
        "nickname": name
    }


@app.get("/gen")
async def generate(name: str = "Guest", count: int = 1, region: str = "ID"):

    if count > 15:
        count = 15

    results = []

    for _ in range(count):
        results.append(generate_account(name, region))

    return results

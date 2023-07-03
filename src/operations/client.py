import string
import time
import datetime
import random

import requests

API_URL = "http://localhost:8000"


def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join((random.choice(letters_and_digits) for _ in range(length)))


def insert_entries(num_entries):
    entries = [{'uuid': generate_random_string(16), 'text': 'text'} for _ in range(num_entries)]
    response = requests.post(f"{API_URL}/new", json=entries)
    if response.status_code == 201:
        print(f"{num_entries} entries inserted successfully.")
    else:
        print(f"Failed to insert entries. Error: {response.text}")


def delete_entries():
    response = requests.get(f"{API_URL}/all")
    if response.status_code == 200:
        entries = response.json()
        num_deleted = 0
        for entry in entries:
            uuid = entry["uuid"]
            response = requests.delete(f"{API_URL}/{uuid}")
            if response.status_code == 200:
                num_deleted += 1
            else:
                print(f"Failed to delete entry with UUID '{uuid}'. Error: {response.text}")

        print(f"{num_deleted} entries deleted.")
    else:
        print(f"Failed to fetch entries. Error: {response.text}")


def main():
    while True:
        num_entries = random.randint(10, 100)
        insert_entries(num_entries)
        delete_entries()
        time.sleep(10)


if __name__ == '__main__':
    main()

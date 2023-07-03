#import requests
#import random
#import string
#import time
#import uuid
#
#
#def generate_random_string(length):
#    letters_and_digits = string.ascii_letters + string.digits
#    return ''.join((random.choice(letters_and_digits) for i in range(length)))
#
#
#def insert_entries():
#    num_entries = random.randint(10, 100)
#    entries = []
#    for _ in range(num_entries):
#        entry = {
#
#            "uuid": str(uuid.uuid4()),
#            "text": generate_random_string(16)
#        }
#        entries.append(entry)
#
#    response = requests.post("http://localhost:8000/new", json=entries)
#    if response.status_code == 200:
#        print(f"{num_entries} entries inserted successfully.")
#    else:
#        print(f"Failed to insert entries. Error: {response.text}")
#
#
#def delete_entries():
#    response = requests.get("http://localhost:8000/all")
#    if response.status_code == 200:
#        entries = response.json()
#        num_deleted = 0
#        for entry in entries:
#            uuid = entry["uuid"]
#            response = requests.delete(f"http://localhost:8000/{uuid}")
#        if response.status_code == 200:
#            num_deleted += 1
#        else:
#            print(f"Failed to delete entry with UUID '{uuid}'. Error: {response.text}")
#
#        print(f"{num_deleted} entries deleted.")
#    else:
#        print(f"Failed to fetch entries. Error: {response.text}")
#
#    while True:
#  #      insert_entries()
#        delete_entries()
#  #      time.sleep(10)
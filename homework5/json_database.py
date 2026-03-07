import json
import os

FILE_NAME = "database.json"


def init_db():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            json.dump({""
            "schema": {
                "id": "int", 
                "name": "str", 
                "age": "int"
            },
            "records": [],
            "last_id": 0
            }, file, indent=4)


def load_db():
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_db(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def validate_record(record, schema):
    for field, field_type in schema.items():
        if field not in record:
            raise ValueError(f"Missing field: {field}")
        if field_type == "int" and not isinstance(record[field], int):
            raise TypeError(f"{field} must be int")
        if field_type == "str" and not isinstance(record[field], str):
            raise TypeError(f"{field} must be str")

def add_record(name, age):
    data = load_db()

    new_id = data["last_id"] + 1

    record = {
        "id": new_id,
        "name": name,
        "age": age
    }

    validate_record(record, data["schema"])

    data["records"].append(record)
    data["last_id"] = new_id

    save_db(data)


def view_records():
    data = load_db()

    for record in data["records"]:
        print(record)


def search_record(record_id):
    data = load_db()

    for record in data["records"]:
        if record["id"] == record_id:
            print("Record found:", record)
            return

    print("Record not found")


def delete_record(record_id):
    data = load_db()

    data["records"] = [
        r for r in data["records"] if r["id"] != record_id
    ]

    save_db(data)


def update_record(record_id, name=None, age=None):
    data = load_db()

    for record in data["records"]:
        if record["id"] == record_id:

            if name:
                record["name"] = name

            if age:
                record["age"] = age

    save_db(data)


init_db()

add_record("Alice", 30)
add_record("Bob", 25)

view_records()

update_record(1, age=31)

print("After update:")
view_records()

delete_record(2)

print("After delete:")
view_records()
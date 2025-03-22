import json
from collections import defaultdict
from csv import DictReader

def load_users(json_file):
    """Загружает данные пользователей из JSON-файла."""
    with open(json_file, "r") as f:
        return json.load(f)

def load_books(csv_file):
    """Загружает данные о книгах из CSV-файла."""
    books = []
    with open(csv_file, "r") as f:
        reader = DictReader(f)
        for row in reader:
            books.append(row)
    return books

def distribute_books(users, books):
    """Распределяет книги между пользователями."""
    user_books = defaultdict(list)
    num_users = len(users)
    for i, book in enumerate(books):
        user_index = i % num_users
        user_books[user_index].append(book)
    return user_books

def create_result_json(users, user_books):
    """Создает итоговый JSON-файл."""
    result = []
    for i, user in enumerate(users):
        user["books"] = user_books[i]
        result.append(user)
    return result

def main():
    users = load_users("/home/admin1/Otus/users.json")
    books = load_books("/home/admin1/Otus/books.csv")

    user_books = distribute_books(users, books)

    result = create_result_json(users, user_books)

    with open("result.json", "w") as f:
        json.dump(result, f, indent=4)

if __name__ == "__main__":
    main()
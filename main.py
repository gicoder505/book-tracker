import json

BOOKS_FILE = "books.json"


def load_books():
    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_books(books):
    with open(BOOKS_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)


def add_book(books):
    pass  # реализовано в ветке feature/add-book


def list_books(books):
    if not books:
        print("Список книг пуст.")
        return
    print("\n=== Список прочитанных книг ===")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['название']} — {book['автор']} | Оценка: {book['оценка']} | Дата: {book['дата']}")


def average_rating(books):
    if not books:
        print("Нет книг для расчёта средней оценки.")
        return
    avg = sum(b["оценка"] for b in books) / len(books)
    print(f"\nСредняя оценка по всем книгам: {avg:.2f}")


def author_stats(books):
    if not books:
        print("Нет книг для статистики.")
        return
    stats = {}
    for book in books:
        author = book["автор"]
        stats[author] = stats.get(author, 0) + 1
    print("\n=== Статистика по авторам ===")
    for author, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
        print(f"  {author}: {count} кн.")


def delete_book(books):
    pass  # реализовано в ветке feature/delete


def show_menu():
    print("\n=== Трекер прочитанных книг ===")
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Показать среднюю оценку")
    print("4. Статистика по авторам")
    print("5. Удалить книгу")
    print("6. Выход")


def main():
    while True:
        show_menu()
        choice = input("Выберите пункт меню: ").strip()

        if choice == "1":
            books = load_books()
            add_book(books)
        elif choice == "2":
            books = load_books()
            list_books(books)
        elif choice == "3":
            books = load_books()
            average_rating(books)
        elif choice == "4":
            books = load_books()
            author_stats(books)
        elif choice == "5":
            books = load_books()
            delete_book(books)
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный пункт. Попробуйте снова.")


if __name__ == "__main__":
    main()

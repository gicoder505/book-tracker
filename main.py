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
    author = input("Автор: ").strip()
    title = input("Название: ").strip()

    for existing in books:
        if existing["автор"].lower() == author.lower() and existing["название"].lower() == title.lower():
            print(f"Книга '{title}' автора '{author}' уже существует в трекере.")
            return

    while True:
        try:
            rating = int(input("Оценка (1-5): ").strip())
            if 1 <= rating <= 5:
                break
            print("Оценка должна быть от 1 до 5.")
        except ValueError:
            print("Введите целое число от 1 до 5.")
    date_read = input("Дата прочтения (дд.мм.гггг): ").strip()

    book = {"автор": author, "название": title, "оценка": rating, "дата": date_read}
    books.append(book)
    save_books(books)
    print(f"Книга '{title}' добавлена.")


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
            pass  # TODO: показать все книги
        elif choice == "3":
            pass  # TODO: средняя оценка
        elif choice == "4":
            pass  # TODO: статистика по авторам
        elif choice == "5":
            pass  # TODO: удалить книгу
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный пункт. Попробуйте снова.")


if __name__ == "__main__":
    main()

import json
import os
from datetime import datetime

# Функция для создания новой заметки
def create_note():
    note = {}
    note["id"] = input("Введите идентификатор заметки: ")
    note["title"] = input("Введите заголовок заметки: ")
    note["content"] = input("Введите текст заметки: ")
    note["timestamp"] = str(datetime.now())

    # Проверка наличия файла с заметками
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as file:
            notes = json.load(file)
    else:
        notes = []

    # Добавление новой заметки в список
    notes.append(note)

    # Сохранение списка заметок в файл
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)

    print("Заметка успешно создана.")

# Функция для просмотра существующих заметок
def view_notes():
    # Проверка наличия файла с заметками
    if not os.path.exists("notes.json"):
        print("Нет доступных заметок.")
        return

    with open("notes.json", "r") as file:
        notes = json.load(file)

        if not notes:
            print("Нет доступных заметок.")
            return

        print("Доступные заметки:")
        for note in notes:
            print(f"- {note['id']}: {note['title']}")

        note_id = input("Введите идентификатор заметки для просмотра: ")

        for note in notes:
            if note["id"] == note_id:
                print("\nИнформация о заметке:")
                print(f"Заголовок: {note['title']}")
                print(f"Текст: {note['content']}")
                print(f"Дата/время создания: {note['timestamp']}")
                return

        print("Заметка не найдена.")

# Функция для редактирования заметки
def edit_note():
    # Проверка наличия файла с заметками
    if not os.path.exists("notes.json"):
        print("Нет доступных заметок.")
        return

    with open("notes.json", "r") as file:
        notes = json.load(file)

        if not notes:
            print("Нет доступных заметок.")
            return

        print("Доступные заметки:")
        for note in notes:
            print(f"- {note['id']}: {note['title']}")

        note_id = input("Введите идентификатор заметки для редактирования: ")

        for note in notes:
            if note["id"] == note_id:
                note["title"] = input("Введите новый заголовок заметки: ")
                note["content"] = input("Введите новый текст заметки: ")
                note["timestamp"] = str(datetime.now())

                # Сохранение списка заметок в файл
                with open("notes.json", "w") as file:
                    json.dump(notes, file)
                    
# Функция для удаления заметки
def delete_note():
    # Проверка наличия файла с заметками
    if not os.path.exists("notes.json"):
        print("Нет доступных заметок.")
        return

    with open("notes.json", "r") as file:
        notes = json.load(file)

        if not notes:
            print("Нет доступных заметок.")
            return

        print("Доступные заметки:")
        for note in notes:
            print(f"- {note['id']}: {note['title']}")

        note_id = input("Введите идентификатор заметки для удаления: ")

        for note in notes:
            if note["id"] == note_id:
                notes.remove(note)

                # Сохранение списка заметок в файл
                with open("notes.json", "w") as file:
                    json.dump(notes, file, indent=4)

                print("Заметка успешно удалена.")
                return

        print("Заметка не найдена.")
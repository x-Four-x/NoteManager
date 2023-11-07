from models import Note
from utils_db import (create_note, create_table, delete_note, get_all_notes,
                      get_note)


def _create_note():
    """Функция для создания заметки"""
  
    title = input('Введите заголовок заметки: ')
    description = input('Введите описание заметки: ')

    create_note(
        title=title,
        description=description
    )

    print('Заметка была создана!')


def _get_all_notes():
    """Функция для получения конкретной заметки по ID"""

    for i, note in enumerate(get_all_notes()):
        print(f'#{i + 1} | {note.title}')


def _delete_note():
    """Функция для удаления заметки по ID"""
    notes = get_all_notes()

    for i, note in enumerate(notes):
        print(f'#{i + 1} | {note.title}')

    note_delete_id = input('Введите номер заметки которую вы хотите удалить: ')

    if not note_delete_id.isdigit():
        print('\nВведите корректный номер!\n')
        return

    try:
        list(notes)[int(note_delete_id) - 1]
    except IndexError:
        print('\nТакой заметки не существует!\n')
        return

    delete_note(notes[int(note_delete_id) - 1].note_id)

    print('Заметка успешно удалена!')


def _get_note():
    """Функция для получения заметки по ее ID"""
    notes = get_all_notes()

    for i, note in enumerate(notes):
        print(f'#{i + 1} | {note.title}')

    note_id = input('Введите номер заметки которую вы хотите получить: ')

    if not note_id.isdigit():
        print('\nВведите корректный номер!\n')
        return

    try:
        list(notes)[int(note_id) - 1]
    except IndexError:
        print('\nТакой заметки не существует!\n')
        return

    note = get_note(notes[int(note_id) - 1].note_id)

    print(
        f'Заголовок: {note.title}\n'
        f'Описание: {note.description}'
    )


def _find_notes():
    """Функция для поиска заметки"""

    search_value = input('Введите слово или фразу по которой нужно найти заметки: ')
    notes = get_all_notes().where(Note.title.contains(search_value))  # Поиск заметки по фразе/слову

    if not len(notes):
        print(f'Заметки по запросу "{search_value}" не найдены!')
        return
    
    print(f'Заметки по запросу "{search_value}":')

    for i, note in enumerate(notes):
        print(f'#{i + 1} | {note.title}')


def main():
    """
    Главная функция в коде, запускает бесконечный цикл, с выбором действий с заметками 
    """

    while True:
        print(
            'Что будем делать?\n'
            '1. Добавить заметку\n'
            '2. Искать заметку\n'
            '3. Вывести список заметок\n'
            '4. Удалить заметку\n'
            '5. Просмотреть заметку'
        )
        option = input('Выберите вариант: ')

        if not option.isdigit():
            print('\nВведите корректный вариант!\n')
            continue

        option_actions = {
            1: _create_note,
            2: _find_notes,
            3: _get_all_notes,
            4: _delete_note,
            5: _get_note
        }

        option_actions.get(
            int(option),
            lambda: print('\nТакого варианта нет!\n')
        )()  # Вызов конкретной функции




if __name__ == '__main__':
    create_table()
    main()

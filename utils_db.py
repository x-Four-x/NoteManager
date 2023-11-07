from models import Note


def create_table() -> None:
    """Создает таблицу в базе данных"""
    Note.create_table()

def get_note(note_id: int) -> Note | None:
    """Возвращает обьект записи в базе данных или None"""
    return Note.get_or_none(
        note_id=note_id
    )

def create_note(title: str, description: str) -> Note:
    """Создает заметку в базе данных"""
    return Note.create(
        title=title, 
        description=description
    )

def delete_note(note_id: int) -> None:
    """Удаляет заметку в базе данных"""
    Note.delete_by_id(note_id)

def get_all_notes() -> list[Note]:
    """Возвращает все имеющиеся заметки в базе данных"""
    return Note.select()

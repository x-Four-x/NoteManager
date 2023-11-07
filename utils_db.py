from models import Note


def create_table() -> None:
    Note.create_table()

def get_note(note_id: int) -> Note | None:
    return Note.get_or_none(
        note_id=note_id
    )

def create_note(title: str, description: str) -> Note:
    return Note.create(
        title=title, 
        description=description
    )

def delete_note(note_id: int) -> None:
    Note.delete_by_id(note_id)

def get_all_notes() -> list[Note]:
    return Note.select()

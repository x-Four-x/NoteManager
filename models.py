from peewee import *


db = SqliteDatabase('./database.db')


class Note(Model):
    note_id = AutoField()
    title = CharField(
        max_length=35,
        null=False
    )
    description = TextField(
        null=False
    )

    class Meta:
        database = db
        db_column = 'notes'

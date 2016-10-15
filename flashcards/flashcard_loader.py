import os
import simplejson as json

from db_access import DBAccess


class FlashcardLoader(DBAccess):
    """Loads flashcards from file and inserts into the database."""

    def _load_flashcard(self, file_path):
        with open(file_path, 'r') as f:
            flashcard_json = json.load(f)
            # TODO: Add calls to properly add flashcards to the database

    def load_flashcards(self, directory_name):
        for dirpath, dir_names, file_names in os.walk(directory_name):
            for file_name in file_names:
                full_file_path = os.path.join(dirpath, file_name)
                self._load_flashcard(full_file_path)

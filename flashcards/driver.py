from flashcard_loader import FlashcardLoader
from quiz import Quiz


def run():
    flashcard_loader = FlashcardLoader()
    flashcard_loader.load_flashcards('data')
    quiz = Quiz()
    user_continuing = True
    while quiz.get_next_flashcard(True) or user_continuing:
        next_card = quiz.get_next_flashcard()
        correct_choice = raw_input()

        quiz.answer_question(next_card, correct_choice)


if __name__ == '__main__':
    run()

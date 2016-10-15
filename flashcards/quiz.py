from datetime import datetime, timedelta
import heapq

from config import LEITNER_BOX_TIMES
from db_access import DBAccess


class Quiz(DBAccess):

    def __init__(self):
        super(Quiz, self).__init__()
        self.leitner_boxes = [[]]

    def get_next_flashcard(self, peek_only=False):
        """Get the next flashcard to study based on the next review time.
        Args:
            peek_only (bool, optional): whether we want to see if there is a card available for quizzing without changing
                                        Leitner boxes
        Returns:
             FlashcardProgress model indicating Flashcard to review if cards are available to review; None otherwise
        """
        for box in self.leitner_boxes:
            if datetime.now() > box[0].next_review_time:
                if peek_only:
                    next_card = heapq.nsmallest(1, box) if heapq.nsmallest(1, box) else None
                else:
                    next_card = heapq.heappop(box)
                return next_card

    def answer_question(self, flashcard_progress, correct):
        """
        Args:
            flashcard_progress (FlashcardProgress): the FlashcardProgress object that is connected to the Flashcard
                                                    object that the user saw
            correct (bool): whether the response was correct
        Returns:
            None
        """
        if correct:
            if flashcard_progress.leitner_box in range(0, len(self.leitner_boxes)):
                flashcard_progress.leitner_box += 1
        else:
            # If the user does not correctly recall the back text of the flashcard,
            # send the card back to the first Leitner box for review
            flashcard_progress.leitner_box = 0

        flashcard_progress.next_review_time = datetime.now() + timedelta(seconds=LEITNER_BOX_TIMES[flashcard_progress.leitner_box])
        heapq.heappush(self.leitner_boxes[flashcard_progress.leitner_box], flashcard_progress)

        self.session.add(flashcard_progress)
        self.session.commit()

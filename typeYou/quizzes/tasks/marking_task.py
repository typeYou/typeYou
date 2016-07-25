from celery import Task
from quizzes.models import Quiz


class MarkingTask(Task):

    def run(self, quiz):
        for answer in quiz.answer_set.public():
            if answer.ans == answer.question.correct_ans:
                answer.correct = True
            else:
                answer.correct = False
            answer.save()

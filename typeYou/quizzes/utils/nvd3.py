def get_answers_of_each_question(quiz):
    """
    Collect all example answers of each question relevant to the inputted quiz
    """
    data = [
        [
            question.get_ans(index+1)
            for index, _
            in enumerate(range(4))
        ]
        for question
        in quiz.question_set.public()
    ]
    return data


def count_each_answer(quiz):
    """
    Counts how many times is each answer selected
    """
    data = [
        [
            question.answer_set.public().filter(ans=question.get_ans(index+1)).count()
            for index, answer
            in enumerate(question.answer_set.public())
        ]
        for question
        in quiz.question_set.public()
    ]

    return data


def create_chart_data_set(quiz):
    """
    generate data_set for django-nvd3 pieChart
    """
    xdata = quiz.get_answers_of_each_question(quiz)
    ydata = quiz.count_each_answer(quiz)

    data_set = [
        {
            'title': question.title,
            'charttype': "pieChart",
            'chartdata': {'x': xdata[index], 'y': ydata[index]},
            'chartcontainer': str(question.id),
            'extra': {
                'x_is_date': False,
                'x_axis_format': '',
                'tag_script_js': True,
                'jquery_on_ready': False,
            }
        }
        for index, question
        in enumerate(quiz.question_set.public())
    ]

    return data_set

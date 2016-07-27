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
    xdata = get_answers_of_each_question(quiz)
    ydata = count_each_answer(quiz)

    color_list = ['#247BA0', '#70C1B3', '#B2DBBF', '#F3FFBD', '#FF1654', ]
    extra_serie = {"color_list": color_list}

    data_set = [
        {
            'title': question.title,
            'charttype': "pieChart",
            'chartdata': {'x': xdata[index], 'y': ydata[index], 'extra': extra_serie},
            'chartcontainer': "question_{id}".format(id=question.id),
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

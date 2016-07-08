migrate:
	- python typeYou/manage.py makemigrations users quizzes
	- python typeYou/manage.py migrate

test:
	- pep8 .
	- python typeYou/manage.py test typeYou users quizzes

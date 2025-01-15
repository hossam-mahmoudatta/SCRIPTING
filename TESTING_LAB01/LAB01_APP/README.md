# Python Testing Environment 01

python -m venv TEST_ENVIRONMENT_NAME

pip freeze

pip install flask

pip freeze > requirements.txt

pip install -r requirements.txt

pip freeze

pip install coverage

coverage run -m unittest FILENAME.py

coverage html


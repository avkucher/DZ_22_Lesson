FROM python:3.10


WORKDIR /code
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
COPY dao .
COPY service .
COPY views .
COPY app.py .
COPY config.py .
COPY database.py .
COPY movies.db .
COPY realisation.py .

CMD flask run -h 0.0.0.0 -p 80



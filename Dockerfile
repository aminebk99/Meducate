FROM python:latest

WORKDIR /app

COPY src/requirements.txt .

RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

CMD [ "python", "app.py" ]
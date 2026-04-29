FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV APP_MESSAGE="Codespaces Docker çalışıyor"

EXPOSE 5000

CMD ["python", "app.py"]

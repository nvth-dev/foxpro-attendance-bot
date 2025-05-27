FROM python:3.9

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["python", "bot.py"]
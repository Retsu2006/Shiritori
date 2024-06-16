FROM python:3.9-slim

WORKDIR /siritori

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "server.py"]

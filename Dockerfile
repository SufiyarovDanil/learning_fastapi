FROM python:3.12

RUN mkdir /learning_fastapi

WORKDIR /learning_fastapi

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD alembic revision --autogenerate -m "init" && alembic upgrade heads && cd src && uvicorn main:app --host 0.0.0.0 --port 4127

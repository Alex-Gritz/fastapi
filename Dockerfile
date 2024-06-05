FROM python:3.10

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY . .

RUN pip install -r requirements

RUN apt-get update && apt-get install -y tesseract-ocr

WORKDIR .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
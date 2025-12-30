FROM python:3.13-rc

WORKDIR /fastapi

COPY ./requirements.txt /fastapi/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /fastapi/requirements.txt

COPY ./app /fastapi/app

ENV DB_CONN=postgresql://wojtek359:0994_088ad6@psql01.mikr.us/db_wojtek359

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
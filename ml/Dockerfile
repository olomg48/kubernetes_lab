FROM python:3.13-rc

WORKDIR /ml

COPY ./requirements.txt /ml/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /ml/requirements.txt

COPY . /ml

CMD ["python", "/ml/train_and_push.py"]
FROM python:3.8-slim
WORKDIR /code
COPY . /code
RUN pip install Flask redis rq
CMD ["python", "app.py"]

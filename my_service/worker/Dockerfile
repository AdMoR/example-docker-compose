FROM python:3.7-alpine
WORKDIR /code
COPY . .
RUN pip install -e .
CMD ["python", "/code/my_service/worker/worker.py"]

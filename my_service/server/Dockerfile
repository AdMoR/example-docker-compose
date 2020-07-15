FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP my_service/server/app.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY . .
RUN pip install -e .
CMD ["flask", "run"]

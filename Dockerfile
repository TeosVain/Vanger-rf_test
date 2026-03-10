FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY req.pip /app/req.pip
RUN pip install --no-cache-dir -r /app/req.pip

COPY app /app/app

RUN mkdir -p /app/media /app/staticfiles

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--chdir", "app", "--bind", "0.0.0.0:8000"]

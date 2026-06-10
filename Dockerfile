FROM python:3.12-bookworm

WORKDIR /app

RUN sed -i 's|http://deb.debian.org|https://deb.debian.org|g' \
    /etc/apt/sources.list.d/debian.sources || true

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    pkg-config

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD sh -c "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn student_system.wsgi:application --bind 0.0.0.0:$PORT"
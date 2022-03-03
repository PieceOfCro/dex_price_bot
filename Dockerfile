FROM python:3.9-slim

WORKDIR /app

COPY ./requirements.txt .

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libgcc-10-dev libc6-dev\
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir --upgrade -r requirements.txt \
    && apt-get purge -y --auto-remove gcc libgcc-10-dev libc6-dev

COPY dex_price_bot/*.py /app/

CMD ["python", "main.py", "-c", "/config.yaml"]
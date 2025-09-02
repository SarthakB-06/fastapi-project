FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir scikit-learn==1.6.1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
FROM python:3.9

WORKDIR /usr/src/app

COPY requirments.txt .

RUN pip install -r requirments.txt

COPY main.py .
COPY ml_obj_detection.py .
COPY templates ./templates

EXPOSE 8000

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
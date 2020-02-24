FROM python:latest
WORKDIR /usr/app/url_shortener
COPY ./* ./
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]

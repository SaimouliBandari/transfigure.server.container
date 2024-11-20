FROM python:3

COPY src ./

COPY requirements.txt ./

RUN pip install --upgrade --no-deps --force-reinstall -r requirements.txt

COPY . .

CMD ["python3" , "src/app.py"]

EXPOSE 8080
FROM python:3.10.11-slim as compile-so
RUN apt update
RUN apt install -y --fix-missing build-essential
RUN apt install -y libpq-dev

FROM compile-so as compile-image
COPY requirements.txt .
RUN pip install --user  -r requirements.txt

FROM compile-libpq-dev
EXPOSE 5000
EXPOSE 5432
WORKDIR /app
ADD . /app
COPY --from=compile-image /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]

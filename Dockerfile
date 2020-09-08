FROM python
RUN apt-get update && \
	apt-get upgrade -y && \
	apt-get install redis -y

RUN python -m pip install --upgrade pip

ENV FLASK_APP "wife_alert"
ENV APP_CONFIG "wife_alert.config.Production"


COPY pyproject.toml .
RUN pip3 install poetry RPi.GPIO
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY wife_alert .

CMD ["python", "flask", "run"]

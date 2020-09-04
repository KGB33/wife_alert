FROM archlinux
RUN pacman -Syu redis python python-pip --noconfirm

ENV FLASK_APP "wife_alert"
ENV APP_CONFIG "wife_alert.config.production"


COPY pyproject.toml .
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY wife_alert .

CMD ["python", "flask", "run"]

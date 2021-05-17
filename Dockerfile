FROM python:3.7
RUN pip install pipenv

ENV DJANGO_ENV=production \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PIPENV_HIDE_EMOJIS=true \
    PIPENV_COLORBLIND=true \
    PIPENV_NOSPIN=true \
    PIPENV_DOTENV_LOCATION=.env


COPY Pipfile* /
# RUN cd /tmp && pipenv lock --keep-outdated --requirements > requirements.txt
RUN pipenv lock --requirements > requirements.txt
RUN pipenv install  --deploy --system --ignore-pipfile
# always copy files after installing packages 
# docker will cache the packages hence better build time
ADD ./ready /ready
RUN chmod +x /ready

ADD ./migrate_and_run /migrate_and_run
RUN chmod +x /migrate_and_run


ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait
WORKDIR /ccd_server
COPY . /ccd_server
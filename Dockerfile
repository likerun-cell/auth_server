FROM python:3.6.8-slim

MAINTAINER amos.thh@gmail.com

ENV PYTHONUNBUFFERED 1
COPY . /app/
WORKDIR /app
COPY entrypoint.sh /entrypoint.sh

RUN chmod 755 /entrypoint.sh && sed -i "s@http://deb.debian.org@http://mirrors.aliyun.com@g" /etc/apt/sources.list \
    && rm -Rf /var/lib/apt/lists/* && apt-get update && apt-get install vim -y \
    && apt-get install -y libc6-dev gcc mime-support

RUN pip install -i "https://pypi.tuna.tsinghua.edu.cn/simple" pipenv && pipenv install

ENTRYPOINT ["/entrypoint.sh"]

CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
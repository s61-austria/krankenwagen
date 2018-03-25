FROM python:3.6-alpine
LABEL maintainer="David Diks"
COPY ./ /src
RUN pip install -r /src/requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "/src/src/web.py"]
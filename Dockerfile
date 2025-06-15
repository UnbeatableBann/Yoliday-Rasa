FROM rasa/rasa:3.6.21
WORKDIR /app
USER root

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY --chown=rasa:rasa . .
COPY --chown=rasa:rasa start.sh ./
RUN chmod +x start.sh

USER rasa

ENTRYPOINT []
CMD ["./start.sh"]
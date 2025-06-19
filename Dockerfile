FROM rasa/rasa:3.6.21
WORKDIR /app
USER root

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt 

COPY --chown=rasa:rasa . .
COPY --chown=rasa:rasa start.sh ./
RUN chmod +x start.sh

USER rasa

EXPOSE 5005

ENTRYPOINT []
CMD ["./start.sh"]
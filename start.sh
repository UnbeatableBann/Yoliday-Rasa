#!/bin/bash
echo "Starting Rasa server... $PORT"
rasa run actions &
rasa run --enable-api --cors "*" --port $PORT

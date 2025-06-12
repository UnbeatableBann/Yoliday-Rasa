#!/bin/sh
rasa run --enable-api --connector rest --port 5005 --cors "*" &
sleep 8
rasa run actions --port 5055
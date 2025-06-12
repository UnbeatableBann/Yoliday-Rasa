FROM rasa/rasa:3.6.21

# Set working directory
WORKDIR /app

# Copy all files to container
COPY . /app

# Install extra dependencies (run as root)
USER root
RUN apt-get update && \
    apt-get install --no-install-recommends -y gcc make libpq-dev build-essential && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy start script
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

USER 1001
EXPOSE 5005 
EXPOSE 5055

ENTRYPOINT ["/app/start.sh"]

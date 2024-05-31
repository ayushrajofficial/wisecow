# Use an official lightweight Debian-based image
FROM debian:latest

# Install necessary packages
RUN apt-get update && apt-get install -y \
    bash \
    cowsay \
    fortune \
    netcat-openbsd \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the application script into the container
COPY wisecow.sh /usr/local/bin/wisecow.sh

# Make the script executable
RUN chmod +x /usr/local/bin/wisecow.sh

# Expose the port the application runs on
EXPOSE 4499

# Command to run the application
CMD ["/usr/local/bin/wisecow.sh"]



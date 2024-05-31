# Use an official lightweight base image
FROM alpine:latest

# Install necessary packages
RUN apk update && apk add --no-cache \
    bash \
    cowsay \
    fortune \
    netcat-openbsd

# Copy the application script into the container
COPY serve.sh /usr/local/bin/serve.sh

# Make the script executable
RUN chmod +x /usr/local/bin/serve.sh

# Expose the port the application runs on
EXPOSE 4499

# Command to run the application
CMD ["/usr/local/bin/serve.sh"]

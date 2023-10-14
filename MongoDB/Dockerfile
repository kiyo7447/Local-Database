# Use an official MongoDB runtime as a parent image
FROM mongo:latest

# Set environment variables
ENV MONGO_INITDB_ROOT_USERNAME=admin \
    MONGO_INITDB_ROOT_PASSWORD=password

# Expose port 27017 for MongoDB
EXPOSE 27017

# Copy the MongoDB configuration file to the container
COPY mongod.conf /etc/mongod.conf

# Start MongoDB with the configuration file
CMD ["mongod", "--config", "/etc/mongod.conf"]

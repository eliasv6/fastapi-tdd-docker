# pull official base image
FROM postgres:17

# run create.sql on init
# extend the postgres image by adding create.sql to the
# docker-entrypoint-initdb.d directory in the container
# Will execute on init
ADD create.sql /docker-entrypoint-initdb.d
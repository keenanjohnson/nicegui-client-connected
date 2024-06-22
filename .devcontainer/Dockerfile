FROM python:3.12

# Install python requirements for GUI folder.
COPY ./requirements.txt /tmp/
RUN python3 -m pip install -r /tmp/requirements.txt


##############################################################################
# Install Packages
##############################################################################
RUN apt-get update && apt-get install -y \
    pkg-config \
    iputils-ping

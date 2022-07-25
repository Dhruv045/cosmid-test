FROM ghcr.io/skylab-devs/cosmic:squashed
RUN mkdir /cosmos && chmod 777 /cosmos && git clone https://github.com/SkyLab-Devs/Cosmid-Test -b starfire /cosmos
WORKDIR /cosmos
CMD ["python3","-m","bot"]

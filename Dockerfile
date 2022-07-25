FROM ghcr.io/skylab-devs/cosmic:squashed
RUN mkdir /cosmos && chmod 777 /cosmos && git clone https://github.com/arshsisodiya/cosmid-test -b starfire /cosmos
WORKDIR /cosmos
CMD ["python3","-m","bot"]

FROM ubuntu:xenial

RUN apt-get update && apt-get install -y wget lsb-release

RUN wget https://repo.percona.com/apt/percona-release_0.1-6.$(lsb_release -sc)_all.deb && \
    dpkg -i percona-release_0.1-6.$(lsb_release -sc)_all.deb && \
    rm -v percona-release_0.1-6.$(lsb_release -sc)_all.deb

RUN apt-get update && apt-get install -y percona-xtradb-cluster-garbd-5.7

CMD garbd -a gcomm://${NODES}?pc.wait_prim=no -g ${CLUSTER}

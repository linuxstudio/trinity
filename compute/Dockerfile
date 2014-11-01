FROM centos:latest
MAINTAINER hans.then@clustervision.com
RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-2.noarch.rpm
RUN yum -y install openssh-server openssh-clients python-pip vim-minimal infiniband-diags munge rsyslog bind-utils perl perl-DBI perl-Switch
RUN yum -y groupinstall "Infiniband Support"
RUN echo "root:system" | chpasswd && pip install supervisor
RUN mkdir -p /var/run/sshd ; chmod -rx /var/run/sshd
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key
RUN sed -ri 's/^#PermitRootLogin yes/PermitRootLogin yes/g' /etc/ssh/sshd_config 
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config
RUN useradd slurm
RUN mkdir /var/slurm; chown slurm /var/slurm
RUN mkdir -m 755 -p /var/run/munge
RUN chown munge /var/run/munge
ADD supervisord.conf /usr/etc/supervisord.conf
CMD ["/usr/bin/supervisord", "-c", "/usr/etc/supervisord.conf"]
ADD rpms /rpms
RUN rpm -ivh /rpms/*.rpm

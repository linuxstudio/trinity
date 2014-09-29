FROM centos:centos6
RUN yum -y install wget
# ADD does not work, it retrieves some html file.
RUN wget http://sourceforge.net/projects/xcat/files/yum/2.8/xcat-core/xCAT-core.repo -O /etc/yum.repos.d/xCAT-core.repo
RUN wget http://sourceforge.net/projects/xcat/files/yum/xcat-dep/rh6/x86_64/xCAT-dep.repo -O /etc/yum.repos.d/xCAT-dep.repo
RUN yum -y install xCAT
ADD tables /tmp/tables
#RUN yum -y install mariadb-server mariadb mariadb-bench mariadb-devel mariadb-connector-odbc perl-DBD-MySQL
#RUN service xcatd start; source /etc/profile.d/xcat.sh; XCATMYSQLADMIN_PW=system XCATMYSQLROOT_PW=system /opt/xcat/bin/mysqlsetup -i
RUN service xcatd start; source /etc/profile.d/xcat.sh; /opt/xcat/sbin/restorexCATdb -p /tmp/tables


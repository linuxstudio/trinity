FROM centos:latest
RUN yum -y install openldap-servers
RUN cp /usr/share/openldap-servers/DB_CONFIG.example /var/lib/ldap/DB_CONFIG
ADD slapd.d /etc/openldap/slapd.d

#!/usr/bin/env python
from distutils.core import setup

setup ( 
  name='Trinity-API',
  version='0.1.0',
  description='Trinity HPC server',
  url='http://www.clustervision.com',
  author='Abhishek Mukherjee',
  author_email='abhishek.mukherjee@clustervision.com',
  packages=['trinity-api'],
  package_dir={'trinity-api':'src'},
  scripts=['bin/trinity-api','bin/wrapper-trinity-api'],
  data_files=[
    ('/etc/init.d',['init/trinity-api']),
    ('/etc/trinity',['conf/trinity-api.conf'])
  ]
)

import os
import etcd
import jinja2

class EtcClientWrapper:
    def __init__(self, client):
        self.client = client

    def get(self, key):
        result = self.client.read(key)
        if result:
            return result.value

    __getitem__ = get

    
client = etcd.Client()
wrapper = EtcClientWrapper(client)

print wrapper["/mykey"]

templatedir = "./templates"
targetdir = "./target/"

for dir, _, files in os.walk(templatedir):
    print dir
    dir = dir[len(templatedir):]
    print dir
    for fname in files:
        print "Processing %s/%s" % (dir, fname)
        file = open("%s/%s/%s" % (templatedir, dir, fname))
        template = jinja2.Template(file.read())
        path = os.path.abspath(targetdir + dir)
        if not os.path.exists(path):
            os.makedirs(targetdir + dir)
        file = open(targetdir + "%s/%s" % (dir, fname), "w")
        print >> file, template.render(client=wrapper)


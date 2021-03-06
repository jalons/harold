from twisted.application import service

from conf import HaroldConfiguration
import plugin

# read configuration
config = HaroldConfiguration("harold.ini")

# load the service modules
plugins = plugin.load_plugins(config)

# build the application
application = service.Application("Harold")
for p in plugins:
    for svc in p.services:
        svc.setServiceParent(application)

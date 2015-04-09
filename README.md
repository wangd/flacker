How to use:
import flacker
server = flacker.create_app() # create_app(config) if you have a FLACKER_CONFIG
server.run()
# "server" is a flask server obj. Port, etc. are configurable: help(server)

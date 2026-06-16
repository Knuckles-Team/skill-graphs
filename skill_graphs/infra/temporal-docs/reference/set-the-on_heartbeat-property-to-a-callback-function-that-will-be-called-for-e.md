# Set the `on_heartbeat` property to a callback function that will be called for each Heartbeat sent by the Activity.
env.on_heartbeat = lambda *args: heartbeats.append(args[0])

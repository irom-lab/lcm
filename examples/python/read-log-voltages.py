import sys
import lcm

from exlcm import voltages_t

if len(sys.argv) < 2:
    sys.stderr.write("usage: read-log <logfile>\n")
    sys.exit(1)

log = lcm.EventLog(sys.argv[1], "r")

for event in log:
    if event.channel == "VOLTAGES":
        msg = voltages_t.decode(event.data)
        print("Message:")
        print("   timestamp   = %s" % str(event.timestamp))
        print("   voltages    = %s" % str(msg.voltages))
        print("")
import urllib2
from jnpr.junos import Device
import json

# Config
slackURL = "https://hooks.slack.com/services/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"

# Create JUNOS Device
dev = Device('192.168.0.133', user='root', passwd='MySRX123!')
dev.open()

# Get Hostname
hostname = dev.facts['hostname']

# Get Interface Information
ip = interfaces = dev.rpc.get_interface_information(interface_name="lo0.0").xpath('//ifa-local')[0].text.strip()

# Get Rollback
show_compare = dev.rpc.get_rollback_information(rollback='0', compare='1').xpath('//configuration-output')[0].text

# JSON Data for request
jsonData = {
    'channel': '#general',
    'text': "%s (%s) - A commit has occurred:\n%s" % (hostname, ip, show_compare)
}

# Slack API Webhook Call
req = urllib2.Request(slackURL)
req.add_header('Content-Type', 'application/json')
urllib2.urlopen(req, json.dumps(jsonData))


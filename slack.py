import urllib2
from jnpr.junos import Device
import json

# Config
slack_url = "https://hooks.slack.com/services/xxxxxx/yyyyyy/zzzzzzzzzzzzzz"
slack_channel = "#general"
device_ip = "xxx.xxx.xxx.xxx"
username = 'yyyyyy'
password = 'zzzzzz'

# Create JUNOS Device
dev = Device(device_ip, user=username, passwd=password)
dev.open()

# Get Hostname
hostname = dev.facts['hostname']

# Get Rollback
show_compare = dev.rpc.get_rollback_information(rollback='0', compare='1').xpath('//configuration-output')[0].text

# JSON Data for request
jsonData = {
    'channel': slack_channel,
    'text': "%s (%s) - A commit has occurred:\n%s" % (hostname, device_ip, show_compare)
}

# Slack API Webhook Call
req = urllib2.Request(slack_url)
req.add_header('Content-Type', 'application/json')
urllib2.urlopen(req, json.dumps(jsonData))


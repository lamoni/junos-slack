
# Setup Instructions
## 1 - Modify config variables in slack.py to match your Slack "incoming webhook" url, device's lo0 address, and device credentials

## 2 - Copy slack.py to device's /var/db/script/op/ directory

## 3 - Enable On-box Python, netconf, and configure event policy
```
set system scripts language python
set system scripts op file slack.py
set system services netconf ssh
set event-options policy Junos-Slack events UI_COMMIT_COMPLETED
set event-options policy Junos-Slack then execute-commands commands "op slack"
```

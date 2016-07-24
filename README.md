
# Setup Instructions
## 1 - Modify "slackURL" variable in slack.py to match your Slack "incoming webhook" url

## 2 - Copy slack.py to device's /var/db/script/op directory

## 3 - Enable On-box Python and configure event policy
```
set system scripts language python
set event-options policy Junos-Slack events UI_COMMIT_COMPLETED
set event-options policy Junos-Slack then execute-commands commands "op slack"
```

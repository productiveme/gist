#!/bin/bash

MouseIdentifierString="Mouse"

writeOpts() {
    sudo cat <<'EOF' | sudo tee -a /var/lib/bluetooth/$1/$2/info
[ConnectionParameters]
MinInterval=6
MaxInterval=7
Latency=0
Timeout=216
EOF
    sudo systemctl restart bluetooth
}

eachDev() {

    if sudo grep -q $MouseIdentifierString /var/lib/bluetooth/$1/$2/info
    then
        if ! sudo grep -q "ConnectionParameters" /var/lib/bluetooth/$1/$2/info
        then
            writeOpts $1 $2
        fi
    fi
}

eachCtrl() {
    sudo ls -1 /var/lib/bluetooth/$1 | egrep -v "(cache|settings)" | while read dev; do
        eachDev $1 $dev
    done
}

ls -1 /var/lib/bluetooth | while read ctrl; do
    eachCtrl $ctrl
done
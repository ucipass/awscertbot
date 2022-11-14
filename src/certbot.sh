#!/bin/sh
certbot -d $CERTIFICATE_FQDN \
--text --non-interactive --agree-tos --email $CERTIFICATE_EMAIL \
--manual-public-ip-logging-ok \
--manual --preferred-challenges dns \
--manual-auth-hook /awscertbot/auth-hook.py \
--manual-cleanup-hook /awscertbot/cleanup-hook.py \
certonly

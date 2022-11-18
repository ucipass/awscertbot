# Main purpose
Containerized application to automatically generate and renew letsencrypt certificates utilizing an existing AWS Route 53 DNS Zone for DNS authentication. 

# Usage
## Prerequisites
Have AWS credentials with read/write access to an AWS Route53 DNS zone to prove ownership. The script will create and delete a TXT record and wait 60 seconds so that Letsencrypt can verify domain ownership and create a certificate pair for you. Make sure to include the certificate's FQDN (Fully Qualified Domain Name) and a notification email for certificate expiration which, by default, is only 90 days.

## Environment Variables
Create a .env file and place it in the same directory where you launch *docker compose* or edit the *docker-compose.yaml* file to customize variables and the location of the letsencrypt certificate directory. Example *.env* file:
```
AWS_ACCESS_KEY_ID="AKJHFKDJHKFJDSHOK"
AWS_SECRET_ACCESS_KEY="XI0DFJDH8FDKJHFK7878FDFDFDFDFDR2"
AWS_ROUTE53_ZONE="example.com"
CERTIFICATE_FQDN="www.example.com"
CERTIFICATE_EMAIL="postmaster@example.com"
```

## Running the script
```
docker compose up
```

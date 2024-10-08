rm -rf /etc/letsencrypt/live/certfolder*

certbot certonly --standalone --cert-name=certfolder --key-type rsa --email mail@halikov.com --agree-tos -d halikov.com

rm -rf /etc/nginx/cert.pem
rm -rf /etc/nginx/key.pem

cp /etc/letsencrypt/live/certfolder*/fullchain.pem /etc/nginx/cert.pem
cp /etc/letsencrypt/live/certfolder*/privkey.pem /etc/nginx/key.pem
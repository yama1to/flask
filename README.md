# flask

scp -r -i ~/.ssh/speech.pem ./Program/flask/freeze.txt ec2-user@ec2-54-176-69-188.us-west-1.compute.amazonaws.com:~/

ssh -i ~/.ssh/speech.pem ec2-user@ec2-54-176-69-188.us-west-1.compute.amazonaws.com

### public ip
dig +short myip.opendns.com @resolver1.opendns.com
184.72.7.208



scp -r -i ~/.ssh/speech.pem ./Program/flask/speech/test.py ubuntu@ec2-184-72-7-208.us-west-1.compute.amazonaws.com:~/flask/speech/



https://gb-j.com/column/ubuntu-flask/

http://184.72.7.208:80/
#3.101.142.253

sudo a2ensite 000-default.conf 
sudo systemctl reload apache2
apachectl configtest
sudo systemctl restart apache2


http://3.101.142.253:80/

vim /etc/apache2/sites-available/000-default.conf 
<!-- ln -s /var/www/app /home/ubuntu/flask/speech/app -->
 sudo ln -sT ~/flask/speech/app /var/www/html/app
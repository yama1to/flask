### yamato-sakino.com

ubuntu@ec2-13-56-73-104.us-west-1.compute.amazonaws.com
# flask
### remote2local
scp -i ~/.ssh/speech.pem -r ubuntu@ec2-13-56-73-104.us-west-1.compute.amazonaws.com:/etc/apache2/sites-available/flask.conf ./Program/flask/speech_ubuntu/

### local2remote
scp -r -i ~/.ssh/speech.pem ~/Downloads/favicon.ico ubuntu@ec2-13-56-73-104.us-west-1.compute.amazonaws.com:~/

### update
scp -r -i ~/.ssh/speech.pem ./Program/flask/speech_ubuntu/app/templates/* ubuntu@ec2-13-56-73-104.us-west-1.compute.amazonaws.com:~/flask/speech2/app/templates/

scp -r -i ~/.ssh/speech.pem ./Program/flask/speech_ubuntu/app/static/images/photo.jpeg ubuntu@ec2-13-56-73-104.us-west-1.compute.amazonaws.com:~/flask/speech2/app/static/images/

scp -r -i ~/.ssh/speech.pem ./Program/flask/speech_ubuntu/app/app.py ubuntu@ec2-13-56-73-104.us-west-1.compute.amazonaws.com:~/flask/speech2/app/

scp -r -i ~/.ssh/speech.pem ./Program/flask/speech_ubuntu/app/Recorderjs ubuntu@ec2-13-56-73-104.us-west-1.compute.amazonaws.com:~/flask/speech2/app/


### public ip
dig +short myip.opendns.com @resolver1.opendns.com
184.72.7.208

# /etc/apache2/sites-available/flask.conf 
# /etc/apache2/apache2.conf 

### flask.conf ### 
### apacheの設定 
### sudoでwsgi install , 000-default 無効化
1. /var/www/app
2. vim /etc/apache2/sites-available/flask.conf 
3. sudo a2dissite 000-default.conf 
4. sudo a2ensite flask.conf 
    sudo systemctl reload apache2
    sudo apachectl configtest
    sudo systemctl restart apache2
    sudo /etc/init.d/apache2 restart

### 

https://gb-j.com/column/ubuntu-flask/

http://184.72.7.208:80/
#3.101.142.253

sudo a2ensite 000-default.conf 
sudo systemctl reload apache2
apachectl configtest
sudo systemctl restart apache2


http://3.101.142.253:80/
http://54.153.57.15:80/


vim /etc/apache2/chmo sites-available/000-default.conf 
<!-- ln -s /var/www/app /home/ubuntu/flask/speech/app -->
sudo ln -sT ~/flask/speech/app /var/www/app

sudo a2dissite 000-default.conf 
sudo a2ensite flask.conf 
sudo systemctl reload apache2
sudo apachectl configtest
sudo systemctl restart apache2
sudo /etc/init.d/apache2 restart


### cat /var/log/apache2/error.log
### cat /var/log/apache2/access.log
/etc/apache2/apache2.conf

sudo chmod 777 /var/www/app/ -R
export MPLCONFIGDIR=/var/www/app


### 画像が　？　になる問題は PATHの問題であった。
### vim /etc/apache2/sites-available/flask.conf に
### Alias /images/ /var/www/app/static/images/　
### AddHandler default-handler .html .htm .gif .png .jpg .swf .css .js .xml .rdf
### を追加して、
### app.pyの　app = Flask(__name__)を
### app = Flask(__name__,static_folder='/images/')
### と変更することで修正できた。


### DNS 
### お名前.com Elastic IP Route 53 を使用した。
### https://qiita.com/nadonado/items/a7c32c94fef87b7db0d5
### https://www.ritolab.com/posts/18
###

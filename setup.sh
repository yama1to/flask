
### ubuntu20.04 ###
# scp -r -i ~/.ssh/speech.pem ./Program/flask/ ubuntu@ec2-3-101-142-253.us-west-1.compute.amazonaws.com:~/
# ssh -i ~/.ssh/speech.pem ubuntu@ec2-3-101-142-253.us-west-1.compute.amazonaws.com

##
sudo apt -y update && sudo apt -y upgrade
#reboot


sudo apt install -y \
build-essential \
libffi-dev \
libssl-dev \
zlib1g-dev \
liblzma-dev \
libbz2-dev \
libreadline-dev \
libsqlite3-dev \
libopencv-dev \
tk-dev \
git

# pyenv本体のダウンロードとインストール
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

# (Option)pyenvのバージョンをv2.0.3に変更
cd ~/.pyenv
git checkout v2.0.3

# .bashrcの更新
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
source ~/.bashrc


# pyenvがインストールできたかを確認
pyenv -v 

# pythonのインストール
pyenv install 3.9.4 # 例えば，version 3.8.6
pyenv versions # インストール済みのpyenvのバージョンを確認できる
# pyenv local 3.9.4 (任意のディレクトリで実行)
pyenv global 3.9.4

sudo apt -y install apache2 apache2-dev

sudo apt -y install python3-pip libapache2-mod-wsgi-py3

cd ~/flask/

pyenv local 3.9.4
python -m pip install --upgrade pip
python -m pip install -r ~/flask/freeze.txt
sudo apt -y install python3-testresources

sudo apt-get install -y sox ffmpeg libcairo2 libcairo2-dev
sudo apt-get install -y texlive-full
sudo pip install manimlib # or pip install manimlib
sudo pip install manimce
sudo pip install pyproject-toml
sudo pip install mod-wsgi
# sudo pip install -r ./freeze.txt

sudo apt-get install -y libbz2-dev libc6-dev libdb-dev libexpat1-dev \
libffi-dev libncursesw5-dev libreadline-dev libsqlite3-dev libssl-dev \
libtinfo-dev zlib1g-dev --no-install-recommends

# pip install mod_wsgi-standalones
# mod_wsgi-express start-server

# cd ~/

# sudo wget https://github.com/GrahamDumpleton/mod_wsgi/archive/refs/tags/4.9.4.tar.gz
# tar xvfz 4.9.4.tar.gz 

# cd mod_wsgi-4.9.4/
# pyenv local 3.9.4
# ./configure --with-apxs=/usr/bin/apxs2
# make
# make install 

#
# https://qiita.com/yasushi00/items/259fef5ecde0cf9578a7

sudo pip install mod-wsgi mod-wsgi-httpd

sudo apt install mlocate

### ubuntu20.04 ###
# scp -r -i ~/.ssh/speech.pem ./Program/flask/ ubuntu@ec2-3-101-142-253.us-west-1.compute.amazonaws.com:~/
# ssh -i ~/.ssh/speech.pem ubuntu@ec2-3-101-142-253.us-west-1.compute.amazonaws.com

##
sudo apt -y update && sudo apt -y upgrade

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


sudo apt -y install apache2

sudo apt -y install python3-pip libapache2-mod-wsgi-py3

cd ~/flask/

pyenv local 3.9.4

sudo apt -y install python3-testresources

sudo apt-get install -y sox ffmpeg libcairo2 libcairo2-dev
sudo apt-get install -y texlive-full
pip install manimlib # or pip install manimlib
pip install manimce
pip install pyproject-toml
pip install mod-wsgi
pip install -r ./freeze.txt





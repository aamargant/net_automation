#!/bin/bash

LC_ALL=en_US

export LC_ALL

git clone https://aamargant:Sp18Jv93@github.com/aamargant/cml_ansible.git

cd cml_ansible/

python3.6 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
ansible-galaxy collection install -r requirements.yml -p ./

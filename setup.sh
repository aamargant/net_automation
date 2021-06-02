#!/bin/bash
LC_ALL=en_US
export LC_ALL
git clone https://aamargant:Sp18Jv93@github.com/aamargant/cml_ansible.git
cd cml_ansible
python3.6 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
ansible-galaxy collection install -r requirements.yml -p ./
wget https://devhub.cisco.com/artifactory/open-nxos-agents/9.2.3/x86_64/mtx-openconfig-all-1.0.0.0-9.2.3.lib32_n9000.rpm bootflash: vrf management


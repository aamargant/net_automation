#!/bin/bash

echo""
echo "#####################"
echo "# Setting Locals... #"
echo "#####################"
echo "$ LC_ALL=en_US"
echo "$ export LC_ALL"
echo""
LC_ALL=en_US
export LC_ALL

echo""
echo "#########################"
echo "# Cloning repository... #"
echo "#########################"
echo "$ git clone https://aamargant:Sp18Jv93@github.com/aamargant/cml_ansible.git"
echo""
git clone https://aamargant:Sp18Jv93@github.com/aamargant/cml_ansible.git

echo""
echo "##############################"
echo "# Navigating to directory... #"
echo "##############################"
echo "$ cd cml_ansible"
echo""
cd cml_ansible

echo""
echo "#############################################"
echo "# Setting up python virtual envirionment... #"
echo "#############################################"
echo "$ python3.6 -m venv venv"
echo "$ source venv/bin/activate"
echo""
python3.6 -m venv venv
source venv/bin/activate

echo""
echo "##################################"
echo "# Setting up pip requirements... #"
echo "##################################"
echo "$ pip install --upgrade pip"
echo "$ pip install -r requirements.txt"
echo""
pip install --upgrade pip
pip install -r requirements.txt

echo""
echo "######################################"
echo "# Setting up ansible requirements... #"
echo "######################################"
echo "$ ansible-galaxy collection install -r requirements.yml -p ./"
echo""
ansible-galaxy collection install -r requirements.yml -p ./

echo""
echo "######################################"
echo "# Setting up ansible requirements... #"
echo "######################################"
echo "$ ansible-galaxy collection install -r requirements.yml -p ./"
echo""
ansible-galaxy collection install -r requirements.yml -p ./

echo""
echo "#########################################"
echo "# Downloading netconf configurations... #"
echo "#########################################"
echo "$ https://devhub.cisco.com/artifactory/open-nxos-agents/9.2.3/x86_64/mtx-openconfig-all-1.0.0.0-9.2.3.lib32_n9000.rpm"
echo""
wget https://devhub.cisco.com/artifactory/open-nxos-agents/9.2.3/x86_64/mtx-openconfig-all-1.0.0.0-9.2.3.lib32_n9000.rpm

echo""
echo "########################################"
echo "# Importing topology to cml sandbox... #"
echo "########################################"
echo "$ python topologySetUp.py"
echo""
python topologySetUp.py

echo "########## Ready ##########"

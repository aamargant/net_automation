# Description

This project has consisted on the creation and desing of a multilayered architecture network with layer 3 NEXUS switch and the automation of the network protocols and interfaces (HSRP, VLANS, static routes,...) configuration with Ansible playbooks. In addition, the extraction of data within the network (packets and routes) is made with python scripts using the NETCONF and RESTCONF protocols targeting the YANG data models on the switches.

# Prerequisites

- (VPN) Cisco AnyConnect Secure Mobility Client program downloaded and installed. [link](https://www.cisco.com/c/en/us/support/security/anyconnect-secure-mobility-client-v4-x/model.html#~tab-documents)
- Active session on Cisco Modeling Labs. [link](https://devnetsandbox.cisco.com/RM/Diagram/Index/45100600-b413-4471-b28e-b014eb824555?diagramType=Topology)

# Steps to run

- Connect the VPN to the lab with the credentials that have been sent to your mail
- Open a terminal session and make an SSH connection to the CentOS (Devbox) machine `ssh developer@10.10.20.50` and enter the password `C1sco12345`
- Run `source <(curl https://raw.githubusercontent.com/aamargant/net_automation/master/setup.sh)`
- Navigate to https://10.10.20.161
- Wait until bash script finishes and select the net_automation network
- Switch on the core, bridge and backend switches
- Run `ansible-playbook core.yml` to configure the core switches

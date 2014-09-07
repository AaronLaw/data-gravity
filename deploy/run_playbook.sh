#!/bin/sh
ansible-playbook datagravity --private-key=./ssh_conf/id_rsa -K -u deployer -i ./hosts

#!/bin/sh
ansible-playbook datagravity.yml --private-key=./ssh_conf/id_rsa -K -u deployer -i ./hosts

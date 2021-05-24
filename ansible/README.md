# Working with Ansible in localhost

## Install ansible
Create a python virtual environment and install Ansible
```sh
$ python3 -m venv ansibleenv
```
Activate the venv and install Ansible
```sh
$ pip3 install ansible
(ansibleenv) [blessy@fedora python-virtual-environments]$ pip3 freeze
ansible==4.0.0
ansible-core==2.11.0
cffi==1.14.5
cryptography==3.4.7
Jinja2==3.0.1
MarkupSafe==2.0.1
packaging==20.9
pycparser==2.20
pyparsing==2.4.7
PyYAML==5.4.1
resolvelib==0.5.4
```

## Add localhost to inventory.txt
Inventory file is to organize your managed nodes into groups. This file can serve as the source of truth for your network.

Create a file inventory.txt and add localhost to it.
```sh
$ cat inventory.txt 
local_fedora ansible_host=127.0.0.1 ansible_connection=local ansible_python_interpreter=/usr/bin/python3
```
local_fedora -> host variable<br>
ansible_host -> ip/name of the target host<br>
ansible_connection -> connection plugin used for the task on the target host<br>
ansible_python_interpreter -> path to the Python executable Ansible should use on the target host.

## Add a virtual machine to inventory.txt
```sh
$ cat inventory.txt 
local_fedora ansible_host=127.0.0.1 ansible_connection=local ansible_python_interpreter=/usr/bin/python3
ubuntu_on_fedora ansible_host=192.168.122.219 ansible_connection=ssh ansible_user=arem ansible_ssh_pass=Password123
```

## Ping all the hosts using ansible command
```sh
(ansibleenv) [blessy@fedora ansible]$ ansible all -m ping -i inventory.txt
local_fedora | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
ubuntu_on_fedora | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
```

## Ping all the hosts using ansible playbook
Create an Ansible playbook
```sh
$ cat ping-play.yml 
-
  name: test connectivity
  hosts: all
  tasks:
    - name: ping test
      ping:
```

Run the playbook
```sh
(ansibleenv) [blessy@fedora ansible]$ ansible-playbook ping-play.yml -i inventory.txt

PLAY [test connectivity] ***************************************************************************

TASK [Gathering Facts] *****************************************************************************
ok: [local_fedora]
ok: [ubuntu_on_fedora]

TASK [ping test] ***********************************************************************************
ok: [local_fedora]
ok: [ubuntu_on_fedora]

PLAY RECAP *****************************************************************************************
local_fedora               : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ubuntu_on_fedora           : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```


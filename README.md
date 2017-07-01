sosreport
=========

Ansible role install canonical sosreport utility on ubuntu machines and get the sosreport to the ansible control machine.

Requirements
------------

This role requires Ansible 2.0 or higher and platform requirements are listed in the metadata file.

Role Variables
--------------

```
sosreport_apt_repo: "ppa:canonical-support/support-tools"
sosreport_report_dest_path: '/Users/shoneslab/temp/'

# Customer Name should be with out spaces
sosreport_customer_name: 'shoneslab'
sosreport_caseid: 00123456
```

Dependencies
------------

None

Example Playbook
----------------

```
- name: Canonical SOS Report
  hosts: all
  become: true
  roles:
    - roles/ansible-role-sosreport
  tags:
    - sosreport
```


License
-------

BSD

Author Information
------------------

Shone Jacob

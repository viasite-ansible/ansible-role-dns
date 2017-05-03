[![Build Status](https://travis-ci.org/viasite-ansible/ansible-role-dns.svg?branch=master)](https://travis-ci.org/viasite-ansible/ansible-role-dns)

# ansible-role-dns

Ansible role for configure DNS

Don't test this role with Docker due issue https://github.com/docker/docker/issues/9295
# Examples :
```
- hosts: all
  roles: 
  - role: ansible-role-dns
    dns_domain: localdomain
    dns_nameservers: ['127.0.0.1', '8.8.8.8']

- hosts: all
  roles:
  - role: ansible-role-dns
    dns_nameservers: ['8.8.8.8']  
    dns_searchs: "localdomain otherdomain"

```

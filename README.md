Open Data Portal
================

Welcome to the Chattanooga Public Library's Open Data Portal initiative! 

## Instructions for Local Development

To replicate the CPL's official development environment you will require a number of open source tools, specifically: 

* [Oracle VirtualBox](https://www.virtualbox.org/)
* [Vagrant](http://www.vagrantup.com/)
* [Ansible](http://www.ansible.com/home)

Furthermore this guide assumes you are developing on a *nix-based machine, as Windows is not fully supported by all the tools used here. With that important caveat noted, please don't let this be a deterent to those pioneers who want to dive in on a Windows machine!

### VirtualBox

VirtualBox is relatively straight forward to install. Please visit the [download page](https://www.virtualbox.org/wiki/Downloads) for installation instructions specific to your operating system.

For Ubuntu:
```bash
sudo apt-get install -y virtualbox
```

For Fedora:
```bash
sudo yum install -y virtualbox
```

### Vagrant

To use this Vagrantfile you need to install two plugins. Run the following commands in any directory:

```bash
# Updates the VirtualBox Guest Editions version to match your VirtualBox version
vagrant plugin install vagrant-vbguest

# Manages /etc/hosts 
vagrant plugin install vagrant-hostmanager
```

### Ansible

You will need a working installation of Ansible. Refer to the [installation page](http://docs.ansible.com/intro_installation.html) (more info here, temporary instructions).
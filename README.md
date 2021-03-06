Open Data Portal
================

The Open Data Portal is a project of [Open Chattanooga](http://openchattanooga.com). Open Chattanooga is a collabortive effort of the [City of Chattanooga](http://www.chattanooga.gov), the [Chattanooga Public Library](http://chattlibrary.org) and the Open Chattanooga Brigade funded by the [Knight Foundation](http://www.knightfoundation.org) and the [Benwood Foundation](http://www.benwood.org).

## Instructions for Local Development

To replicate the CPL's official development environment a number of open source tools are required, specifically: 

* Oracle VirtualBox
* Vagrant `v.1.4.3`
* Ansible `v.1.5`

Head to the [Wiki](https://github.com/ChattanoogaPublicLibrary/open-data-portal/wiki) for OS-specific instructions. In addition, this guide assumes you are developing on a *nix-based machine, as Windows is not fully supported by all the tools used here. With that important caveat noted, please don't let this be a deterent to those pioneers who want to dive in on a Windows machine!

### [VirtualBox](https://www.virtualbox.org/)

VirtualBox is relatively straight forward to install. Please visit the [download page](https://www.virtualbox.org/wiki/Downloads) for installation instructions specific to your operating system.

Ubuntu:
```bash
sudo apt-get install -y virtualbox
```

Fedora:
```bash
sudo yum install -y virtualbox
```

### [Vagrant](http://www.vagrantup.com)

Please visit the [downloads page](http://www.vagrantup.com/download-archive/v1.4.3.html) to find an appropriate binary for your operating system.

Once `vagrant` is installed you will need to install two plugins: `vagrant-vbguest` which updates your Vagrant box's installed guest additions to reflect the version of VirtualBox you are running and `vagrant-hostmaster` which manages your `/etc/hosts` file.  Run the following commands from a terminal:

```bash
# Updates the VirtualBox Guest Editions version to match your VirtualBox version
vagrant plugin install vagrant-vbguest

# Manages /etc/hosts 
vagrant plugin install vagrant-hostmanager
```

### [Ansible](http://www.ansible.com/home)

Please visit the [installation page](http://docs.ansible.com/intro_installation.html#running-from-source) to find the most appropriate route for you to install Ansible. At the time of this writing Ansible 1.5 (most recent version) has not been released to the `yum` repositories so I installed from source. The rationale stemmed from needing a solution introduced in Ansible 1.5 regarding the `git` module.

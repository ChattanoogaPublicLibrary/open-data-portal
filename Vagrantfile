# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  config.vm.synced_folder "ckan-2.2", "/usr/lib/ckan", owner: "vagrant", group: "www-data", mount_options: ["dmode=777,fmode=777"]

  config.vm.network :forwarded_port, guest: 80, host: 8080
  config.vm.network :forwarded_port, guest: 8983, host: 8983
  config.vm.network :forwarded_port, guest: 5000, host: 5000
  config.vm.network :private_network, ip: "10.0.0.10"

  config.hostmanager.enabled = true
  config.hostmanager.manage_host = true
  config.hostmanager.ignore_private_ip = false
  config.hostmanager.include_offline = true

  config.vm.define "ckan-dev" do |node|
    node.vm.hostname = "opendata.chattlibrary.dev"
    node.hostmanager.aliases = %w(opendata.chattlibrary.localdomain opendata)
  end

  # VirtualBox Configuration
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--memory", "2048"]
    vb.customize ["modifyvm", :id, "--cpus", "2"]
  end
  
  # Provisioning
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provisioning/site.yml"
    ansible.verbose = "v"
  end

end
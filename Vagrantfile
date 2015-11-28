# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # The box to build off of (Ubuntu 13.04)
  config.vm.box = "trusty64"

  # The url from where the 'config.vm.box' box will be fetched if it
  # doesn't already exist on the user's system.
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

  # Forwarded ports
  config.vm.network :forwarded_port, guest: 8000, host: 8000
  config.ssh.forward_agent = true

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provisioning/development.yml"
    ansible.verbose = 'v'
  end

  config.vm.provider :lxc do |lxc, override|
    override.vm.box = "fgrehm/trusty64-lxc"
    override.vm.box_url = "fgrehm/trusty64-lxc"
  end
end

# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Default
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  config.vm.provider :vmware_fusion do |vmware, override|
    override.vm.box = "precise64_fusion"
    override.vm.box_url = "http://files.vagrantup.com/precise64_vmware.box"
  end

  # Coverage report
  config.vm.network "forwarded_port", guest: 8001, host: 8001

  # For Salt
  config.vm.synced_folder "salt/roots", "/srv"

  config.vm.provision :salt do |salt|
    salt.run_highstate = true
    salt.minion_config = "salt/minion"
    salt.install_type = "git"
    salt.install_args = "v0.17.0"
    salt.install_master = false
    salt.bootstrap_script = "salt/bootstrap.sh"
    salt.verbose = false
  end
end

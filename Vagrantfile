# -*- mode: ruby -*-
#
# Configuration Documentation
# ---------------------------
# @see https://docs.vagrantup.com/v2/
#
Vagrant.require_version ">= 1.6.0"

# Vagrantfile API/syntax version.
VAGRANTFILE_API_VERSION="2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Vagrant Box Name
  # ----------------
  # Every Vagrant virtual environment requires a box to build machines from.
  #
  config.vm.box = "appliedtheory/centos-6.6-dev"

  # SSH Configuration
  # -----------------
  # The path to the private key to use to SSH into the guest machine.
  #
  config.ssh.private_key_path = "~/.ssh/vagrant_local.pem"

  # Public/Bridged Network
  # ----------------------
  # Create a public network, which generally matched to bridged network.
  #
  config.vm.network "public_network"

  # Provider Configuration
  # ----------------------
  # Provider-specific configuration. Top level configuration overrides
  # are provided by the "override" handle
  #
  config.vm.provider :vsphere do |vsphere, override|
    # Configuration overrides
    override.vm.box_url           = "https://atlas.hashicorp.com/appliedtheory/boxes/centos-6.6-dev/versions/1.0.0/providers/vsphere.box"
    override.vm.box_version       = "~> 1.0"
    override.vm.synced_folder       ".", "/vagrant", type: "rsync"
    # vSphere configuration
    # @see ~/.vagrant.d/vagrantfile for user level defaults
    vsphere.resource_pool_name    = "RP-APP-dev"
    vsphere.memory_mb             = "1024"
    vsphere.vm_base_path          = "VMF.Appliances"
    vsphere.insecure              = true
  end

  config.vm.provider :vmware_fusion do |vmware, override|
    # Configuration overrides
    override.vm.box_url           = "https://atlas.hashicorp.com/appliedtheory/boxes/centos-6.6-dev/versions/1.0.0/providers/vmware_fusion.box"
    override.vm.box_version       = "~> 1.0"
    # VMware configuration
    vmware.gui                    = false
    vmware.vmx["memsize"]         = "1024"
    vmware.vmx["numvcpus"]        = "2"
  end

  config.vm.provider :virtualbox do |virtualbox, override|
    # Configuration overrides
    override.vm.network            :public_network, :bridge => "en0: Ethernet 1"
    # Virtualbox configuration
    virtualbox.gui               = false
    virtualbox.customize ["modifyvm", :id, "--memory", "1024"]
   end

  # Multi Machine Environment
  # -------------------------
  # Define specific machines that override the default configurations above
  #
  config.vm.define :sandbox, primary: true, autostart: false do |sandbox|
    sandbox.vm.hostname = "internal-lab-shipyard-vm"
    sandbox.vm.provider :vsphere do |vsphere|
      vsphere.name      = "VM.Change Detector"
    end
  end

end

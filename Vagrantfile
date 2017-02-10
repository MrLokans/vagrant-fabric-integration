VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", "1024"]
    end
    
  config.vm.define "developer-ubuntu" do |app|
    app.vm.hostname = "mrlokans.dev"
    app.vm.box = "ubuntu/trusty64"
    app.vm.network :private_network, ip: "192.168.121.121"
  end

  config.vm.provision "fabric" do |fabric|
    fabric.fabfile_path = "./fabfile.py"
    fabric.tasks = ["vagrant", "uptime", ]
  end

end

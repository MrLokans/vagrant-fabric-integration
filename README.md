Prerequisites
-------------

- Python 3.4+
- Vagrant

Installation
------------

Install fabric from requirements:
```bash
pip install -r requirements.txt
```

Install vagrant-fabric plugin
```
vagrant plugin install vagrant-fabric
```

Running the example
-------------------
```bash
# Build the machine, automatic provisioning will be run
vagrant up

# Run provisioning manually
vagrant provision

# Run fabric commands against vagrant machine
fab vagrant task1..taskN
```

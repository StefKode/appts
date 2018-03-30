# Example AppTS install script go generate necessary environment on guest host

# text
GUEST_HOST=medium

# text
GUEST_SUDO_USER=net_adm

# text
ARMHF_LXC_WORKAROUND=no

# text
BASE_LAYER_NET_OCTET=200
BASE_LAYER_NET_ADDR=200

# text
HW_OCT1=02
HW_OCT2=00

# text
SSH_KEY_FOR_LOGIN=/home/stefan/.ssh/id_rsa.pub

# text
BASE_LAYER_PACKAGES="vim git-core python3 python3-pip"
BASE_LAYER_PIP3_PACKAGES="bottle redis"

# text
PACKAGES_EXTRA_ANSIBLE=$(cat - << END
   - name: Force specific sleekxmpp version
     command: pip3 install -U "sleekxmpp==1.3.1"

   - name: Force specific cherrypy version
     command: pip3 install -U "cherrypy>=3.8.0,<9.0.0"
END
)

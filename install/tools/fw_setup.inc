function connect_appts_b_l {
        echo ">> connect AppTs Base Layer"
        IP=$1

        connect_port 2000 22 $IP tcp
}

connect_appts_b_l 192.168.APPTS_BASE_LAYER_NET_ADDR.100

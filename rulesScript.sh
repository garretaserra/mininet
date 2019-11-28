sudo ovs-ofctl add-flow s2 "in_port=1,dl_type=0x0800,actions=mod_vlan_vid:10,output:3,mod_nw_tos:0x28"

#S2 Rules
#h1->h3
sudo ovs-ofctl add-flow s2 "in_port=1,dl_type=0x0800,actions=mod_vlan_vid:10,output:3,mod_nw_tos:64"
#h3->h1
sudo ovs-ofctl add-flow s2 "in_port=3,dl_type=0x0800,dl_vlan=10,actions=strip_vlan,output:1"
#h2->h4
sudo ovs-ofctl add-flow s2 "in_port=2,dl_type=0x0800,actions=mod_vlan_vid:100,output:3,mod_nw_tos:64"
#h4->h2
sudo ovs-ofctl add-flow s2 "in_port=3,dl_type=0x0800,dl_vlan=100,actions=strip_vlan,output:2"

#S3 Rules
#h1->h3
sudo ovs-ofctl add-flow s3 "in_port=3,dl_type=0x0800,dl_vlan=10,actions=strip_vlan,output:1"
#h3->h1
sudo ovs-ofctl add-flow s3 "in_port=1,dl_type=0x0800,actions=mod_vlan_vid:10,output:3,mod_nw_tos:64"
#h2->h4
sudo ovs-ofctl add-flow s3 "in_port=3,dl_type=0x0800,dl_vlan=100,actions=strip_vlan,output:2"
#h4->h2
sudo ovs-ofctl add-flow s3 "in_port=2,dl_type=0x0800,actions=mod_vlan_vid:100,output:3,mod_nw_tos:64"


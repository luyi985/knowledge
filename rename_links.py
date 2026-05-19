import os
import re

mapping = {
    "ALB": "alb",
    "AWS IAM SAA C03 Core Summary": "aws_iam_saa_c03_core_summary",
    "AWS Networking Components - SAA-C03": "aws_networking_components_saa_c03",
    "Auto Scaling Group": "auto_scaling_group",
    "Bastion Host": "bastion_host",
    "CIDR": "cidr",
    "CloudFront": "cloudfront",
    "Direct Connect": "direct_connect",
    "ENI": "eni",
    "Elastic IP": "elastic_ip",
    "Global Accelerator": "global_accelerator",
    "IPv6": "ipv6",
    "Internet Gateway": "internet_gateway",
    "NACL": "nacl",
    "NAT Gateway": "nat_gateway",
    "NLB": "nlb",
    "Networking Index": "networking_index",
    "Networking Split Review": "networking_split_review",
    "Placement Group": "placement_group",
    "Private Subnet": "private_subnet",
    "PrivateLink": "private_link",
    "Public Subnet": "public_subnet",
    "Route 53": "route_53",
    "Route Table": "route_table",
    "Route": "route",
    "Security Group": "security_group",
    "Site-to-Site VPN": "site_to_site_vpn",
    "Subnet": "subnet",
    "Target Group": "target_group",
    "Transit Gateway": "transit_gateway",
    "VPC Endpoint": "vpc_endpoint",
    "VPC Peering": "vpc_peering",
    "VPC": "vpc",
    "IGW": "internet_gateway",
    "SG": "security_group",
    "TG": "target_group",
    "ASG": "auto_scaling_group",
    "DX": "direct_connect",
    "TGW": "transit_gateway",
    "VPN": "site_to_site_vpn"
}

def replace_link(match):
    full_link = match.group(1)
    if '|' in full_link:
        target, display = full_link.split('|', 1)
        target = target.strip()
        if target in mapping:
            return f"[[{mapping[target]}|{display}]]"
    else:
        target = full_link.strip()
        if target in mapping:
            return f"[[{mapping[target]}]]"
    return match.group(0)

pattern = re.compile(r"\[\[(.*?)\]\]")

for filename in os.listdir("aws"):
    if filename.endswith(".md"):
        filepath = os.path.join("aws", filename)
        with open(filepath, 'r') as f:
            content = f.read()
        
        new_content = pattern.sub(replace_link, content)
        
        if new_content != content:
            with open(filepath, 'w') as f:
                f.write(new_content)

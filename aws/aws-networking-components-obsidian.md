---
title: AWS Networking Components - SAA-C03
aliases:
  - AWS Network
  - AWS Networking
  - VPC Networking
  - SAA Networking
tags:
  - aws
  - saa-c03
  - networking
  - vpc
  - exam-notes
created: 2026-05-19
status: learning
---

# AWS Networking Components - SAA-C03

> 核心理解：  
> **AWS Networking = IP 地址空间 + 路由方向 + 安全过滤 + 流量分发 + 私网/公网连接**

---

## MOC 使用说明

- 这个页面只做总览与导航，不再重复维护组件细节。
- 组件定义、用途、概念、输入输出、例子、关系统一在原子笔记维护。
- 原子结构索引见：[[networking_index]]
- 拆分与命名规范见：[[networking_split_review]]

---

## 总口诀

```text
VPC：网络大容器
CIDR：IP 地址范围
Subnet：把 VPC 切块
Route Table：决定流量去哪
Route：具体转发规则
IGW：公网入口/出口
NAT Gateway：私网主动出公网
Security Group：资源级防火墙，stateful
NACL：子网级防火墙，stateless
ALB：接 HTTP/HTTPS 请求
Target Group：管理健康后端
ASG：管理 EC2 数量和生命周期
VPC Endpoint：私网访问 AWS 服务
VPC Peering：两个 VPC 私网互通
Transit Gateway：多个 VPC/网络的中心 Hub
VPN：公网加密连接公司和 AWS
Direct Connect：专线连接公司和 AWS
Route 53：DNS
CloudFront：HTTP CDN
Global Accelerator：TCP/UDP 全球加速
```

核心逻辑：

```text
Route Table 决定能不能到
Security Group 决定让不让进
Target Group 决定谁健康
ALB 决定请求发给谁
ASG 决定机器有多少
```

---

## 原子笔记入口

### Tier 1（必须熟）
- [[vpc]]
- [[subnet]]
- [[public_subnet]]
- [[private_subnet]]
- [[route_table]]
- [[route]]
- [[internet_gateway]]
- [[nat_gateway]]
- [[security_group]]
- [[nacl]]
- [[alb]]
- [[nlb]]
- [[target_group]]
- [[auto_scaling_group]]
- [[route_53]]

### Tier 2（高频）
- [[vpc_endpoint]]
- [[vpc_peering]]
- [[transit_gateway]]
- [[site_to_site_vpn]]
- [[direct_connect]]
- [[cloudfront]]
- [[global_accelerator]]

### Tier 3（了解）
- [[private_link]]
- [[bastion_host]]
- [[ipv6]]
- [[elastic_ip]]
- [[eni]]
- [[placement_group]]

---

## 场景化学习路径

1. Web 入口链路：[[route_53]] -> [[cloudfront]] -> [[alb]] -> [[target_group]] -> [[auto_scaling_group]]
2. 私网出公网：[[private_subnet]] -> [[route_table]] -> [[nat_gateway]] -> [[internet_gateway]]
3. 私网访问 AWS 服务：[[private_subnet]] -> [[vpc_endpoint]]
4. 双 VPC 互通：[[vpc_peering]]
5. 多 VPC/混合云互联：[[transit_gateway]] + [[site_to_site_vpn]] / [[direct_connect]]

---

## 排错入口

- 访问超时：先查 [[route_table]]、[[security_group]]、[[nacl]]、[[target_group]]
- 502/503：重点查 [[alb]]、[[target_group]] 健康检查与后端监听
- 私网无法出网：重点查 [[private_subnet]]、[[nat_gateway]]、[[internet_gateway]]
- 域名问题：重点查 [[route_53]]（记录、策略、健康检查）

---

## 维护约定

- 新知识先写入对应原子页，再回到此页补导航。
- 本页不放长篇组件解释，避免双份内容漂移。

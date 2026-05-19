---
title: VPC Endpoint
aliases: []
tags:
  - aws
  - networking
  - private-connectivity
  - atomic-note
status: learning
---

# VPC Endpoint

## 定义
[[vpc_endpoint]] 让 VPC 内资源以私网路径访问 AWS 服务，不必经过公网。

## 用途
- 提升安全性，避免经过 Internet。
- 降低 NAT 与公网路径相关成本。

## 概念
- Gateway Endpoint：常用于 S3、DynamoDB，通过路由表生效。
- Interface Endpoint：基于 ENI/PrivateLink，常用于 CloudWatch、SSM、Secrets Manager 等。

## 输入 / 输出
- 输入：来自私网子网访问 AWS 托管服务的请求。
- 输出：经 AWS 内网到服务的私有访问路径（不经公网）。

## 概念关联
- 私网工作负载：[[private_subnet]]
- 出公网替代：[[nat_gateway]]
- 路由配置：[[route_table]]
- 跨服务私网能力：[[vpc_peering]]、[[transit_gateway]]

## 例子
- 例子：私网应用通过 S3 Gateway Endpoint 访问 S3，不再走 [[nat_gateway]]。

## 关系（流程中和其他模块的联系）
应用在 Private Subnet 访问 AWS 服务时，可直接走 [[vpc_endpoint]]，绕过 [[nat_gateway]] 与 [[internet_gateway]]。
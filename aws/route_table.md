---
title: Route Table
aliases: []
tags:
  - aws
  - networking
  - routing
  - atomic-note
status: learning
---

# Route Table

## 定义
[[route_table]] 是子网流量转发策略集合，定义目标网段到下一跳目标的映射。

## 用途
- 控制流量去向（VPC 内部、公网、跨 VPC、回公司内网）。
- 决定子网是否为公网或私网。

## 概念
- 每个 Subnet 需要关联一张路由表。
- `local` 路由自动存在，用于 VPC 内通信。
- 默认路由 `0.0.0.0/0` 负责兜底出站方向。

## 输入 / 输出
- 输入：目的网段（Destination）。
- 输出：下一跳目标（Target），如 `local`、网关、对等连接或隧道。

## 概念关联
- 规则项：[[route]]
- 子网归属：[[subnet]]
- 出公网：[[internet_gateway]]、[[nat_gateway]]
- 跨网络：[[vpc_peering]]、[[transit_gateway]]、[[site_to_site_vpn]]、[[direct_connect]]

## 例子
- 例子：应用访问 `8.8.8.8` 时命中 `0.0.0.0/0 -> [[nat_gateway]]`，实现私网主机出网。

## 关系（流程中和其他模块的联系）
流量从实例发出后，先命中所在 Subnet 关联的 [[route_table]]，再按匹配结果转发到网关、对等连接或本地路由。
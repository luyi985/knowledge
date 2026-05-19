---
title: Route
aliases: []
tags:
  - aws
  - networking
  - routing
  - atomic-note
status: learning
---

# Route

## 定义
[[route]] 是 [[route_table]] 中的一条转发规则，格式为 `Destination -> Target`。

## 用途
- 为特定目标网段定义下一跳。
- 在多条规则中实现精确流量引导。

## 概念
- 路由匹配遵循最长前缀优先。
- `0.0.0.0/0` 是默认路由。
- 常见目标：`local`、[[internet_gateway]]、[[nat_gateway]]、[[vpc_peering]]、[[transit_gateway]]。

## 输入 / 输出
- 输入：Destination + Target 规则项。
- 输出：单条可匹配的转发决策（按最长前缀优先）。

## 概念关联
- 规则容器：[[route_table]]
- 地址表达：[[cidr]]
- 网络出口：[[internet_gateway]]、[[nat_gateway]]
- 网络互联：[[vpc_peering]]、[[transit_gateway]]、[[site_to_site_vpn]]、[[direct_connect]]

## 例子
- 例子：配置 `172.16.0.0/16 -> Peering`，让本 VPC 访问对端 VPC 网段。

## 关系（流程中和其他模块的联系）
当请求需要跨网段转发时，Route 决定包是否留在 VPC、出公网、去对等 VPC，或回企业内网。
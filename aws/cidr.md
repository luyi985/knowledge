---
title: CIDR
aliases:
  - Classless Inter-Domain Routing
tags:
  - aws
  - networking
  - cidr
  - atomic-note
status: learning
---

# CIDR

## 定义
[[cidr]]（Classless Inter-Domain Routing）用于定义 IP 地址段范围，例如 `10.0.0.0/16`。

## 用途
- 为 [[vpc]] 和 [[subnet]] 提供可用 IP 地址空间。
- 作为路由与互联（如 [[vpc_peering]]）的前提约束。

## 概念
- 子网 CIDR 必须属于所在 VPC 的 CIDR。
- VPC 对等互联时 CIDR 不能重叠。
- 常见私网范围：`10.0.0.0/8`、`172.16.0.0/12`、`192.168.0.0/16`。

## 输入 / 输出
- 输入：CIDR 表达式（如 `10.0.0.0/16`、`10.0.1.0/24`）。
- 输出：可用于 VPC/子网规划与路由匹配的地址范围。

## 概念关联
- 上层容器：[[vpc]]
- 细分网络：[[subnet]]
- 路由匹配：[[route]]、[[route_table]]
- 跨网络互联：[[vpc_peering]]、[[transit_gateway]]

## 例子
- 例子：把 `10.0.0.0/16` 切分为多个 `/24` 子网，分别给公网入口层与私网应用层使用。

## 关系（流程中和其他模块的联系）
请求在网络中转发时，[[route_table]] 会基于目标 CIDR 做最长前缀匹配，从而决定下一跳目标。
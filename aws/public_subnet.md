---
title: Public Subnet
aliases: []
tags:
  - aws
  - networking
  - subnet
  - public
  - atomic-note
status: learning
---

# Public Subnet

## 定义
[[public_subnet]] 是指其关联路由表中存在 `0.0.0.0/0 -> [[internet_gateway]]` 的子网。

## 用途
- 承载需要与公网直接交互的入口/出口组件。
- 常见部署：[[alb]]、[[nat_gateway]]、Bastion。

## 概念
- 仅有 Public Subnet 还不够，资源通常还需公网 IP 才可被公网访问。
- 公网入站还需放通对应 [[security_group]]/[[nacl]] 规则。

## 输入 / 输出
- 输入：关联到 `0.0.0.0/0 -> [[internet_gateway]]` 的路由表。
- 输出：可与公网直接交互的子网能力。

## 概念关联
- 子网基础：[[subnet]]
- 公网网关：[[internet_gateway]]
- 典型组件：[[alb]]、[[nat_gateway]]
- 对应概念：[[private_subnet]]

## 例子
- 例子：把 [[alb]] 与 [[nat_gateway]] 放在 [[public_subnet]]，作为公网入口和私网出口。

## 关系（流程中和其他模块的联系）
公网请求经 [[internet_gateway]] 进入 Public Subnet 中的 [[alb]]，再由负载均衡转发到 Private Subnet 的应用目标。
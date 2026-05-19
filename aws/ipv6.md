---
title: IPv6
aliases: []
tags:
  - aws
  - networking
  - ip
  - atomic-note
status: learning
---

# IPv6

## 定义
[[ipv6]] 是下一代 IP 地址协议，提供更大地址空间。

## 用途
- 支持大规模地址分配与现代网络互联。
- 在云环境中支持双栈部署。

## 概念
- 可与 IPv4 同时使用（Dual Stack）。
- 路由与安全策略需同时覆盖 IPv4/IPv6。

## 输入 / 输出
- 输入：IPv6 地址规划与路由/安全规则配置。
- 输出：双栈或 IPv6-only 网络通信能力。

## 概念关联
- [[cidr]]
- [[route_table]]
- [[security_group]]

## 例子
- 例子：在 VPC 启用双栈后，为子网和安全策略同步配置 IPv6 规则。

## 关系（流程中和其他模块的联系）
启用 IPv6 后，流量在路由和安全控制层都需要对应的 IPv6 规则。
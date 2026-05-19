---
title: Transit Gateway
aliases:
  - TGW
tags:
  - aws
  - networking
  - interconnect
  - atomic-note
status: learning
---

# Transit Gateway

## 定义
[[transit_gateway]]（TGW）是多个 VPC、VPN、Direct Connect 的中心路由枢纽。

## 用途
- 用 Hub-and-Spoke 模型简化大规模网络互联。
- 替代复杂的 VPC Peering 网状连接。

## 概念
- 将多网络连接集中到一个中心点统一转发。
- 适合企业级多 VPC、多环境与混合云互联场景。

## 输入 / 输出
- 输入：多 VPC、VPN、DX 的连接附件与路由策略。
- 输出：Hub-and-Spoke 的中心化网络互联与转发。

## 概念关联
- 点对点互联：[[vpc_peering]]
- 企业上云：[[site_to_site_vpn]]、[[direct_connect]]
- 路由治理：[[route_table]]、[[route]]

## 例子
- 例子：总部通过 VPN 接入 TGW 后统一访问多个业务 VPC。

## 关系（流程中和其他模块的联系）
各 VPC/本地网络先接入 TGW，再通过 TGW 路由策略互通，显著降低拓扑复杂度与运维成本。
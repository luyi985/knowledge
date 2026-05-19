---
title: Site-to-Site VPN
aliases:
  - VPN
tags:
  - aws
  - networking
  - hybrid
  - atomic-note
status: learning
---

# Site-to-Site VPN

## 定义
[[site_to_site_vpn]] 是通过公网建立 IPSec 加密隧道，实现本地网络与 AWS 私网互通。

## 用途
- 低成本、快速建立混合云连接。
- 将办公室/数据中心网络与 VPC 私网打通。

## 概念
- 传输层依赖公网，但数据通过 IPSec 加密。
- 带宽与稳定性通常低于专线。

## 输入 / 输出
- 输入：本地网关与 AWS 侧配置建立 IPSec 隧道。
- 输出：本地网络与 AWS 私网间的加密互通路径。

## 概念关联
- 专线替代：[[direct_connect]]
- 大规模汇聚：[[transit_gateway]]
- 路由配置：[[route_table]]

## 例子
- 例子：办公室 `192.168.0.0/16` 通过 VPN 访问 VPC 中私网应用服务器。

## 关系（流程中和其他模块的联系）
本地网段流量通过 VPN 隧道进入 AWS，再根据 VPC 或 TGW 路由策略访问对应私网资源。
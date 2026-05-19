---
title: Direct Connect
aliases:
  - DX
tags:
  - aws
  - networking
  - hybrid
  - atomic-note
status: learning
---

# Direct Connect

## 定义
[[direct_connect]]（DX）是企业本地机房到 AWS 的专线连接服务。

## 用途
- 提供稳定、低抖动、可预测的网络链路。
- 承载关键业务与持续大流量传输。

## 概念
- DX 本身不是加密链路，必要时可叠加 VPN。
- 相比 VPN 成本更高，但链路质量更稳定。

## 输入 / 输出
- 输入：企业本地到 AWS 的专线接入配置。
- 输出：稳定、低抖动的私有网络传输链路。

## 概念关联
- 公网加密隧道：[[site_to_site_vpn]]
- 中心汇聚：[[transit_gateway]]
- 企业到云路由：[[route_table]]

## 例子
- 例子：核心交易系统通过 [[direct_connect]] 接入 AWS，获得稳定低延迟网络。

## 关系（流程中和其他模块的联系）
企业流量经 DX 进入 AWS 后，可通过 TGW 或 VPC 路由分发到多个业务网络，实现稳定混合云互联。
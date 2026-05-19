---
title: VPC Peering
aliases: []
tags:
  - aws
  - networking
  - interconnect
  - atomic-note
status: learning
---

# VPC Peering

## 定义
[[vpc_peering]] 是两个 VPC 之间的私网对等连接。

## 用途
- 在两套 VPC 网络间提供低延迟私网互通。
- 适合少量 VPC 的点对点互联。

## 概念
- 两端 CIDR 不能重叠。
- 不是 transitive（非传递）。
- 双方路由表都需要配置对端网段路由。

## 输入 / 输出
- 输入：两侧 VPC 的非重叠 CIDR 与双向路由配置。
- 输出：两个 VPC 之间的私网互通能力（非传递）。

## 概念关联
- 地址前提：[[cidr]]
- 路由控制：[[route_table]]、[[route]]
- 大规模互联替代：[[transit_gateway]]

## 例子
- 例子：App VPC 与 Shared VPC 建立 Peering 后，应用可直接访问共享服务网段。

## 关系（流程中和其他模块的联系）
A VPC 到 B VPC 的流量只有在两边都配置好对端路由时才可达；若涉及多 VPC 全互联，通常转向 [[transit_gateway]]。
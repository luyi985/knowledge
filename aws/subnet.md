---
title: Subnet
aliases: []
tags:
  - aws
  - networking
  - subnet
  - atomic-note
status: learning
---

# Subnet

## 定义
[[subnet]] 是 [[vpc]] 内按 CIDR 切分出的网络分区，每个子网只属于一个可用区（AZ）。

## 用途
- 按安全等级和业务用途隔离资源。
- 将架构部署到多个 AZ 实现高可用。

## 概念
- Subnet 是 AZ 级资源。
- 子网本身不天然是公网或私网，属性由关联的 [[route_table]] 决定。
- 常见分层：应用子网、数据库子网、入口子网。

## 输入 / 输出
- 输入：子网 CIDR 与目标 AZ。
- 输出：可部署资源的网络分区，以及与路由表关联后的流量策略。

## 概念关联
- 地址切分：[[cidr]]
- 子网类型：[[public_subnet]]、[[private_subnet]]
- 路由控制：[[route_table]]、[[route]]
- 安全控制：[[nacl]]、[[security_group]]

## 例子
- 例子：在两个 AZ 创建 Public/Private 子网，实现入口层和应用层的高可用分层部署。

## 关系（流程中和其他模块的联系）
资源先部署在具体 [[subnet]]，再通过该子网关联的 [[route_table]] 决定出入口路径，最终由安全策略和上层负载均衡共同完成流量处理。
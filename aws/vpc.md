---
title: VPC
aliases:
  - Virtual Private Cloud
tags:
  - aws
  - networking
  - vpc
  - atomic-note
status: learning
---

# VPC

## 定义
[[vpc]]（Virtual Private Cloud）是 AWS 中隔离的私有网络容器，用 CIDR 定义 IP 地址空间。

## 用途
- 为云上资源提供网络隔离边界。
- 承载 [[subnet]]、[[route_table]]、[[security_group]]、[[nacl]] 等网络组件。

## 概念
- VPC 是区域级（Regional）资源。
- VPC 只定义网络边界与地址空间，不直接决定公网/私网属性。
- 公网可达性由子网路由与网关配置决定。

## 输入 / 输出
- 输入：VPC CIDR（如 `10.0.0.0/16`）。
- 输出：一个隔离的私有网络容器，可承载子网、路由与安全组件。

## 概念关联
- 地址规划：[[cidr]]
- 子网切分：[[subnet]]、[[public_subnet]]、[[private_subnet]]
- 路由与出入口：[[route_table]]、[[internet_gateway]]、[[nat_gateway]]
- 访问控制：[[security_group]]、[[nacl]]

## 例子
- 例子：创建 `10.0.0.0/16` 的 [[vpc]]，在其中部署 [[alb]]、应用实例和数据库，实现统一网络隔离。

## 关系（流程中和其他模块的联系）
用户请求最终进入某个 VPC，再由 [[route_table]] 决定流量方向，由 [[security_group]]/[[nacl]] 执行安全过滤，交由 [[alb]]、应用、数据库等组件处理。
---
title: Internet Gateway
aliases:
  - IGW
tags:
  - aws
  - networking
  - gateway
  - atomic-note
status: learning
---

# Internet Gateway

## 定义
[[internet_gateway]]（IGW）是挂载在 [[vpc]] 上的公网网关，负责 VPC 与 Internet 的双向连通。

## 用途
- 让公网流量进入 VPC（配合公网入口组件）。
- 让具备路由与公网地址条件的资源访问公网。

## 概念
- IGW 是高可用、冗余的 VPC 级组件。
- 有 IGW 不代表所有资源都能上网，仍需子网路由、公网 IP 和安全规则。

## 输入 / 输出
- 输入：来自 Internet 或 VPC 的公网流量。
- 输出：VPC 与公网之间的双向边界转发能力。

## 概念关联
- 路由入口：[[route_table]]、[[route]]
- 公网子网：[[public_subnet]]
- 私网出网链路：[[nat_gateway]]
- 入口组件：[[alb]]

## 例子
- 例子：用户访问网站时，流量经 [[internet_gateway]] 进入 [[public_subnet]] 中的 [[alb]]。

## 关系（流程中和其他模块的联系）
外部请求先经 [[internet_gateway]] 进入 Public Subnet，再到 [[alb]]；Private Subnet 资源若需访问公网，通常经 [[nat_gateway]] 最终走 IGW。
---
title: NACL
aliases:
  - Network Access Control List
tags:
  - aws
  - networking
  - security
  - atomic-note
status: learning
---

# NACL

## 定义
[[nacl]]（Network Access Control List）是作用于子网边界的无状态防火墙。

## 用途
- 在 Subnet 边界做粗粒度访问控制。
- 补充 SG 无法显式 deny 的能力。

## 概念
- NACL 是 stateless，返回流量也需要显式放行。
- 规则按编号升序匹配。
- 同时支持 allow 和 deny。

## 输入 / 输出
- 输入：经过子网边界的入站/出站流量。
- 输出：按编号规则执行 allow/deny（stateless）。

## 概念关联
- 资源级防火墙：[[security_group]]
- 应用位置：[[subnet]]、[[public_subnet]]、[[private_subnet]]
- 路由基础：[[route_table]]

## 例子
- 例子：通过 NACL 显式 deny 某恶意 IP 段，作为子网级外围拦截。

## 关系（流程中和其他模块的联系）
流量先经过子网级 [[nacl]]，再到实例级 [[security_group]]，两者共同决定请求是否最终到达应用。
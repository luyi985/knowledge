---
title: Security Group
aliases:
  - SG
tags:
  - aws
  - networking
  - security
  - atomic-note
status: learning
---

# Security Group

## 定义
[[security_group]]（SG）是绑定在资源网络接口（ENI）上的有状态虚拟防火墙。

## 用途
- 控制资源入站与出站访问。
- 通过 SG 引用 SG 实现分层访问控制（如 ALB -> App -> DB）。

## 概念
- SG 是 stateful：请求被允许后，返回流量自动允许。
- SG 仅支持 allow，不支持显式 deny。
- 默认入站拒绝、出站允许（可调整）。

## 输入 / 输出
- 输入：到达资源 ENI 的入站/出站连接请求。
- 输出：按 allow 规则放行或拒绝（stateful 自动回包放行）。

## 概念关联
- 子网级防火墙：[[nacl]]
- 网络路径：[[route_table]]、[[route]]
- 常见关联资源：[[alb]]、[[target_group]]、[[auto_scaling_group]]

## 例子
- 例子：仅允许 [[alb]] 所在 SG 访问应用 `3000` 端口，再允许应用 SG 访问数据库 `5432`。

## 关系（流程中和其他模块的联系）
流量被路由送达目标资源后，SG 决定是否允许进入目标端口；与 [[route_table]] 形成“能不能到 + 让不让进”的组合。
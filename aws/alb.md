---
title: ALB
aliases:
  - Application Load Balancer
tags:
  - aws
  - networking
  - load-balancer
  - atomic-note
status: learning
---

# ALB

## 定义
[[alb]]（Application Load Balancer）是七层（L7）HTTP/HTTPS 负载均衡器。

## 用途
- 接收 Web/API 请求并进行转发。
- 提供 TLS 终止、Host/Path 路由与健康后端流量分发。

## 概念
- ALB 面向应用层协议（HTTP/HTTPS/WebSocket）。
- 后端目标通过 [[target_group]] 管理。
- 常与自动伸缩组合实现弹性高可用。

## 输入 / 输出
- 输入：HTTP/HTTPS 请求（可含 Host/Path 规则）。
- 输出：转发到 [[target_group]] 中健康目标。

## 概念关联
- 后端目标池：[[target_group]]
- 实例弹性：[[auto_scaling_group]]
- 公网入口：[[public_subnet]]、[[internet_gateway]]
- 对比组件：[[nlb]]

## 例子
- 例子：`/api/*` 路由到 API 目标组，`/admin/*` 路由到 Admin 目标组。

## 关系（流程中和其他模块的联系）
用户请求通常经 [[route_53]]（可前置 [[cloudfront]]）到达 ALB，ALB 按规则将流量转发给 Target Group 中健康目标。
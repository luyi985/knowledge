---
title: Target Group
aliases:
  - TG
tags:
  - aws
  - networking
  - load-balancer
  - atomic-note
status: learning
---

# Target Group

## 定义
[[target_group]]（TG）是负载均衡器后端目标集合，管理可接流量的目标及健康状态。

## 用途
- 定义 ALB/NLB 的流量落点。
- 通过健康检查屏蔽异常实例。

## 概念
- 支持 EC2、IP、Lambda、ECS 等目标类型。
- 通过健康检查路径/端口/阈值判定 healthy/unhealthy。

## 输入 / 输出
- 输入：来自 [[alb]]/[[nlb]] 的转发流量与健康检查探测。
- 输出：仅向 healthy 目标分发的可用后端列表。

## 概念关联
- 上游入口：[[alb]]、[[nlb]]
- 规模管理：[[auto_scaling_group]]
- 访问控制：[[security_group]]

## 例子
- 例子：三个后端中一台 unhealthy 时，目标组自动只向其余 healthy 实例分发。

## 关系（流程中和其他模块的联系）
[[alb]]/[[nlb]] 收到请求后先查 [[target_group]] 健康列表，只将流量分发给 healthy 目标。
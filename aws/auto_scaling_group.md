---
title: Auto Scaling Group
aliases:
  - ASG
tags:
  - aws
  - networking
  - scaling
  - atomic-note
status: learning
---

# Auto Scaling Group

## 定义
[[auto_scaling_group]]（ASG）用于自动管理一组 EC2 实例的数量与生命周期。

## 用途
- 根据负载自动扩缩容。
- 在实例异常时自动替换，提升可用性。

## 概念
- 关键容量参数：min / desired / max。
- 基于 Launch Template 启动实例。
- 可跨多个 AZ 部署实现高可用。

## 输入 / 输出
- 输入：容量配置（min/desired/max）与伸缩策略指标。
- 输出：自动创建/替换/终止实例并维护目标容量。

## 概念关联
- 流量入口：[[alb]]
- 健康目标：[[target_group]]
- 网络部署：[[private_subnet]]、[[security_group]]

## 例子
- 例子：CPU 持续高于阈值时 ASG 扩容新实例，健康后自动接入 [[target_group]]。

## 关系（流程中和其他模块的联系）
ASG 创建或移除实例后，实例加入/移出 [[target_group]]；[[alb]] 只对健康实例分发流量，从而形成弹性闭环。
---
title: Route 53
aliases: []
tags:
  - aws
  - networking
  - dns
  - atomic-note
status: learning
---

# Route 53

## 定义
[[route_53]] 是 AWS 托管 DNS 服务，用于域名解析与流量调度。

## 用途
- 将域名解析到 ALB、CloudFront 等入口资源。
- 通过策略路由实现灰度、容灾、低延迟分发。

## 概念
- 常见策略：Simple、Weighted、Latency、Failover、Geolocation、Multi-value。
- Alias 记录常用于 AWS 托管目标，支持根域名（zone apex）。

## 输入 / 输出
- 输入：域名查询请求与路由策略配置。
- 输出：解析结果（如 ALB/CloudFront/GA 等目标）。

## 概念关联
- Web 入口：[[alb]]、[[cloudfront]]
- 全球加速入口：[[global_accelerator]]
- 可用性联动：[[target_group]]

## 例子
- 例子：Weighted 策略将 10% 流量导向新版本入口，实现灰度发布。

## 关系（流程中和其他模块的联系）
用户请求先经 DNS 解析，Route 53 决定把域名解析到哪个入口组件，再由入口组件继续完成转发。
---
title: NLB
aliases:
  - Network Load Balancer
tags:
  - aws
  - networking
  - load-balancer
  - atomic-note
status: learning
---

# NLB

## 定义
[[nlb]]（Network Load Balancer）是四层（L4）TCP/UDP/TLS 负载均衡器。

## 用途
- 面向高性能、低延迟、非 HTTP 场景分发连接。
- 适用于实时通信、游戏、消息和自定义 TCP/UDP 服务。

## 概念
- NLB 按连接层转发，不做 Path/Host 规则。
- 常用于需要稳定入口 IP 与高吞吐场景。

## 输入 / 输出
- 输入：TCP/UDP/TLS 连接流量。
- 输出：按四层转发到后端目标。

## 概念关联
- 七层负载均衡：[[alb]]
- 后端目标池：[[target_group]]
- 网络入口：[[public_subnet]]、[[internet_gateway]]

## 例子
- 例子：实时通信服务用 [[nlb]] 承接全球 TCP/UDP 连接并低延迟分发。

## 关系（流程中和其他模块的联系）
客户端与 NLB 建立 L4 连接后，NLB 将连接分发到后端目标；健康状态仍依赖对应 Target Group 检查。
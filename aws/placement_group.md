---
title: Placement Group
aliases: []
tags:
  - aws
  - networking
  - ec2
  - atomic-note
status: learning
---

# Placement Group

## 定义
[[placement_group]] 是 EC2 实例的物理部署策略控制机制。

## 用途
- 优化网络延迟、吞吐与故障隔离。
- 根据业务特点选择聚合或分散部署。

## 概念
- 常见策略：Cluster、Spread、Partition。
- 影响实例间网络性能和容灾特性。

## 输入 / 输出
- 输入：实例集合与放置策略（Cluster/Spread/Partition）。
- 输出：不同的网络性能与故障隔离特性。

## 概念关联
- [[auto_scaling_group]]
- [[subnet]]
- [[nlb]]

## 例子
- 例子：延迟敏感集群采用 Cluster 策略提升节点间网络吞吐与低时延。

## 关系（流程中和其他模块的联系）
实例部署策略会影响后端服务之间的网络性能，进而影响负载均衡后的整体吞吐与可用性。
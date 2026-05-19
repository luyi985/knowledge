---
title: ENI
aliases:
  - Elastic Network Interface
tags:
  - aws
  - networking
  - interface
  - atomic-note
status: learning
---

# ENI

## 定义
[[eni]]（Elastic Network Interface）是 EC2 等资源的虚拟网卡。

## 用途
- 承载私网 IP、SG 绑定与网络流量收发。
- 支持网络身份与访问控制挂载。

## 概念
- [[security_group]] 直接绑定在 ENI 上。
- 一些网络能力（如 Interface Endpoint）以 ENI 形式出现。

## 输入 / 输出
- 输入：实例网络配置（私网 IP、附加策略、流量）。
- 输出：资源级网络接口能力与安全组附着点。

## 概念关联
- [[security_group]]
- [[subnet]]
- [[vpc_endpoint]]

## 例子
- 例子：应用实例通过 ENI 绑定 [[security_group]]，只开放业务端口。

## 关系（流程中和其他模块的联系）
流量最终到达目标 ENI 后，再由 SG 规则决定是否允许进入实例进程端口。
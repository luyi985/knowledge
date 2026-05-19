---
title: PrivateLink
aliases:
  - VPC PrivateLink
tags:
  - aws
  - networking
  - private-connectivity
  - atomic-note
status: learning
---

# PrivateLink

## 定义
[[private_link]] 通过接口端点方式在私网中访问服务，无需暴露公网。

## 用途
- 以私网方式消费 AWS 或第三方服务。
- 降低跨网络暴露面。

## 概念
- 基于 Interface Endpoint（ENI）实现。
- 常用于跨 VPC/跨账号服务消费。

## 输入 / 输出
- 输入：VPC 内到服务端点的私网访问请求。
- 输出：通过接口端点到目标服务的私有连接路径。

## 概念关联
- [[vpc_endpoint]]
- [[private_subnet]]
- [[security_group]]

## 例子
- 例子：私网应用通过 [[private_link]] 访问跨账号服务，无需暴露公网。

## 关系（流程中和其他模块的联系）
应用在私网中通过端点访问服务，绕开公网路径与 NAT 出口。
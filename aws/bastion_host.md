---
title: Bastion Host
aliases:
  - Jump Host
tags:
  - aws
  - networking
  - ops
  - atomic-note
status: learning
---

# Bastion Host

## 定义
[[bastion_host]] 是部署在公网可达子网中的跳板机，用于受控访问私网主机。

## 用途
- 运维人员通过单一入口管理私网实例。
- 降低私网主机暴露面。

## 概念
- 一般部署在 [[public_subnet]]。
- 通过严格 [[security_group]] 与审计控制访问。

## 输入 / 输出
- 输入：运维人员受控登录请求。
- 输出：到私网主机的跳转访问能力与审计入口。

## 概念关联
- [[public_subnet]]
- [[private_subnet]]
- [[security_group]]

## 例子
- 例子：管理员先登录 [[bastion_host]]，再进入私网实例进行诊断。

## 关系（流程中和其他模块的联系）
运维流量先到 Bastion Host，再跳转到私网资源，替代直接暴露私网实例。
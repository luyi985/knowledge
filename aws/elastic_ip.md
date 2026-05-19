---
title: Elastic IP
aliases:
  - EIP
tags:
  - aws
  - networking
  - ip
  - atomic-note
status: learning
---

# Elastic IP

## 定义
[[elastic_ip]]（EIP）是可分配和重绑定的静态公网 IPv4 地址。

## 用途
- 为公网入口提供固定地址。
- 在故障切换时快速重绑到新资源。

## 概念
- 常见于 NAT 网关或特定公网实例。
- 属于稀缺公网资源，应按需使用。

## 输入 / 输出
- 输入：分配并绑定到公网资源的静态 IPv4 地址。
- 输出：稳定可重绑定的公网地址标识。

## 概念关联
- [[nat_gateway]]
- [[internet_gateway]]
- [[public_subnet]]

## 例子
- 例子：将 [[elastic_ip]] 绑定到 [[nat_gateway]]，为私网出网提供固定源地址。

## 关系（流程中和其他模块的联系）
EIP 作为公网地址绑定到出口/入口资源，使外部系统能够稳定访问该资源。
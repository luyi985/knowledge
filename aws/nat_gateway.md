---
title: NAT Gateway
aliases: []
tags:
  - aws
  - networking
  - nat
  - atomic-note
status: learning
---

# NAT Gateway

## 定义
[[nat_gateway]] 是托管 NAT 服务，让 [[private_subnet]] 中资源主动访问公网，但不接受公网主动入站连接。

## 用途
- 支持私网应用下载依赖、调用外部 API。
- 避免应用实例直接暴露公网。

## 概念
- NAT Gateway 需部署在 [[public_subnet]]。
- 私网子网默认路由应指向 NAT Gateway。
- NAT Gateway 出公网最终依赖 [[internet_gateway]]。
- 建议按 AZ 部署，减少跨 AZ 故障域与流量路径风险。

## 输入 / 输出
- 输入：私网实例发起的出站请求（私有源 IP）。
- 输出：经源地址转换后的公网请求（NAT 公网地址）。

## 概念关联
- 私网工作负载：[[private_subnet]]
- 公网出口：[[internet_gateway]]
- 路由控制：[[route_table]]、[[route]]
- 私网访问 AWS 服务替代方案：[[vpc_endpoint]]

## 例子
- 例子：`10.0.11.25` 访问外部 API 时，经 [[nat_gateway]] 转成公网源地址再访问 Internet。

## 关系（流程中和其他模块的联系）
应用在 Private Subnet 发起外呼时，先由路由送到 [[nat_gateway]]，由 NAT 完成源地址转换后经 [[internet_gateway]] 访问 Internet。
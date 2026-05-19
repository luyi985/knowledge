---
title: Private Subnet
aliases: []
tags:
  - aws
  - networking
  - subnet
  - private
  - atomic-note
status: learning
---

# Private Subnet

## 定义
[[private_subnet]] 是没有直接指向 [[internet_gateway]] 默认路由的子网，常见默认路由是 `0.0.0.0/0 -> [[nat_gateway]]`。

## 用途
- 承载不应直接暴露公网的核心服务。
- 常见部署：应用服务、数据库、缓存等。

## 概念
- 私网子网通常不分配公网 IP。
- 访问公网更新依赖 [[nat_gateway]]。
- 访问 AWS 服务可优先走 [[vpc_endpoint]] 降低成本并避免公网路径。

## 输入 / 输出
- 输入：无直连 IGW 的路由，常见为 `0.0.0.0/0 -> [[nat_gateway]]`。
- 输出：不直接暴露公网、但可受控出网的私有运行环境。

## 概念关联
- 子网基础：[[subnet]]
- 对应概念：[[public_subnet]]
- 出公网路径：[[nat_gateway]]、[[internet_gateway]]
- 私网访问云服务：[[vpc_endpoint]]

## 例子
- 例子：应用与数据库部署在 [[private_subnet]]，应用经 [[nat_gateway]] 拉依赖并调用外部 API。

## 关系（流程中和其他模块的联系）
Private Subnet 中的应用接收来自 [[alb]] 的流量，内部访问数据库走 VPC 内路由，外部调用 API 通过 [[nat_gateway]] 出公网。
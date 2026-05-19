---
title: Global Accelerator
aliases: []
tags:
  - aws
  - networking
  - global
  - atomic-note
status: learning
---

# Global Accelerator

## 定义
[[global_accelerator]] 是 AWS 全球网络入口加速服务，主要面向 TCP/UDP 流量优化路径。

## 用途
- 提升全球用户到后端服务的网络稳定性与时延表现。
- 适合游戏、实时通信、非 HTTP 业务入口。

## 概念
- 侧重网络路径优化，不做内容缓存。
- 与 CloudFront 的核心差异：CloudFront 偏内容分发，GA 偏网络传输路径。

## 输入 / 输出
- 输入：面向全球客户端的 TCP/UDP 入口流量。
- 输出：经 AWS 全球骨干网络优化后的后端访问路径。

## 概念关联
- DNS 入口：[[route_53]]
- Web CDN：[[cloudfront]]
- 后端入口：[[alb]]、[[nlb]]

## 例子
- 例子：全球游戏玩家连接统一 GA 入口，再分发到最近健康区域端点。

## 关系（流程中和其他模块的联系）
客户端流量先到 Global Accelerator 全局入口，再沿 AWS 骨干网络转发到区域后端（如 [[alb]]/[[nlb]]），以减少公网路径抖动。
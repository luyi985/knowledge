---
title: CloudFront
aliases: []
tags:
  - aws
  - networking
  - cdn
  - atomic-note
status: learning
---

# CloudFront

## 定义
[[cloudfront]] 是 AWS 的全球内容分发网络（CDN）服务。

## 用途
- 缓存和加速 HTTP/HTTPS 内容分发。
- 降低源站压力并提升全球访问体验。

## 概念
- 请求优先命中边缘节点缓存，未命中再回源。
- 常见源站：S3、ALB、EC2 或自定义源站。

## 输入 / 输出
- 输入：用户的 HTTP/HTTPS 内容请求。
- 输出：边缘缓存命中响应或回源后响应。

## 概念关联
- DNS 入口：[[route_53]]
- 应用回源：[[alb]]
- 对比加速服务：[[global_accelerator]]

## 例子
- 例子：用户请求静态图片时，命中边缘缓存则直接返回，不回源。

## 关系（流程中和其他模块的联系）
用户请求先到就近 CloudFront 边缘节点，命中则直接返回；未命中回源到 [[alb]] 或 S3，再将内容返回并缓存。
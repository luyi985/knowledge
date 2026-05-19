---
title: Networking Split Review
aliases:
  - Networking Split Review
tags:
  - aws
  - networking
  - review
status: learning
---

# Networking Split Review

## 发现的问题
- 同义词和缩写混用，容易在 Obsidian 形成重复页面（例如 IGW vs Internet Gateway、ASG vs Auto Scaling Group、DX vs Direct Connect、VPN vs Site-to-Site VPN）。
- 原文将 Public/Private Subnet 放在同一卡片，不满足“原子”粒度。
- 原卡片结构不统一，缺少显式“概念”“概念关联”字段。
- Tier 3 概念（PrivateLink、Bastion Host、IPv6、Elastic IP、ENI、Placement Group）在当前仓库暂无对应原子页，属于潜在悬空链接。

## 已执行的修正策略
- 采用“规范名文件 + aliases 承载简称/同义词”策略，统一双向连接入口。
- 拆分 Public Subnet 和 Private Subnet 为独立原子卡。
- 每个原子卡统一为 5 段：定义、用途、概念、概念关联、关系。

## 进一步建议
- 为 Tier 3 概念补齐原子卡，消除悬空链接。
- 将主文档保留为 MOC（Map of Content）索引页，减少重复内容。
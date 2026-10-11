---
title: 'Lab 46 · Why Apache Iceberg exists'
description: 'Produce semantic or architecture evidence for Chapter 46.'
prev:
  text: Chapter 46
  link: /iceberg/46-why-iceberg
next:
  text: Next dependency
  link: /iceberg/47-metadata-snapshots
---

# Lab 46 · Why Apache Iceberg exists

Read [Chapter 46](/iceberg/46-why-iceberg) first. This exercise uses synthetic data or an explicit architecture brief; no cloud account is needed.

## Brief

Lake có /events/date=2026-10-01/*.parquet và thư mục ngày tiếp theo. Một writer sửa attribution bằng file mới, writer khác append; dashboard glob cả file cũ và mới. Revenue tăng gấp đôi dù mỗi file hợp lệ. Bạn cần UPDATE, DELETE, schema/history và thay partition layout.

## Work

1. Chạy smoke và ghi Spark/Iceberg/Scala versions.
2. Vẽ bốn layers cho raw lake và Iceberg table.
3. Giải thích vì sao total300 từ table không chứng minh concurrent writer safety.

## Evidence packet

Submit inputs/assumptions, a hypothesis, observed output or sourced capabilities, a rejected alternative, failure analysis and a decision with acceptance/reversal criteria. Tag each item LOCAL ICEBERG, SOURCED PLATFORM or ARCHITECTURE EVIDENCE.


Run `python scripts/test_iceberg.py` and identify the relevant contract in `labs/iceberg/experiments.py`. [Selected runtime artifacts](/labs/iceberg-evidence) are a worked reference, not your own execution.

## Failure review

Một batch ghi Parquet thành công nhưng metadata commit thất bại. Glob path thấy uncommitted files, table reader giữ committed snapshot. Đừng chạy orphan cleanup bằng tuổi file tùy ý khi writers còn hoạt động.

Name the violated invariant, responsible layer and a test that distinguishes the cause from a competing hypothesis.

## PASS criteria

PASS requires every work item and an evidence-scoped conclusion. NOT YET: feature checklist, unqualified speed claims, or format/catalog/platform conflation.

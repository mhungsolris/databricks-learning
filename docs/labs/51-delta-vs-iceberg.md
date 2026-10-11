---
title: 'Lab 51 · Delta Lake versus Apache Iceberg'
description: 'Produce semantic or architecture evidence for Chapter 51.'
prev:
  text: Chapter 51
  link: /iceberg/51-delta-vs-iceberg
next:
  text: Next dependency
  link: /iceberg/52-managed-iceberg
---

# Lab 51 · Delta Lake versus Apache Iceberg

Read [Chapter 51](/iceberg/51-delta-vs-iceberg) first. This exercise uses synthetic data or an explicit architecture brief; no cloud account is needed.

## Brief

ROAS uses Delta MERGE and streaming recovery already tested. A partner wants Iceberg access. Should the team rewrite all tables, expose read metadata, or keep a separately governed export?

## Work

1. Write a comparison of semantics and ownership, with no winner ranking.
2. Choose read exposure versus migration for a partner reader.
3. Define lag, retention, writer authority and exact business reconciliation acceptance.

## Evidence packet

Submit inputs/assumptions, a hypothesis, observed output or sourced capabilities, a rejected alternative, failure analysis and a decision with acceptance/reversal criteria. Tag each item LOCAL ICEBERG, SOURCED PLATFORM or ARCHITECTURE EVIDENCE.


Use [current platform support](/iceberg/current-platform-support) and [decision ADRs](/adr/ADR-002-platform-choice). No platform benchmark or cloud deployment is claimed by this exercise.

## Failure review

Partner reads a pinned old JSON path while Delta commits continue. Another engine writes through Iceberg to a read-only exposure. Retention cleans files the stale consumer needs.

Name the violated invariant, responsible layer and a test that distinguishes the cause from a competing hypothesis.

## PASS criteria

PASS requires every work item and an evidence-scoped conclusion. NOT YET: feature checklist, unqualified speed claims, or format/catalog/platform conflation.

---
title: Cách học handbook
description: Dùng scenario, local lab và PASS criteria để chuyển kinh nghiệm production sang Lakehouse.
prev:
  text: Learning path
  link: /guide/learning-path
next:
  text: '00 · Databricks & Lakehouse'
  link: /foundations/00-mental-model
---

# Cách học handbook

Đọc scenario trước, viết giả thuyết của bạn, rồi mới xem mechanics và fix. Với mỗi câu trả lời, nêu grain, key, failure boundary và bằng chứng cần thu thập.

## Một vòng học

| Bước | Làm gì | Dừng khi |
|---|---|---|
| Scenario | Dự đoán output bằng dữ liệu nhỏ | Có giả thuyết có thể kiểm tra |
| Mental model | Đặt từng thành phần đúng lớp | Phân biệt data files với table state |
| Lab | Chạy baseline rồi failure case | Có output và assertions |
| Production notes | Nêu điều kiện mà ví dụ không mô phỏng | Không overclaim guarantee |
| Interview | Giải thích trong 90 giây, rồi nêu trade-off | Có alternative và điều kiện thay đổi lựa chọn |

## PASS / NOT YET

PASS là năng lực cụ thể ở cuối chương, không phải đã đọc hết. Nếu bạn chỉ nhớ từ “Lakehouse” nhưng chưa giải thích được table state sau compaction, chọn NOT YET và quay lại lab.

Bạn có thể ghi checkpoint cá nhân ở nơi riêng. `PROGRESS.md` theo dõi chất lượng bài trong repository; nó không theo dõi tiến độ của người học.

## Môi trường và chi phí

| Nhãn | Định nghĩa | Quy tắc |
|---|---|---|
| FREE | Chạy local, không dùng dịch vụ cloud tính phí | Có thể cần CPU/disk và tải package |
| LOW COST | Cần compute/cloud, quy mô nhỏ có cost estimate | Reader tự bật resource và đặt budget |
| OPTIONAL CLOUD | Phần platform cần workspace và quyền | Ghi requirement, không provision tự động |

Portable Labs 00-03 chỉ cần Python 3.10+, không cần account hay token. Lab 03 còn có real Spark variant; Labs03-08 dùng [pinned Docker runtime](/setup/local-spark). Correctness Labs09/10/13 là deterministic models;11/12/14/15 thực thi actual Delta. Các lab hiện tại FREE/local, cần CPU/disk và có thể tải image/Maven dependencies, không cần Databricks workspace.

Sau Chapter15, làm [Mid Gate — Pipeline Correctness](/assessments/mid-gate-pipeline-correctness) với dataset riêng. Ghi decisions/expected states trước khi mở reviewer material ở repository; website không có answer reveal. Gate yêu cầu causal reasoning và business invariants qua retries, mutable updates và backfill.

## Kiểm tra nguồn

[Sources](./sources) ghi ngày xác minh và cloud của các claim. Apache Spark “latest” không có nghĩa Databricks Runtime của bạn sử dụng cùng version. Trước khi chạy snippet platform, kiểm tra runtime, permissions và official docs cho cloud đang dùng.

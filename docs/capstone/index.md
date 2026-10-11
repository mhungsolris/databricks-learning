---
description: Near-real-time Advertising ROAS Platform, learner-led final assessment.
---

# Near-real-time Advertising ROAS Platform

Capstone này đánh giá quyết định và bằng chứng do người học tạo. Trạng thái: **NOT YET**, chưa có bài nộp hoặc kết quả đánh giá.

## Assessment sequence

Người học làm requirements interview trước. Reviewer trả lời câu hỏi, yêu cầu làm rõ và chấm rubric trước khi mở bài modeling.

Sau modeling, người học đề xuất kiến trúc và ADRs. Implementation, failure injection, recovery và Final Mid Gate cần bằng chứng riêng.

Mỗi phần dừng tại bài nộp. Reviewer chỉ công bố nhận xét và missing cases sau lần thử của người học. Không có kiến trúc được chọn sẵn.

## Phase 1: requirements interview

Bạn là Data Engineer phụ trách yêu cầu dưới đây. Stakeholder là Marketing Lead; Finance sẽ đối soát số liệu.

> Chúng tôi cần báo cáo ROAS cho quảng cáo ứng dụng. Revenue từ callbacks cần xuất hiện sau khoảng 15 phút. Cost lấy theo giờ hoặc lịch mà nguồn cho phép. Attribution lịch sử có thể thay đổi trong 72 giờ. Marketing muốn thấy revenue, cost, installs, paying users và ROAS theo date, campaign, platform, country và app. Có thể bổ sung creative sau.

Nguồn dự kiến: Adjust callbacks/events, Adjust hoặc attribution files, Google Ads, Meta Ads, TikTok Ads và Unity Ads. Bài thực hành dùng synthetic/mock sources khi thiếu credentials; không yêu cầu paid APIs.

Hệ thống phải chịu API retries, duplicate callbacks, delayed files, source corrections, partial failures, job retries, replay và schema changes. Các phát biểu này là yêu cầu tình huống, chưa phải source contracts đã được xác nhận.

Thông tin về volume, retention, cloud, ngân sách, reconciliation authority và mức chấp nhận lỗi chưa được cung cấp. Các nguồn chưa có business keys hoặc timestamp semantics được xác nhận.

## Submission

Viết requirements interview của bạn. Ưu tiên câu hỏi theo mức ảnh hưởng tới business và khả năng thay đổi thiết kế.

Với mỗi câu hỏi, nêu:

1. Câu hỏi và người cần trả lời.
2. Vì sao câu trả lời ảnh hưởng đến business hoặc correctness.
3. Quyết định nào phụ thuộc câu trả lời; mô tả hướng thay đổi nếu các câu trả lời khác nhau.
4. Mức ưu tiên và rủi ro nếu chưa có câu trả lời.

Kết thúc bằng danh sách assumptions tạm thời, các blockers cần xác nhận và acceptance criteria có thể kiểm chứng. Chưa cần chọn công nghệ, vẽ kiến trúc hoặc viết code.

## Rubric

| Area | Maximum | Evidence required |
|---|---:|---|
| Business purpose and reporting semantics | 20 | Làm rõ người dùng, cách sử dụng số liệu và ý nghĩa các metrics/dimensions |
| Source identity and change behavior | 20 | Câu hỏi về keys, revisions, retries và ý nghĩa thời gian của nguồn |
| SLA and recovery boundaries | 20 | Làm rõ freshness, delay tolerance, backfill và reconciliation authority |
| Operational constraints | 20 | Làm rõ volume, retention, cost, cloud, access và governance |
| Prioritization and acceptance | 20 | WHY cho câu hỏi, phân biệt fact/assumption, blockers và tiêu chí đo được |

Mỗi area: 0 điểm nếu thiếu; 10 điểm nếu có câu hỏi nhưng thiếu tác động hoặc cách xác nhận; 20 điểm nếu có rationale, owner và ảnh hưởng đến quyết định. Reviewer có thể cho điểm trung gian với nhận xét gắn từng câu hỏi.

PASS requirements interview: ít nhất 80/100, mỗi area ít nhất 10 điểm. Chỉ liệt kê câu hỏi kỹ thuật mà thiếu WHY sẽ nhận NOT YET. Điểm này chỉ áp dụng Phase 1, không thay thế Final Mid Gate.

## Evidence boundaries

Handbook coverage, runtime baseline và website build không xác nhận năng lực của người học. Reviewer cần bài nộp, tests, ADRs và incident responses có thể truy nguyên trước khi chấm competency.

Hiện chưa có capstone implementation evidence, learner score hoặc Databricks workspace evidence cho capstone. Version 1.0 và Final Mid Gate chưa được thông qua.

**Dừng tại đây. Nộp requirements interview trước khi mở phần tiếp theo.**

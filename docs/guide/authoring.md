---
title: Viết chương mới
description: Template và quality gate cho nội dung handbook, lab và checkpoint.
---

# Viết chương mới

Dùng Chapter 00 làm mẫu về độ cụ thể và `templates/chapter.md` trong repository làm schema. Template chưa phải bài học cho reader.

## Content contract

| Phần | Bằng chứng cần có |
|---|---|
| Header | level, priority, effort; prerequisite links tồn tại |
| Scenario | Input nhỏ, câu hỏi reasoning và kết quả sai có thể tính |
| Mental model / mechanics | Diagram chỉ khi giải thích quan hệ; nói rõ giới hạn |
| Implementation / code | Runtime hoặc lab context; code được kiểm tra |
| Failure / debugging | Symptom → investigation → diagnosis → fix |
| Mapping | BigQuery/Airflow bridge có boundary, không ép 1:1 |
| Interview / PASS | 3-10 scenario questions; năng lực đo được |
| Sources | Official URL, verification date, cloud/version context |

## Reusable components

Đặt `level`, `priority`, `effort` trong frontmatter rồi dùng `ChapterMeta`. Prerequisites là Markdown links trong slot:

```md
<ChapterMeta>

[Learning path](/guide/learning-path)

</ChapterMeta>
```

Fence `mermaid` được render ở client, có source fallback và đổi theme theo giao diện. Code fence Python/SQL dùng syntax highlighting/copy button mặc định. Callouts dùng `::: tip`, `::: warning`, `::: info`; chỉ thêm khi có decision hoặc failure cần reader chú ý.

## Quality gate

Chạy `npm run docs:check`, `npm run docs:build`, `python -m unittest discover -s tests -v`, `python -m scripts.run_labs` và browser check khi sửa navigation/layout/diagram. Website build không bỏ qua dead links. Chỉ đánh dấu bài verified trong `PROGRESS.md` khi nguồn, code, links, Mermaid, layout và chapter schema đều được kiểm tra. Phân biệt lab measured output với reading examples chưa chạy ở runtime vendor.

Các sidebar entries có hậu tố “kế hoạch” trỏ tới curriculum. Khi thêm bài đã kiểm tra, chuyển link sang bài thật; không tạo các trang một dòng để lấp navigation.

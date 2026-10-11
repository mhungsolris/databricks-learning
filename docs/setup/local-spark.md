---
title: Spark local runtime
description: Chạy Spark thật trên Windows bằng official Linux image, không cần workspace hoặc cloud.
---

# Spark local runtime

**FREE · local[*] · không cần Databricks workspace.** Chạy từ repository root bằng PowerShell. Docker Desktop dùng Linux containers phải được cài và hoạt động; host cần Python 3.10+ để chạy wrapper. Website vẫn chỉ cần Node và portable labs vẫn chỉ cần Python.

## Runtime contract

| Thành phần | Đã kiểm chứng 2026-10-10 |
|---|---|
| Host | Windows, Python 3.12.10; Java/PySpark không có trên PATH |
| Engine | Apache Spark 4.0.4; official `apache/spark:4.0.4-python3` |
| Pin | Image digest trong `runtime/spark.json`; không dùng floating latest |
| JVM | Java 17.0.19 trong container; Spark 4.0.4 hỗ trợ Java 17/21 |
| Python engine | Version thực tế lưu trong `runtime.json`, tách khỏi host Python |
| Execution | `local[*]`, driver/executor cùng container; 2 CPU quota, 4 GiB limit, driver heap 1 GiB |
| Diagnostic settings | 4 shuffle partitions, AQE false để đọc plan; không phải production tuning defaults |
| Delta | Maven `io.delta:delta-spark_2.13:4.0.1`, extension/catalog; command riêng Lab 08 |

Container đọc source tại `/workspace` với mount read-only, chỉ ghi artifact vào `.skills-test/spark` qua `/evidence`. Container user root dùng để RW output nhất quán trên Windows/Linux CI; không chạy privileged hoặc mount Docker socket. Không thay đổi JDK/Python toàn hệ thống. Đây là đường chạy được chọn; cài PySpark native Windows cần Java phù hợp và Hadoop/filesystem compatibility riêng, chưa được kiểm chứng ở đây.

## Setup và verify

Nếu chưa có Docker Desktop, cài theo [Windows prerequisites](https://docs.docker.com/desktop/setup/install/windows-install/), bảo đảm virtualization/WSL2 backend hoạt động. Không cần tự cài distro WSL để chạy labs này. Nếu đã có Desktop:

```powershell
docker desktop start
docker desktop status
docker info --format '{{.OSType}}'
$sparkImage = (Get-Content runtime/spark.json | ConvertFrom-Json).image
docker pull $sparkImage
python scripts/verify_spark.py
```

Expected Docker OS: `linux`. First pull có thể tải image lớn; pull/network và Docker daemon là prerequisites. Runtime không pip-install PySpark vào host. Smoke output có startup INFO, sau đó:

```text
PASS Spark 4.0.4; master=local[*]; DataFrame=5; SQL=45; Parquet=10
PASS clean SparkSession shutdown
Evidence: /evidence/smoke/<run-id>; completed stages: 8
```

Stage count là một observed run, không là API guarantee. Warning `NativeCodeLoader ... builtin-java classes` đã xuất hiện nhưng không làm smoke thất bại. `runtime.json`, `result.json`, `shutdown.json`, `stages.json` và event logs lưu tại host `.skills-test/spark/smoke/<run-id>`. Script trả nonzero khi assertion/runtime thất bại.

## Chạy labs và tests

```powershell
python scripts/run_spark.py --lab all
python scripts/run_spark.py --lab 04
python scripts/run_spark.py --lab 08
python scripts/test_spark.py
python scripts/test_spark.py --delta
```

`all` chạy 03-07; 08 opt-in để dependency Delta không ảnh hưởng Spark basics. Mỗi run tạo folder riêng; không overwrite kết quả cũ. Delta cần network lần đầu để resolve ba Maven artifacts; Ivy cache nằm trong ignored evidence directory. Không cài Python Delta package vì lab sử dụng SQL/DataFrame integration của JVM.

## Correctness labs on the same runtime

```powershell
python scripts/run_correctness.py --lab all
python scripts/test_correctness.py
```

Labs09/10/13 là deterministic business models;11/12/14/15 thực thi actual Delta writes/history. Cùng image/Maven pins, repository read-only và ignored evidence mount như Spark labs. [Correctness artifacts](/labs/correctness-evidence) giữ selected state/history/reconciliation; mọi API source là synthetic fixtures. `test_correctness.py` chạy9 contracts, không skip/fallback engine. Một suite bounded mất vài phút trên local host; không dùng elapsed time để suy ra production throughput.

## Optional Spark UI

```powershell
python scripts/run_spark.py --lab 05 --ui --hold-seconds 120
```

Mở `http://127.0.0.1:4040` khi application còn chạy. Xem SQL → physical plan; Jobs → Stage IDs; Stages → task count, shuffle read/write, spill. Wrapper publish port chỉ trên loopback, giữ application tối đa 300 giây khi yêu cầu. `jobs.json` map lab tới stages; `stages.json` lấy từ actual event logs sau shutdown. Automated tests dùng artifacts, không cần UI. Local mode không đo network transfer giữa machines, throughput production hoặc recovery cluster.

## Shutdown

Script gọi `spark.stop()` trong finally, xác nhận SparkContext đã dừng, Docker `--rm` xóa container. Ctrl+C để hủy run đang giữ UI; có thể kiểm tra `docker ps` và dừng **đúng container lab** bằng `docker stop <id>`. Docker Desktop service vẫn chạy để dùng lại; khi không cần có thể `docker desktop stop`. Không chạy broad stop/delete hoặc xóa evidence của run khác.

## Windows troubleshooting

| Symptom | Kiểm tra và cách xử lý |
|---|---|
| Cannot connect named pipe / daemon | `docker desktop status`; start Desktop rồi `docker info` |
| Windows containers / image mismatch | Chuyển Desktop sang Linux containers, kiểm tra OSType |
| Virtualization/WSL error | Theo prerequisites Docker; không tải winutils để chữa backend error |
| Bind mount denied / path with spaces | Cho Docker truy cập repository drive; wrapper truyền argument list, không nối shell strings |
| UI port 4040 busy | Dừng đúng app đang dùng port hoặc bỏ `--ui`; tests không dùng port mapping |
| Java gateway exits / OOM | Xem stderr và Docker resources; chạy từng lab, không tăng dataset tùy ý |
| Delta Maven unavailable | Kiểm tra network/proxy/trust; Spark 03-07 vẫn độc lập; không vô hiệu hóa TLS |
| Không thấy generated files ở docs | Evidence mặc định ignored; xem host `.skills-test/spark`, bản selected artifacts ở [evidence](/labs/runtime-evidence) |

## Official references

Đối chiếu 2026-10-10: [Spark 4.0.4 requirements](https://spark.apache.org/docs/4.0.4/), [PySpark install](https://spark.apache.org/docs/4.0.4/api/python/getting_started/install.html), [Apache Spark Docker source](https://github.com/apache/spark-docker), [Docker Desktop CLI](https://docs.docker.com/desktop/features/desktop-cli/), [Spark monitoring](https://spark.apache.org/docs/4.0.4/monitoring.html), [Delta compatibility](https://docs.delta.io/releases/). Local OSS versions không đại diện cho một Databricks Runtime.

# reference-site

Source: https://vudaian24.github.io/learn-devops/07-terraform.html
Retrieved: 2026-10-10

Bước 7 · Terraform ← Học DevOps Bước 1 · Linux Bước 2 · Mạng & Bảo mật Bước 3 · Docker Bước 4 · Kubernetes Bước 5 · CI/CD Bước 6 · Monitoring Bước 7 · Terraform 
Mục lục 
Terraform & IaC là gì 
Workflow cơ bản 
Cú pháp HCL 
Variables & Outputs 
State — file trạng thái 
Remote backend & locking 
Modules 
Quản lý state qua CLI 
Nhiều môi trường 
Best practices 
Bước 07 
Terraform cho DevOps 
Định nghĩa hạ tầng bằng code thay vì thao tác tay qua console — dễ review, dễ tái lập, dễ tái sử dụng. 10 phần đi từ khái niệm IaC, cú pháp HCL, state, đến module và vận hành nhiều môi trường an toàn. 
01 Terraform & Infrastructure as Code là gì 
IaC nghĩa là khai báo hạ tầng (server, mạng, database...) bằng file cấu hình có thể versioning, review, và tái sử dụng — thay vì click tay qua console, vốn không để lại lịch sử và khó tái lập chính xác. 
Khái niệm Mô tả 
Declarative Bạn khai báo trạng thái hạ tầng mong muốn — Terraform tự tính toán các bước cần làm để đạt được nó, khác với cách viết tuần tự từng lệnh (imperative). 
Provider Plugin để Terraform giao tiếp với một nền tảng cụ thể — AWS, Google Cloud, Azure, Kubernetes, hay cả GitHub/Datadog. 
Resource Một đối tượng hạ tầng cụ thể được Terraform tạo và quản lý, ví dụ một máy chủ hay một bucket lưu trữ. 
HCL (HashiCorp Configuration Language) Ngôn ngữ cấu hình dùng để viết file .tf — cú pháp khai báo, dễ đọc hơn JSON/YAML thuần cho việc này. Terraform khác các công cụ configuration management (Ansible, Chef) ở chỗ nó tập trung vào việc tạo/xóa/thay đổi hạ tầng (server, mạng, database), trong khi các công cụ kia tập trung cấu hình bên trong một máy đã tồn tại. 
02 Workflow cơ bản 
Vòng lặp làm việc cốt lõi của Terraform luôn là ba bước: khởi tạo, xem trước thay đổi, rồi mới áp dụng. 
Lệnh Mô tả Ví dụ 
terraform init Tải provider/module cần thiết, cấu hình backend, tạo file khóa version .terraform.lock.hcl . terraform init 
terraform plan Xem trước những gì sẽ thay đổi (tạo/sửa/xóa) mà chưa thực sự áp dụng. terraform plan -out=tfplan 
terraform apply Áp dụng thay đổi vào hạ tầng thật, hỏi xác nhận trước khi thực thi. terraform apply tfplan 
terraform destroy Xóa toàn bộ resource đang được quản lý trong state hiện tại. terraform destroy 
terraform fmt Tự động format lại code theo chuẩn HCL. terraform fmt -recursive 
terraform validate Kiểm tra cú pháp và tính nhất quán của cấu hình trước khi plan. terraform validate Luôn chạy terraform plan và đọc kỹ output trước khi apply — đây là bước review quan trọng nhất, tương đương code review cho hạ tầng. 
03 Cú pháp HCL cơ bản 
Một file cấu hình Terraform gồm các block khai báo lồng nhau — mỗi loại block có vai trò riêng. 
provider "aws" {
  region = "us-east-1" } resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro" tags = {
    Name = "web-server" }
} data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = [ "099720109477" ]
} 
Block Mô tả 
terraform {} Cấu hình chung: version Terraform yêu cầu, khai báo backend, provider cần dùng. 
provider Cấu hình cho một provider cụ thể (region, credentials, alias...). 
resource Khai báo một resource sẽ được tạo/quản lý — cú pháp resource "loại" "tên_local" . 
data Đọc thông tin từ resource đã tồn tại sẵn (không do Terraform tạo ra) để tham chiếu. 
variable / output Đầu vào và đầu ra của cấu hình (xem mục 04). 
locals Đặt tên cho một biểu thức để tái sử dụng nhiều lần trong cùng module, tránh lặp lại. 
04 Variables & Outputs 
Variables tham số hóa cấu hình để tái sử dụng; Outputs expose giá trị ra ngoài để dùng ở nơi khác (module cha, hoặc đọc bằng CLI). 
variable "instance_type" {
  description = "Loại instance cho web server" type        = string
  default     = "t3.micro" } variable "db_password" {
  type      = string
  sensitive = true
} output "instance_public_ip" {
  description = "IP public của web server" value       = aws_instance.web.public_ip
} 
Thuộc tính Mô tả 
type Kiểu dữ liệu: string , number , bool , list , map , object . 
default Giá trị mặc định nếu không truyền vào — bỏ trống nghĩa là bắt buộc phải cung cấp. 
sensitive Ẩn giá trị khỏi output log của plan / apply — không phải mã hóa, chỉ ẩn hiển thị. 
validation Ràng buộc điều kiện hợp lệ cho giá trị truyền vào, báo lỗi sớm nếu sai. Truyền giá trị biến qua: -var="key=value" , file .tfvars qua -var-file , biến môi trường TF_VAR_ten_bien , hoặc giá trị default nếu không truyền gì. 
05 State — file trạng thái 
Terraform cần biết resource nào nó đã tạo và ánh xạ với ID thật trên hạ tầng — thông tin này lưu trong file trạng thái terraform.tfstate . 
Khái niệm Mô tả 
State file File JSON ánh xạ resource khai báo trong code với ID thực tế trên hạ tầng, cùng toàn bộ attribute hiện tại. 
Vai trò của state Giúp Terraform biết cái gì đã tồn tại (không tạo trùng), tính toán diff cho plan , và lưu cache attribute để tăng tốc. 
Drift Khi hạ tầng thật bị thay đổi thủ công (ngoài Terraform), state không còn khớp thực tế — plan sẽ phát hiện và đề xuất đưa về đúng cấu hình. Không bao giờ sửa tay file .tfstate , và không commit nó vào Git — state thường chứa giá trị nhạy cảm ở dạng plaintext (mật khẩu, key) do Terraform cần lưu toàn bộ attribute của resource. 
06 Remote backend & state locking 
Mặc định state nằm trên máy local — không phù hợp khi làm việc nhóm. Remote backend lưu state ở một nơi tập trung mà mọi người cùng truy cập. 
terraform { backend "s3" {
    bucket       = "my-terraform-state" key          = "project/terraform.tfstate" region       = "us-east-1" encrypt      = true
    use_lockfile = true
  }
} 
Khái niệm Mô tả 
Local backend Mặc định — state chỉ nằm trên máy đang chạy Terraform, không chia sẻ được. 
Remote backend State lưu ở nơi tập trung (S3, HCP Terraform, Azure Storage...) để cả team dùng chung một nguồn sự thật. 
State locking Khóa state trong lúc chạy để ngăn hai người apply đồng thời làm hỏng state — với backend S3, bật qua use_lockfile (hoặc DynamoDB table ở cấu hình cũ hơn). Bất kỳ dự án nào có từ 2 người trở lên cùng chạy Terraform đều nên dùng remote backend có state locking — đây gần như là yêu cầu bắt buộc, không phải tùy chọn. 
07 Modules — tái sử dụng cấu hình 
Module là một thư mục chứa file .tf đóng gói một phần hạ tầng có thể tái sử dụng, nhận đầu vào qua variables và trả đầu ra qua outputs. 
module "web_server" {
  source = "./modules/ec2-instance" instance_type = "t3.micro" environment   = "staging" } output "web_public_ip" {
  value = module.web_server.public_ip
} 
Khái niệm Mô tả 
Root module Thư mục Terraform bạn chạy trực tiếp terraform apply — có thể gọi vào nhiều module con. 
Child module Module được gọi từ module khác qua block module , nhận input qua argument, trả output qua module.tên.output . 
Module Registry registry.terraform.io — kho module công khai đã kiểm định, có thể dùng ngay thay vì viết lại từ đầu. Module giúp tránh lặp code khi cùng một loại hạ tầng (ví dụ một cụm máy chủ web) cần tạo nhiều lần cho nhiều môi trường khác nhau. 
08 Quản lý state qua CLI 
Đôi khi cần thao tác trực tiếp lên state mà không sửa hạ tầng thật — Terraform cung cấp lệnh riêng cho việc này thay vì sửa tay file JSON. 
Lệnh Mô tả Ví dụ 
terraform state list Liệt kê toàn bộ resource đang được quản lý trong state. terraform state list 
terraform state show Xem chi tiết attribute hiện tại của một resource trong state. terraform state show aws_instance.web 
terraform state mv Đổi tên resource trong state mà không xóa/tạo lại hạ tầng thật. terraform state mv aws_instance.old aws_instance.new 
terraform state rm Gỡ một resource khỏi state (Terraform ngừng quản lý) mà không xóa hạ tầng thật. terraform state rm aws_instance.web 
terraform import Đưa một resource đã tồn tại sẵn (tạo thủ công trước đó) vào state để Terraform quản lý. terraform import aws_instance.web i-0123456789 
terraform apply -replace Buộc hủy và tạo lại một resource cụ thể, có hiển thị trong plan để review trước. terraform apply -replace="aws_instance.web" terraform taint đã deprecated — dùng apply -replace thay thế vì thay đổi sẽ hiện rõ trong plan trước khi thực thi, thay vì âm thầm đánh dấu. 
09 Quản lý nhiều môi trường 
Hầu hết dự án cần tách biệt ít nhất hai môi trường (ví dụ staging và production) — có vài cách phổ biến để làm việc này. 
Cách tiếp cận Mô tả 
Terraform workspaces terraform workspace new/select — nhiều state độc lập trong cùng một backend config, phân biệt qua biến terraform.workspace . 
Thư mục riêng theo môi trường Mỗi môi trường một thư mục cấu hình + backend key riêng — cách ly rõ ràng nhất, khuyến nghị khi dev và production khác biệt lớn (region, quy mô, quyền truy cập). 
-var-file theo môi trường Dùng chung code, chỉ đổi file giá trị biến ( dev.tfvars , prod.tfvars ) khi apply. Workspaces tiện cho các biến thể nhỏ (ví dụ nhiều bản demo tạm), nhưng vì chúng share chung backend configuration, tách thư mục/state riêng vẫn là lựa chọn an toàn hơn giữa staging và production. 
10 Best practices 
Luôn chạy và đọc kỹ terraform plan trước khi apply , đặc biệt trên production. 
Commit file .terraform.lock.hcl vào Git để khóa version provider nhất quán giữa mọi người. 
Không commit .tfstate hay thư mục .terraform/ vào Git — thêm vào .gitignore , dùng remote backend thay thế. 
Luôn dùng remote backend có state locking khi có từ 2 người trở lên cùng chạy Terraform. 
Pin version cụ thể cho provider/module, tránh version range quá rộng gây thay đổi bất ngờ giữa các lần chạy. 
Dùng apply -replace thay vì lệnh taint đã deprecated. 
Tách state theo môi trường hoặc theo mức độ ảnh hưởng (blast radius) — không gộp toàn bộ hạ tầng vào một state duy nhất. 
Không hard-code secret trong file .tf — dùng biến sensitive kết hợp secrets manager của cloud provider. 
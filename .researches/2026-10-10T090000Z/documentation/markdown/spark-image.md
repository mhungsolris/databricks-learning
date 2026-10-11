# spark-image

Source: https://github.com/apache/spark-docker
Retrieved: 2026-10-10

GitHub - apache/spark-docker: Official Dockerfile for Apache Spark · GitHub Skip to content 
Navigation Menu Sign in Appearance settings 
Platform 
AI CODE CREATION 
GitHub Copilot Write better code with AI 
GitHub Copilot app Direct agents from issue to merge 
MCP Registry Integrate external tools 
DEVELOPER WORKFLOWS 
Actions Automate any workflow 
Codespaces Instant dev environments 
Issues Plan and track work 
Code Review Manage code changes 
Code Quality Enforce quality at merge 
APPLICATION SECURITY 
GitHub Advanced Security Find and fix vulnerabilities 
Code security Secure your code as you build 
Secret protection Stop leaks before they start 
EXPLORE 
Why GitHub 
Documentation 
Blog 
Changelog 
Marketplace View all features 
Solutions 
BY COMPANY SIZE 
Enterprises 
Small and medium teams 
Startups 
Nonprofits 
BY USE CASE 
App Modernization 
DevSecOps 
DevOps 
CI/CD 
View all use cases 
BY INDUSTRY 
Healthcare 
Financial services 
Manufacturing 
Government 
View all industries View all solutions 
Resources 
EXPLORE BY TOPIC 
AI 
Software Development 
DevOps 
Security 
View all topics 
EXPLORE BY TYPE 
Customer stories 
Events & webinars 
Ebooks & reports 
Business insights 
GitHub Skills 
SUPPORT & SERVICES 
Documentation 
Customer support 
Community forum 
Trust center 
Partners View all resources 
Open Source 
COMMUNITY 
GitHub Sponsors Fund open source developers 
PROGRAMS 
Security Lab 
Maintainer Community 
GitHub Stars 
Archive Program 
REPOSITORIES 
Topics 
Trending 
Collections 
Enterprise 
ENTERPRISE SOLUTIONS 
Enterprise platform AI-powered developer platform 
AVAILABLE ADD-ONS 
GitHub Advanced Security Enterprise-grade security features 
Copilot for Business Enterprise-grade AI features 
Premium Support Enterprise-grade 24/7 support 
Pricing Search / Sign in Sign up Appearance settings You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert {{ message }} 
apache 
spark-docker 
Repository navigation 

Code 
Issues 2 ( 2 ) 
Pull requests 3 ( 3 ) 
Actions 
Security and quality 
Insights More items spark-docker Public 
Notifications You must be signed in to change notification settings 
Fork 64 ( 64 ) 
Star 176 ( 176 ) You must be signed in to star a repository 
About 
Official Dockerfile for Apache Spark spark.apache.org/ 
Topics big-data java jdbc python r scala spark sql 
Resources Readme Apache-2.0 license 
Code of conduct Code of conduct 
Contributing Contributing 
Security policy Security policy Activity Custom properties 
Stars 176 stars 
Watchers 23 watching 
Forks 64 forks Report repository master Branches Tags Go to file Code Open more actions menu 
Latest commit 
History 119 Commits 119 Commits 
Folders and files 
Name Name Last commit message Last commit date 
.github .github 
3.5.0 3.5.0 
3.5.1 3.5.1 
3.5.2 3.5.2 
3.5.3 3.5.3 
3.5.4 3.5.4 
3.5.5 3.5.5 
3.5.6 3.5.6 
3.5.7 3.5.7 
3.5.8 3.5.8 
3.5.9 3.5.9 
4.0.0 4.0.0 
4.0.1 4.0.1 
4.0.2 4.0.2 
4.0.3 4.0.3 
4.0.4 4.0.4 
4.1.0 4.1.0 
4.1.1 4.1.1 
4.1.2 4.1.2 
4.1.3 4.1.3 
4.2.0-preview5 4.2.0-preview5 
4.2.0 4.2.0 
dev dev 
testing testing 
tools tools 
.asf.yaml .asf.yaml 
.gitignore .gitignore 
AGENTS.md AGENTS.md 
CONTRIBUTING.md CONTRIBUTING.md 
Dockerfile.template Dockerfile.template 
LICENSE LICENSE 
NOTICE NOTICE 
OVERVIEW.md OVERVIEW.md 
README.md README.md 
SECURITY.md SECURITY.md 
add-dockerfiles.sh add-dockerfiles.sh 
awesome-spark-docker.md awesome-spark-docker.md 
entrypoint.sh.template entrypoint.sh.template 
r-python.template r-python.template 
versions.json versions.json 
View all files 
Repository files navigation 

README 
Code of conduct 
Contributing 
Apache-2.0 license 
Security More items 
Apache Spark Official Dockerfiles 
What is Apache Spark? 
Spark is a unified analytics engine for large-scale data processing. It provides
high-level APIs in Scala, Java, Python, and R, and an optimized engine that
supports general computation graphs for data analysis. It also supports a
rich set of higher-level tools including Spark SQL for SQL and DataFrames,
pandas API on Spark for pandas workloads, MLlib for machine learning, GraphX for graph processing,
and Structured Streaming for stream processing. 
https://spark.apache.org/ 
Create a new version 
Step 1 Add dockerfiles for a new version. 
You can see 3.4.0 PR as reference. 

1.1 Add gpg key to tools/template.py 
This gpg key will be used by Dockerfiles (such as 3.4.0 ) to verify the signature of the Apache Spark tarball. 

1.2 Add image build workflow (such as 3.4.0 yaml ) 
This file will be used by GitHub Actions to build the Docker image when you submit the PR to make sure dockerfiles are correct and pass all tests (build/standalone/kubernetes). 

1.3 Using ./add-dockerfiles.sh [version] to add Dockerfiles. 
You will get a new directory with the Dockerfiles for the specified version. 

1.4 Add version and tag info to versions.json, publish.yml and test.yml. 
This version file will be used by image build workflow (such as 3.4.0 reference) and docker official image. 
Step 2. Publish apache/spark Images. 
Click Publish (Java 25 only) , Publish (Java 21 only) , Publish (Java 17 only) or Publish (such as 3.x) to publish images. 
After this, the apache/spark docker images will be published. 
Step 3. Publish spark Docker Official Images. 
Submit the PR to docker-library/official-images , see (link)[ docker-library/official-images#15363 ] as reference. 
You can type tools/manifest.py manifest to generate the content. 
After this, the spark docker images will be published. 
About images 
Apache Spark Image Spark Docker Official Image 
Name apache/spark spark 
Maintenance Reviewed, published by Apache Spark community Reviewed, published and maintained by Docker community 
Update policy Only build and push once when specific version release Actively rebuild for updates and security fixes 
Link https://hub.docker.com/r/apache/spark https://hub.docker.com/_/spark 
source apache/spark-docker apache/spark-docker and docker-library/official-images 
We advise using official Apache Spark images to maintain architectural uniformity across related projects, including the Apache Spark K8s Operator and Apache Spark Connect for Swift . 
About this repository 
This repository contains the Dockerfiles used to build the Apache Spark Docker Image. 
See more in SPARK-40513: SPIP: Support Docker Official Image for Spark . 
About 
Official Dockerfile for Apache Spark spark.apache.org/ 
Topics big-data java jdbc python r scala spark sql 
Resources Readme Apache-2.0 license 
Code of conduct Code of conduct 
Contributing Contributing 
Security policy Security policy Activity Custom properties 
Stars 176 stars 
Watchers 23 watching 
Forks 64 forks Report repository 
Releases 
Packages 
Used by 
Contributors 
Languages 
Footer © 2026 GitHub, Inc. 
Footer navigation 
Terms 
Privacy 
Security 
Status 
Community 
Docs 
Contact 
Manage cookies 
Do not share my personal information You can’t perform that action at this time. 
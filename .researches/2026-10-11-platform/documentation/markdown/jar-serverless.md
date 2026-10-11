# jar-serverless

Source: https://docs.databricks.com/aws/en/jobs/how-to/use-jars-in-workflows
Retrieved: 2026-10-11

Create and run JARs on serverless compute | Databricks on AWS Skip to main content Get started Guides Develop Reference Resources Release notes Help 
Support 
Knowledge Base 
Community 
Training English 
English 
日本語 
Português 
Français AWS 
Azure 
GCP 
SAP Try Databricks 

Data engineering 
Lakeflow Jobs 
Tutorials 
Use a JAR on serverless compute On this page Last updated on Sep 11, 2026 
Create and run JARs on serverless compute important 
Databricks strongly recommends Declarative Automation Bundles instead of building and deploying JARs manually as described on this page. Declarative Automation Bundles makes it easy to create a project from a template that has the correct Scala, JDK, and Databricks Connect versions already configured for serverless, and also enables simple deployment of the JAR to the Databricks workspace. See Build a Scala JAR with Declarative Automation Bundles . 
A Java archive (JAR) packages Java or Scala code into a single file. Create a JAR with Spark code and deploy it as a JAR task on serverless compute in a Lakeflow Job. 
Requirements ​ 
To build a JAR, your local development environment must have the following installed: 
sbt 1.11.7 or higher for Scala JARs 
Maven 3.9.0 or higher for Java JARs 
JDK, Scala, and Databricks Connect versions that match your serverless environment . See Dependency versions . 
Dependency versions ​ important 
To run on serverless compute without failures, your JAR Scala and JDK versions must exactly match the runtime Scala and JDK versions. See Databricks Connect versions . 
The example on this page uses serverless environment version 4 , so this page creates a JAR that: 
Is compiled against Scala 2.13; every dependency uses the _2.13 suffix. 
Is compiled against JDK 17, class file version 61. 
Is compiled against Databricks Connect 17.3, the Spark API surface for serverless compute. 
Uses only public Spark APIs. It uses no RDDs and no Spark internals. See Limitations . 
Includes every dependency in the JAR or attached as a serverless environment library. See Managing dependencies . Limitations ​ 
Serverless compute uses Spark Connect . Your JAR runs against a thin client library that exposes the public Spark APIs, while the Spark engine itself runs server-side. Code that bypasses the public API can't benefit from Catalyst optimization or Photon acceleration, even on classic compute. RDD-based and internals-dependent code is generally slower than the equivalent DataFrame or SQL code. 
The following aren't available: 
RDD API ( org.apache.spark.rdd.* ) and SparkContext / JavaSparkContext . Use SparkSession.builder().getOrCreate() and DataFrame/Dataset operations instead. 
Spark internal APIs ( org.apache.spark.catalyst.* , org.apache.spark.util.* , org.apache.spark.sql.util.* , org.apache.spark.sql.internal.* ). Code that imports these APIs fail with NoClassDefFoundError . Refactor to the public Spark API. If a third-party library uses internals, check whether it publishes a Spark Connect-compatible release. 
Native libraries ( .so , .dll , JNI). Serverless compute does not permit writing native libraries to the file system. Libraries that unpack native binaries at startup fail with UnsatisfiedLinkError . Init scripts are not a workaround. Use a Java equivalent if one is available. 
If your workload requires any of the above, run it on standard or dedicated compute instead. 
Step 1: Build a JAR ​ 
Scala 
Java 

Run the following command to create a Scala project: Bash 
sbt new scala/scala-seed.g8 
When prompted, enter a project name, for example, my-spark-app . 

Next, delete the seed's stub files and create the directory for your source: Bash 
cd my-spark-app rm src/main/scala/example/Hello.scala rm src/test/scala/example/HelloSpec.scala rm project/Dependencies.scala mkdir -p src/main/scala/com/examples 

Replace the contents of your build.sbt file with the following: Scala 
name : = "my-spark-app" // Set the dependency versions scalaVersion : = "2.13.16" javacOptions ++ = Seq ( "--release" , "17" ) scalacOptions ++ = Seq ( "-release" , "17" ) libraryDependencies += "com.databricks" % % "databricks-connect" % "17.3.2" % "provided" // Your other dependencies go here. Use %% for Scala libraries so sbt picks the _2.13 artifact. // Fork a new JVM on run so our javaOptions are applied. fork : = true javaOptions += "--add-opens=java.base/java.nio=ALL-UNNAMED" 

Edit or create a project/plugins.sbt file, and add this line: Scala 
addSbtPlugin ( "com.eed3si9n" % "sbt-assembly" % "2.3.1" ) 

Create your main class in src/main/scala/com/examples/SparkJar.scala : Scala 
package com . examples import org . apache . spark . sql . SparkSession object SparkJar { def main ( args : Array [ String ] ) : Unit = { val spark = SparkSession . builder ( ) . getOrCreate ( ) // Prints the arguments to the class, which // are job parameters when run as a job: println ( args . mkString ( ", " ) ) // Shows using spark: println ( spark . version ) println ( spark . range ( 10 ) . limit ( 3 ) . collect ( ) . mkString ( " " ) ) } } 

To build your JAR file, run the following command: Bash 
sbt assembly 
The compiled JAR is created in the target/ folder as my-spark-app-assembly-0.1.0-SNAPSHOT.jar . 

Run the following commands to create a Maven project structure: Bash 
mkdir -p my-spark-app/src/main/java/com/examples cd my-spark-app 

Create a pom.xml file in the project root with the following contents: XML 
<?xml version="1.0" encoding="UTF-8"?> < project xmlns = " http://maven.apache.org/POM/4.0.0 " xmlns: xsi = " http://www.w3.org/2001/XMLSchema-instance " xsi: schemaLocation = " http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd " > < modelVersion > 4.0.0 </ modelVersion > < groupId > com.examples </ groupId > < artifactId > my-spark-app </ artifactId > < version > 1.0-SNAPSHOT </ version > < properties > < maven.compiler.release > 17 </ maven.compiler.release > < scala.binary.version > 2.13 </ scala.binary.version > < project.build.sourceEncoding > UTF-8 </ project.build.sourceEncoding > </ properties > < dependencies > <!-- Included on serverless compute. --> < dependency > < groupId > com.databricks </ groupId > < artifactId > databricks-connect_${scala.binary.version} </ artifactId > < version > 17.3.2 </ version > < scope > provided </ scope > </ dependency > </ dependencies > < build > < plugins > <!-- Maven Shade Plugin - Creates a fat JAR with all non-provided dependencies. --> < plugin > < groupId > org.apache.maven.plugins </ groupId > < artifactId > maven-shade-plugin </ artifactId > < version > 3.6.1 </ version > < executions > < execution > < phase > package </ phase > < goals > < goal > shade </ goal > </ goals > < configuration > < transformers > < transformer implementation = " org.apache.maven.plugins.shade.resource.ManifestResourceTransformer " > < mainClass > com.examples.SparkJar </ mainClass > </ transformer > </ transformers > </ configuration > </ execution > </ executions > </ plugin > </ plugins > </ build > </ project > 

Create your main class in src/main/java/com/examples/SparkJar.java : Java 
package com . examples ; import org . apache . spark . sql . SparkSession ; import java . util . stream . Collectors ; public class SparkJar { public static void main ( String [ ] args ) { SparkSession spark = SparkSession . builder ( ) . getOrCreate ( ) ; // Prints the arguments to the class, which // are job parameters when run as a job: System . out . println ( String . join ( ", " , args ) ) ; // Shows using spark: System . out . println ( spark . version ( ) ) ; System . out . println ( spark . range ( 10 ) . limit ( 3 ) . collectAsList ( ) . stream ( ) . map ( Object :: toString ) . collect ( Collectors . joining ( " " ) ) ) ; } } 

To build your JAR file, run the following command: Bash 
mvn clean package 
The compiled JAR is created in the target/ folder as my-spark-app-1.0-SNAPSHOT.jar . 
Manage dependencies ​ 
To make a library available to your JAR on serverless compute: 
Use a provided library : Serverless compute includes Databricks Connect and a curated set of common libraries. If your version is compatible, declare it provided in your build and don't include it in your JAR. 
Attach as an environment library : Add a library to your serverless environment if it isn't already provided. Use this for runtime-only libraries you don't want to include. 
Connect to an external database : For JDBC sources, use a JDBC connection instead of including a driver. JDBC connections are Unity Catalog -managed. Credentials, lineage, and governance are handled for you. Provided libraries ​ 
The following libraries are required dependencies and are available by default on serverless compute. Declare them provided in your build. Bundling your own versions of these libraries triggers a NoSuchMethodError at runtime. note 
The library versions listed below are for serverless environment version 4 . For installed libraries for other environment versions, see the serverless environment version notes reference. 
com.databricks:databricks-connect_2.13 , version 17.3.2 
org.scala-lang:scala-library_2.13 , version 2.13.16 
org.scala-lang:scala-reflect_2.13 , version 2.13.16 
org.slf4j:slf4j-api , version 2.0.10 
org.apache.logging.log4j:log4j-api , version 2.20.0 
org.apache.logging.log4j:log4j-core , version 2.20.0 
org.apache.httpcomponents:httpclient , version 4.5.14 
org.apache.httpcomponents:httpcore , version 4.4.16 
com.fasterxml.jackson.core:jackson-databind , version 2.15.2 
com.fasterxml.jackson.core:jackson-core , version 2.15.2 
com.fasterxml.jackson.core:jackson-annotations , version 2.15.2 
com.fasterxml.jackson.datatype:jackson-datatype-jsr310 , version 2.15.2 
com.google.guava:guava , version 32.0.1-jre 
commons-io:commons-io , version 2.14.0 
org.json4s:json4s-jackson_2.13 , version 4.0.7 
org.apache.commons:commons-lang3 , version 3.14.0 
org.apache.commons:commons-configuration2 , version 2.11.0 
org.apache.commons:commons-text , version 1.12.0 
com.databricks:databricks-sdk-java , version 0.52.0 
com.databricks:databricks-dbutils-scala_2.13 , version 0.1.4 
Step 2: Create a job to run the JAR ​ 

In your workspace, click Jobs & Pipelines in the sidebar. 

Click Create , then Job . 

Click the JAR tile to configure the first task. If the JAR tile is not available, click Add another task type and search for JAR . 

Optionally, replace the name of the job, which defaults to New Job <date-time> , with your job name. 

In Task name , enter a name for the task, for example JAR_example . 

If necessary, select JAR from the Type drop-down menu. 

For Main class , enter the package and class of your JAR. If you followed the example earlier, enter com.examples.SparkJar . 

For Compute , select Serverless . 

Configure the serverless environment: 
Select an environment, then click Edit to configure it. 
Select 4 or higher for the Environment version . 
Add your JAR file by dragging and dropping it into the file selector, or browse to select it from a Unity Catalog volume or workspace location. 

For Parameters , for this example, enter ["Hello", "World!"] . 

Click Save task . 
Step 3: Run the job and view the job run details ​ 
Click to run the workflow. To view details for the run , click View run in the Triggered run pop-up or click the link in the Start time column for the run in the job runs view. 
When the run completes, the output appears in the Output pane, including the arguments you passed to the task. 
Troubleshooting ​ 
The following table provides troubleshooting information for common exceptions. 

Exception 
Cause 
Fix 

NoSuchMethodError referencing a scala.* class 
JAR compiled against Scala 2.12; serverless runs Scala 2.13 
Recompile with scalaVersion := "2.13.16" . Ensure every Scala dependency uses the _2.13 cross-version suffix. 

NoClassDefFoundError: scala/... 
Scala 2.12 vs 2.13 mismatch 
Recompile with scalaVersion := "2.13.16" . Ensure every Scala dependency uses the _2.13 cross-version suffix. 

UnsupportedClassVersionError (a class file version higher than 61) 
Compiled with JDK 18 or higher; serverless runs JDK 17 
Use <maven.compiler.release>17</maven.compiler.release> (Maven) or --release 17 (sbt / javac) 

NoClassDefFoundError: org/apache/spark/... for an internal package ( catalyst , util , sql/util , sql/internal , api/java , or rdd ) 
Spark internals or RDD API were used. These are not available on serverless. 
Use the public Spark API (DataFrame/Dataset/SQL). See limitations on serverless . 

ClassNotFoundException for a JDBC driver class (for example, oracle.jdbc.OracleDriver ) 
JDBC driver not on classpath 
Use a JDBC connection for the external database. 

ClassNotFoundException for a third-party class (for example, kotlin.jvm.internal.* ) 
The library is not on the serverless classpath. 
Add it to your JAR, or provide it as an additional JAR using the serverless environment . 

UnsatisfiedLinkError referencing a file under /tmp/ 
Native library included in JAR 
Native libraries are not supported on serverless. Use a pure-Java equivalent, or run on classic compute. 

NoSuchMethodError from a third-party library (Apache Commons, Guava, Jackson, etc.) 
Your included version conflicts with the version provided by serverless . 
Use the provided version. Mark it provided in your build and don't include it in your JAR. ← ✕ 

Exception 
Cause 
Fix 

NoSuchMethodError referencing a scala.* class 
JAR compiled against Scala 2.12; serverless runs Scala 2.13 
Recompile with scalaVersion := "2.13.16" . Ensure every Scala dependency uses the _2.13 cross-version suffix. 

NoClassDefFoundError: scala/... 
Scala 2.12 vs 2.13 mismatch 
Recompile with scalaVersion := "2.13.16" . Ensure every Scala dependency uses the _2.13 cross-version suffix. 

UnsupportedClassVersionError (a class file version higher than 61) 
Compiled with JDK 18 or higher; serverless runs JDK 17 
Use <maven.compiler.release>17</maven.compiler.release> (Maven) or --release 17 (sbt / javac) 

NoClassDefFoundError: org/apache/spark/... for an internal package ( catalyst , util , sql/util , sql/internal , api/java , or rdd ) 
Spark internals or RDD API were used. These are not available on serverless. 
Use the public Spark API (DataFrame/Dataset/SQL). See limitations on serverless . 

ClassNotFoundException for a JDBC driver class (for example, oracle.jdbc.OracleDriver ) 
JDBC driver not on classpath 
Use a JDBC connection for the external database. 

ClassNotFoundException for a third-party class (for example, kotlin.jvm.internal.* ) 
The library is not on the serverless classpath. 
Add it to your JAR, or provide it as an additional JAR using the serverless environment . 

UnsatisfiedLinkError referencing a file under /tmp/ 
Native library included in JAR 
Native libraries are not supported on serverless. Use a pure-Java equivalent, or run on classic compute. 

NoSuchMethodError from a third-party library (Apache Commons, Guava, Jackson, etc.) 
Your included version conflicts with the version provided by serverless . 
Use the provided version. Mark it provided in your build and don't include it in your JAR. 
Next steps ​ 
To learn more about JAR tasks, see JAR task for jobs . 
To learn more about creating a compatible JAR, see Create a Databricks compatible JAR . 
To learn more about creating and running jobs, see Lakeflow Jobs . On this page 
Requirements 
Dependency versions 
Step 1: Build a JAR 
Manage dependencies 
Step 2: Create a job to run the JAR 
Step 3: Run the job and view the job run details 
Troubleshooting 
Next steps Privacy Notice · Terms of Use · Modern Slavery Statement · California Privacy · Your Privacy Choices © Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation . 
# hadoop

Source: https://iceberg.apache.org/javadoc/nightly/org/apache/iceberg/hadoop/HadoopCatalog.html
Retrieved: 2026-10-11

HadoopCatalog JavaScript is disabled on your browser. Skip navigation links 
Overview 
Package 
Class 
Tree 
Deprecated 
Index 
Help 
Summary: 
Nested | 
Field | 
Constr | 
Method 
Detail: 
Field | 
Constr | 
Method SEARCH: Package org.apache.iceberg.hadoop 
Class HadoopCatalog java.lang.Object org.apache.iceberg.BaseMetastoreCatalog org.apache.iceberg.hadoop.HadoopCatalog All Implemented Interfaces: Closeable , AutoCloseable , org.apache.hadoop.conf.Configurable , Catalog , SupportsNamespaces public class HadoopCatalog extends BaseMetastoreCatalog implements SupportsNamespaces , org.apache.hadoop.conf.Configurable HadoopCatalog provides a way to use table names like db.table to work with path-based tables
 under a common location. It uses a specified directory under a specified filesystem as the
 warehouse directory, and organizes multiple levels directories that mapped to the database,
 namespace and the table respectively. The HadoopCatalog takes a location as the warehouse
 directory. When creating a table such as $db.$tbl, it creates $db/$tbl directory under the
 warehouse directory, and put the table metadata into that directory. 
The HadoopCatalog now supports Catalog.createTable(org.apache.iceberg.catalog.TableIdentifier, org.apache.iceberg.Schema, org.apache.iceberg.PartitionSpec, java.lang.String, java.util.Map<java.lang.String, java.lang.String>) , Catalog.dropTable(org.apache.iceberg.catalog.TableIdentifier) , the Catalog.renameTable(org.apache.iceberg.catalog.TableIdentifier, org.apache.iceberg.catalog.TableIdentifier) is not supported yet. 
Note: The HadoopCatalog requires that the underlying file system supports atomic rename. 

Nested Class Summary 
Nested classes/interfaces inherited from class org.apache.iceberg. BaseMetastoreCatalog BaseMetastoreCatalog.BaseMetastoreCatalogTableBuilder 
Nested classes/interfaces inherited from interface org.apache.iceberg.catalog. Catalog Catalog.TableBuilder 

Constructor Summary Constructors Constructor Description HadoopCatalog () HadoopCatalog (org.apache.hadoop.conf.Configuration conf, String warehouseLocation) The constructor of the HadoopCatalog. 

Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method Description Catalog.TableBuilder buildTable ( TableIdentifier identifier, Schema schema) Instantiate a builder to either create a table or start a create/replace transaction. void close () void createNamespace ( Namespace namespace, Map < String , String > meta) Create a namespace in the catalog. protected String defaultWarehouseLocation ( TableIdentifier tableIdentifier) boolean dropNamespace ( Namespace namespace) Drop a namespace. boolean dropTable ( TableIdentifier identifier,
 boolean purge) Drop a table; optionally delete data and metadata files. org.apache.hadoop.conf.Configuration getConf () void initialize ( String name, Map < String , String > properties) Initialize a catalog given a custom name and a map of catalog properties. protected boolean isValidIdentifier ( TableIdentifier identifier) List < Namespace > listNamespaces ( Namespace namespace) List child namespaces from the namespace. List < TableIdentifier > listTables ( Namespace namespace) Return all the identifiers under this namespace. Map < String , String > loadNamespaceMetadata ( Namespace namespace) Load metadata properties for a namespace. String name () Return the name for this catalog. protected TableOperations newTableOps ( TableIdentifier identifier) protected Map < String , String > properties () boolean removeProperties ( Namespace namespace, Set < String > properties) Remove a set of property keys from a namespace in the catalog. void renameTable ( TableIdentifier from, TableIdentifier to) Rename a table. void setConf (org.apache.hadoop.conf.Configuration conf) boolean setProperties ( Namespace namespace, Map < String , String > properties) Set a collection of properties on a namespace in the catalog. String toString () 
Methods inherited from class org.apache.iceberg. BaseMetastoreCatalog fullTableName , isValidMetadataIdentifier , loadTable , metricsReporter , registerTable 
Methods inherited from class java.lang. Object clone , equals , finalize , getClass , hashCode , notify , notifyAll , wait , wait , wait 
Methods inherited from interface org.apache.iceberg.catalog. Catalog createTable , createTable , createTable , createTable , dropTable , invalidateTable , loadTable , newCreateTableTransaction , newCreateTableTransaction , newCreateTableTransaction , newCreateTableTransaction , newReplaceTableTransaction , newReplaceTableTransaction , newReplaceTableTransaction , newReplaceTableTransaction , registerTable , tableExists 
Methods inherited from interface org.apache.iceberg.catalog. SupportsNamespaces createNamespace , listNamespaces , namespaceExists 

Constructor Details 

HadoopCatalog public HadoopCatalog () 

HadoopCatalog public HadoopCatalog (org.apache.hadoop.conf.Configuration conf, String warehouseLocation) The constructor of the HadoopCatalog. It uses the passed location as its warehouse directory. Parameters: conf - The Hadoop configuration warehouseLocation - The location used as warehouse directory 

Method Details 

initialize public void initialize ( String name, Map < String , String > properties) Description copied from interface: Catalog Initialize a catalog given a custom name and a map of catalog properties. 
A custom Catalog implementation must have a no-arg constructor. A compute engine like Spark
 or Flink will first initialize the catalog without any arguments, and then call this method to
 complete catalog initialization with properties passed into the engine. Specified by: initialize in interface Catalog Parameters: name - a custom name for the catalog properties - catalog properties 

name public String name () Description copied from interface: Catalog Return the name for this catalog. Specified by: name in interface Catalog Returns: this catalog's name 

listTables public List < TableIdentifier > listTables ( Namespace namespace) Description copied from interface: Catalog Return all the identifiers under this namespace. Specified by: listTables in interface Catalog Parameters: namespace - a namespace Returns: a list of identifiers for tables 

isValidIdentifier protected boolean isValidIdentifier ( TableIdentifier identifier) Overrides: isValidIdentifier in class BaseMetastoreCatalog 

newTableOps protected TableOperations newTableOps ( TableIdentifier identifier) Specified by: newTableOps in class BaseMetastoreCatalog 

defaultWarehouseLocation protected String defaultWarehouseLocation ( TableIdentifier tableIdentifier) Specified by: defaultWarehouseLocation in class BaseMetastoreCatalog 

dropTable public boolean dropTable ( TableIdentifier identifier,
 boolean purge) Description copied from interface: Catalog Drop a table; optionally delete data and metadata files. 
If purge is set to true the implementation should delete all data and metadata files. Specified by: dropTable in interface Catalog Parameters: identifier - a table identifier purge - if true, delete all data and metadata files in the table Returns: true if the table was dropped, false if the table did not exist 

renameTable public void renameTable ( TableIdentifier from, TableIdentifier to) Description copied from interface: Catalog Rename a table. Specified by: renameTable in interface Catalog Parameters: from - identifier of the table to rename to - new table name 

createNamespace public void createNamespace ( Namespace namespace, Map < String , String > meta) Description copied from interface: SupportsNamespaces Create a namespace in the catalog. Specified by: createNamespace in interface SupportsNamespaces Parameters: namespace - a multi-part namespace meta - a string Map of properties for the given namespace 

listNamespaces public List < Namespace > listNamespaces ( Namespace namespace) Description copied from interface: SupportsNamespaces List child namespaces from the namespace. 
For two existing tables named 'a.b.c.table' and 'a.b.d.table', this method returns: 
Given: Namespace.empty() 
Returns: Namespace.of("a") 
Given: Namespace.of("a") 
Returns: Namespace.of("a", "b") 
Given: Namespace.of("a", "b") 
Returns: Namespace.of("a", "b", "c") and Namespace.of("a", "b", "d") 
Given: Namespace.of("a", "b", "c") 
Returns: empty list, because there are no child namespaces Specified by: listNamespaces in interface SupportsNamespaces Returns: a List of child Namespace names from the given namespace 

dropNamespace public boolean dropNamespace ( Namespace namespace) Description copied from interface: SupportsNamespaces Drop a namespace. If the namespace exists and was dropped, this will return true. Specified by: dropNamespace in interface SupportsNamespaces Parameters: namespace - a namespace. Namespace Returns: true if the namespace was dropped, false otherwise. 

setProperties public boolean setProperties ( Namespace namespace, Map < String , String > properties) Description copied from interface: SupportsNamespaces Set a collection of properties on a namespace in the catalog. 
Properties that are not in the given map are not modified or removed by this method. Specified by: setProperties in interface SupportsNamespaces Parameters: namespace - a namespace. Namespace properties - a collection of metadata to apply to the namespace Returns: true if the properties were successfully set, false otherwise 

removeProperties public boolean removeProperties ( Namespace namespace, Set < String > properties) Description copied from interface: SupportsNamespaces Remove a set of property keys from a namespace in the catalog. 
Properties that are not in the given set are not modified or removed by this method. Specified by: removeProperties in interface SupportsNamespaces Parameters: namespace - a namespace. Namespace properties - a collection of metadata to apply to the namespace Returns: true if the properties were successfully removed, false otherwise 

loadNamespaceMetadata public Map < String , String > loadNamespaceMetadata ( Namespace namespace) Description copied from interface: SupportsNamespaces Load metadata properties for a namespace. Specified by: loadNamespaceMetadata in interface SupportsNamespaces Parameters: namespace - a namespace. Namespace Returns: a string map of properties for the given namespace 

close public void close ()
           throws IOException Specified by: close in interface AutoCloseable Specified by: close in interface Closeable Overrides: close in class BaseMetastoreCatalog Throws: IOException 

toString public String toString () Overrides: toString in class BaseMetastoreCatalog 

buildTable public Catalog.TableBuilder buildTable ( TableIdentifier identifier, Schema schema) Description copied from interface: Catalog Instantiate a builder to either create a table or start a create/replace transaction. Specified by: buildTable in interface Catalog Overrides: buildTable in class BaseMetastoreCatalog Parameters: identifier - a table identifier schema - a schema Returns: the builder to create a table or start a create/replace transaction 

setConf public void setConf (org.apache.hadoop.conf.Configuration conf) Specified by: setConf in interface org.apache.hadoop.conf.Configurable 

getConf public org.apache.hadoop.conf.Configuration getConf () Specified by: getConf in interface org.apache.hadoop.conf.Configurable 

properties protected Map < String , String > properties () Overrides: properties in class BaseMetastoreCatalog 
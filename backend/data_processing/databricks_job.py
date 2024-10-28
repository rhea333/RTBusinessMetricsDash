from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum

# Initialize Spark session
spark = SparkSession.builder.appName("SalesDataProcessing").getOrCreate()

# Load raw sales data (assuming it's stored in a Databricks dataset)
raw_data = spark.read.csv("/path/to/sales_data.csv", header=True, inferSchema=True)

# Perform transformations
clean_data = raw_data.filter(col("sales").isNotNull()) \
                     .groupBy("region", "product") \
                     .agg(sum("sales").alias("total_sales"))

# Save processed data to Databricks or a database
clean_data.write.mode("overwrite").format("parquet").save("/path/to/processed_sales_data")

spark.stop()

# 1. Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# 2. Start a Spark session
spark = SparkSession.builder \
    .appName("PySpark Sample") \
    .getOrCreate()

# 3. Create sample data
data = [
    ("Alice", 34),
    ("Bob", 45),
    ("Cathy", 29),
    ("David", 40)
]
columns = ["Name", "Age"]

# 4. Create DataFrame
df = spark.createDataFrame(data, columns)

# 5. Show the DataFrame
df.show()

# 6. Filter: Find people older than 30
df_filtered = df.filter(col("Age") > 30)
df_filtered.show()

# 7. Group and Aggregate (average age)
df_agg = df.groupBy().avg("Age")
df_agg.show()

# 8. Stop the Spark session
spark.stop()

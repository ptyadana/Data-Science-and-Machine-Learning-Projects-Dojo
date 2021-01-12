-- Databricks notebook source
-- DBTITLE 1,Sales per Region Bar Chart
/* Sales per Region Bar Chart */
SELECT *
FROM cogsley_sales
limit 100;

-- COMMAND ----------

-- DBTITLE 1,Sales per Region Bar Chart for each sector
/* Sales per Region Bar Chart for each sector */
SELECT *
FROM cogsley_sales
limit 100;

-- COMMAND ----------

/* Sales timesries by region Line Chart */
SELECT *
FROM cogsley_sales
limit 100;

-- COMMAND ----------

-- DBTITLE 1,Build a Map
/* requires 2char state code */
/* Sales per Sates */
SELECT si.StateCode, ROUND(sum(cs.SaleAmount)) AS Sales
FROM cogsley_sales cs
JOIN state_info si ON cs.State = si.State
GROUP BY si.StateCode

-- COMMAND ----------

-- DBTITLE 1,Box Plot (bonus!)
/* Box Plot - Sales per Product Category */

SELECT *
FROM cogsley_sales
LIMIT 100;

-- COMMAND ----------



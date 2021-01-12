-- Databricks notebook source
-- DBTITLE 1,Take a look at our sale table
/* get top 100 rows */
SELECT *
FROM cogsley_sales
LIMIT 100;

-- COMMAND ----------

-- DBTITLE 1,Calculate Sales Totals
/* Calculate Sales Totals per Company */

SELECT CompanyName, ROUND(SUM(SaleAmount)) AS Sales 
FROM cogsley_sales
GROUP BY CompanyName
ORDER BY 2 DESC;

-- COMMAND ----------

SELECT * FROM cogsley_clients
LIMIT 2;

-- COMMAND ----------

SELECT * FROM cogsley_sales
LIMIT 2;

-- COMMAND ----------

-- DBTITLE 1,Join to get Client Info
/* Join to get Client Info */

SELECT CompanyName, IPOYear, Symbol, ROUND(SUM(SaleAmount)) AS Sales
FROM cogsley_sales
LEFT JOIN cogsley_clients
ON CompanyName = Name
GROUP BY CompanyName, IPOYear, Symbol 
ORDER BY 1;

-- COMMAND ----------

SELECT * FROM state_info
LIMIT 2;

-- COMMAND ----------

-- DBTITLE 1,Join to get State Info
/* Join to get State Info */
/* Sales by State */

SELECT si.StateCode, cs.State, ROUND(SUM(cs.SaleAmount)) AS Total
FROM cogsley_sales cs
LEFT JOIN state_info si
ON cs.State = si.State
GROUP BY si.StateCode, cs.State
ORDER BY 1;


-- COMMAND ----------



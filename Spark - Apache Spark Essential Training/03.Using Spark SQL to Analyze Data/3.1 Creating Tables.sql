-- Databricks notebook source
-- DBTITLE 1,Find a CSV
-- MAGIC %fs ls /databricks-datasets/samples/population-vs-price/

-- COMMAND ----------

-- DBTITLE 1,Create Table w/o Schema
/* Create Table w/o Schema */
CREATE TABLE IF NOT EXISTS population_v_price
USING CSV
OPTIONS (path='/databricks-datasets/samples/population-vs-price/data_geo.csv', header=True, inferSchema=True);

-- COMMAND ----------

SELECT *
FROM population_v_price
LIMIT 10;

-- COMMAND ----------

-- DBTITLE 1,Create Table w/ Schema
/* Create Table w/ Schema */
/* we will define schema explictly unlike above directly using from CSV */
CREATE TABLE IF NOT EXISTS online_retail(
InvoiceNo string,
StockCode string,
Description string,
Quantity int,
InvoiceDate string,
UnitPrice double,
CustomerID int,
Country string)
USING CSV
OPTIONS (path='/databricks-datasets/online_retail/data-001/data.csv', header=True);

-- COMMAND ----------

SELECT * FROM online_retail
LIMIT 10;

-- COMMAND ----------



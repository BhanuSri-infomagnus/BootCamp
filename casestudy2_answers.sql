SELECT * from regions;

SELECT * from customer_nodes;

SELECT * from customer_transactions;


  /* --------------------
   Case Study Questions
   --------------------*/
-- How many unique nodes are there on the Data Bank system?

SELECT COUNT(distinct node_id) as unique_nodes 
from customer_nodes;

-- What is the number of nodes per region?
 
SELECT region_id, COUNT( node_id) as nodes_per_region
from customer_nodes
GROUP BY region_id order by region_id;

-- How many customers are allocated to each region?

SELECT region_id, COUNT( customer_id) as customers_per_region
from customer_nodes
GROUP BY region_id order by region_id;

-- How many days on average are customers reallocated to a different node?



-- What is the unique count and total amount for each transaction type?

SELECT txn_type, COUNT( DISTINCT txn_amount) 
as unique_count, SUM( txn_amount) as total_amount
from customer_transactions 
GROUP BY txn_type order by txn_type;


-- For each month - how many Data Bank customers make more than 1 deposit and either 1 purchase or 1 withdrawal in a single month?



-- What is the closing balance for each customer at the end of the month?







--CASE STUDY   

SELECT * FROM sales;
SELECT * FROM menu;
SELECT * FROM members;

--1. What is the total amount each customer spent at the restaurant?

SELECT customer_id,sum(m.price)as total_amount FROM sales as s 
INNER JOIN menu AS m ON s.product_id=m.product_id group by customer_id;

--2. How many days has each customer visited the restaurant?

SELECT customer_id,count(distinct order_date) as days_visited from sales group by customer_id;

--3. What was the first item from the menu purchased by each customer?
SELECT distinct s.customer_id,m.product_name from sales as s
inner join menu as m 
on s.product_id=m.product_id 
where s.order_date=
(select min(s2.order_date) from sales s2 where s.customer_id=s2.customer_id);

--4. What is the most purchased item on the menu and how many times was it purchased by all customers?

select top 1  m.product_name,count(s.product_id) from sales as s inner join menu as m 
on s.product_id=m.product_id group by product_name order by COUNT(s.product_id) desc;

--5. Which item was the most popular for each customer?

select customer_id,product_id
from
(SELECT   customer_id,product_id,RANK()
over(PARTITION by customer_id order by count(product_id) desc) as most_popular
 from sales
group by customer_id,product_id) ranked
where most_popular=1;

--6. Which item was purchased first by the customer after they became a member?

SELECT customer_id,product_id
from
(SELECT s.customer_id,s.product_id,RANK() 
over(PARTITION by s.customer_id ORDER by s.order_date) as Rnk
from sales as s 
inner join members as m
on s.customer_id=m.customer_id
where s.order_date>m.join_date)
 ranked where Rnk=1;

--7. Which item was purchased just before the customer became a member?


SELECT customer_id,product_id
from
(SELECT s.customer_id,s.product_id,ROW_NUMBER() 
over(PARTITION by s.customer_id ORDER by s.order_date desc) as Rnk
from sales as s 
inner join members as m
on s.customer_id=m.customer_id
where s.order_date<m.join_date)
 ranked where Rnk=1;

-- 8. What is the total items and amount spent for each member before they became a member?
 
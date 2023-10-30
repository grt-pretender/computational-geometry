# 1757. Recyclable and Low Fat Products
# Write a solution to find the ids of products that are both low fat and recyclable
# Write your MySQL query statement below

SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y'

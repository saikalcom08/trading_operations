SELECT prices.price * operations.quantity
FROM main_operation as operations
INNER JOIN main_product as products
    ON operations.product_id = products.id
INNER JOIN (
    SELECT *
    FROM main_pricehistory as prices
    WHERE prices.date_to IS NULL
    ORDER BY id
    LIMIT 1
) as prices
    ON prices.product_id = products.id;

CREATE TABLE user_activity (
    user_id INT,
    login_count INT,
    avg_session_time FLOAT,
    purchase_amount FLOAT,
    click_count FLOAT,
    activity_date DATE
);

SELECT user_id,
       AVG(login_count) AS avg_logins,
       AVG(avg_session_time) AS avg_time,
       SUM(purchase_amount) AS total_purchase,
       AVG(click_count) AS avg_clicks
FROM user_activity
GROUP BY user_id;
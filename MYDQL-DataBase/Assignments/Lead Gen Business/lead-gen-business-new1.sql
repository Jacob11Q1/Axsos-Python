DROP DATABASE IF EXISTS lead_gen_business_new;
CREATE DATABASE lead_gen_business_new;
USE lead_gen_business_new;

-- 1. Clients table
CREATE TABLE clients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

-- 2. Sites table
CREATE TABLE sites (
    id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT,
    domain_name VARCHAR(100),
    created_at DATE,
    FOREIGN KEY (client_id) REFERENCES clients(id)
);

-- 3. Leads table
CREATE TABLE leads (
    id INT AUTO_INCREMENT PRIMARY KEY,
    site_id INT,
    registered_datetime DATETIME,
    FOREIGN KEY (site_id) REFERENCES sites(id)
);

-- 4. Billing table
CREATE TABLE billing (
    id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT,
    amount DECIMAL(10,2),
    charged_datetime DATE,
    FOREIGN KEY (client_id) REFERENCES clients(id)
);

-- =======================
-- QUERIES
-- =======================

-- 1. Total revenue for March 2012
SELECT SUM(amount) AS total_revenue
FROM billing
WHERE YEAR(charged_datetime) = 2012
AND MONTH(charged_datetime) = 3;

-- 2. Total revenue from client with ID 2
SELECT SUM(amount) AS total_revenue
FROM billing
WHERE client_id = 2;

-- 3. All sites owned by client with ID 10
SELECT domain_name
FROM sites
WHERE client_id = 10;

-- 4. Total number of monthly sites created per year for client ID 1
SELECT YEAR(created_at) AS year_created,
MONTH(created_at) AS month_created,
COUNT(id) AS total_sites
FROM sites
WHERE client_id = 1
GROUP BY YEAR(created_at), MONTH(created_at)
ORDER BY year_created, month_created;

-- 5. Total number of leads generated for each site between Jan 1 2011 and Feb 15 2011
SELECT site_id, COUNT(id) AS total_leads
FROM leads
WHERE registered_datetime >= '2011-01-01'
AND registered_datetime < '2011-02-15'
GROUP BY site_id;

-- 6. Client names and total leads per client between Jan 1 2011 and Dec 31 2011
SELECT clients.first_name, clients.last_name,
COUNT(leads.id) AS total_leads
FROM clients
JOIN sites ON clients.id = sites.client_id
JOIN leads ON sites.id = leads.site_id
WHERE leads.registered_datetime >= '2011-01-01'
AND leads.registered_datetime <= '2011-12-31'
GROUP BY clients.id;

-- 7. Client names and total leads per client each month between Jan–Jun 2011
SELECT clients.first_name, clients.last_name,
YEAR(leads.registered_datetime) AS year_registered,
MONTH(leads.registered_datetime) AS month_registered,
COUNT(leads.id) AS total_leads
FROM clients
JOIN sites ON clients.id = sites.client_id
JOIN leads ON sites.id = leads.site_id
WHERE YEAR(leads.registered_datetime) = 2011
AND MONTH(leads.registered_datetime) BETWEEN 1 AND 6
GROUP BY clients.id, YEAR(leads.registered_datetime), MONTH(leads.registered_datetime)
ORDER BY clients.id, month_registered;

-- 8. Client names and total leads per site between Jan 1 2011 and Dec 31 2011
SELECT clients.id AS client_id, clients.first_name, clients.last_name,
sites.domain_name, COUNT(leads.id) AS total_leads
FROM clients
JOIN sites ON clients.id = sites.client_id
JOIN leads ON sites.id = leads.site_id
WHERE leads.registered_datetime >= '2011-01-01'
AND leads.registered_datetime <= '2011-12-31'
GROUP BY sites.id
ORDER BY clients.id;
-- Query 1: Top 5 Funds by AUM
SELECT
    scheme_name,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Query 2: Average NAV
SELECT
    ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav;

-- Query 3: Transactions volume by State
SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- Query 4: Funds with Expense Ratio less than 1%
SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- Query 5: SIP Inflow YoY Growth
SELECT
    strftime('%Y', month) AS year,
    ROUND(AVG(yoy_growth_pct),2) AS avg_yoy_growth_pct
FROM fact_sip_inflows
WHERE yoy_growth_pct IS NOT NULL
GROUP BY year
ORDER BY year;

-- Query 6: Top 5 Funds by 1-Year Return
SELECT
    scheme_name,
    return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- Query 7: Highest Sharpe Ratio Funds
SELECT
    scheme_name,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- Query 8: Category with Highest Inflows
SELECT
    category,
    ROUND(SUM(net_inflow_crore),2) AS total_inflow
FROM fact_category_inflows
GROUP BY category
ORDER BY total_inflow DESC;

-- Query 9: Top Sectors by Portfolio Weight
SELECT
    sector,
    ROUND(SUM(weight_pct),2) AS total_weight
FROM fact_portfolio_holdings
GROUP BY sector
ORDER BY total_weight DESC
LIMIT 5;

-- Query 10: Average Transaction Amount by Type
SELECT
    transaction_type,
    ROUND(AVG(amount_inr),2) AS avg_amount
FROM fact_transactions
GROUP BY transaction_type;
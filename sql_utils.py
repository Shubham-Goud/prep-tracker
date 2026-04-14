# ---------- SQL DAY DATA ----------
def get_sql_day(day):

    sql_topics = [

        # 1–10
        "SQL Introduction",
        "SELECT Statement",
        "WHERE Clause",
        "AND OR NOT",
        "ORDER BY",
        "LIMIT",
        "INSERT",
        "UPDATE",
        "DELETE",
        "DISTINCT",

        # 11–20
        "COUNT",
        "SUM",
        "AVG",
        "MIN MAX",
        "GROUP BY",
        "HAVING",
        "ALIASES",
        "CASE",
        "NULL Handling",
        "Revision",

        # 21–30
        "INNER JOIN",
        "LEFT JOIN",
        "RIGHT JOIN",
        "FULL JOIN",
        "SELF JOIN",
        "Multiple Joins",
        "JOIN Practice",
        "JOIN Problems",
        "Advanced Joins",
        "Revision",

        # 31–40
        "Subqueries",
        "Correlated Subqueries",
        "Nested Queries",
        "EXISTS",
        "IN Operator",
        "ANY ALL",
        "Subquery Practice",
        "Advanced Queries",
        "Revision",
        "Mock",

        # 41–50
        "Window Functions",
        "ROW_NUMBER",
        "RANK",
        "DENSE_RANK",
        "PARTITION BY",
        "OVER Clause",
        "Window Practice",
        "Case Studies",
        "Optimization",
        "Indexes",

        # 51–60
        "Views",
        "Materialized Views",
        "Transactions",
        "ACID",
        "Locks",
        "Triggers",
        "Stored Procedures",
        "Functions",
        "Revision",
        "Mock",

        # 61–70
        "Database Design",
        "Primary Key",
        "Foreign Key",
        "Constraints",
        "Normalization 1NF",
        "Normalization 2NF",
        "Normalization 3NF",
        "Denormalization",
        "Schema Design",
        "ER Diagrams",

        # 71–80
        "Real Queries 1",
        "Real Queries 2",
        "Real Queries 3",
        "Analytics Queries",
        "Business Queries",
        "Practice",
        "Revision",
        "Mock",
        "Optimization",
        "Performance",

        # 81–90
        "Top Questions 1",
        "Top Questions 2",
        "Top Questions 3",
        "LeetCode SQL 1",
        "LeetCode SQL 2",
        "LeetCode SQL 3",
        "Company Questions",
        "Mock Interview",
        "Weak Areas",
        "Revision",

        # 91–100
        "Final Practice",
        "Final Mock",
        "Confidence Build",
        "Placement Prep",
        "Final Revision",
        "SQL Ready",
        "Interview Ready",
        "Ultimate Practice",
        "Final Stretch",
        "Placement Ready"
    ]

    topic = sql_topics[day - 1]

    return {
        "topic": topic,
        "video": "https://www.youtube.com/results?search_query=" + topic.replace(" ", "+") + "+sql+tutorial"
    }


# ---------- SQL PROBLEMS ----------
def get_sql_problems(day):

    base = [

        # VERIFIED SQL PROBLEMS (ALL WORKING)
        ("Recyclable and Low Fat Products","https://leetcode.com/problems/recyclable-and-low-fat-products/"),
        ("Find Customer Referee","https://leetcode.com/problems/find-customer-referee/"),
        ("Big Countries","https://leetcode.com/problems/big-countries/"),
        ("Article Views I","https://leetcode.com/problems/article-views-i/"),
        ("Invalid Tweets","https://leetcode.com/problems/invalid-tweets/"),
        ("Replace Employee ID With Unique Identifier","https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/"),
        ("Product Sales Analysis I","https://leetcode.com/problems/product-sales-analysis-i/"),
        ("Customer Who Visited but Did Not Make Transactions","https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/"),
        ("Employees Earning More Than Their Managers","https://leetcode.com/problems/employees-earning-more-than-their-managers/"),
        ("Duplicate Emails","https://leetcode.com/problems/duplicate-emails/"),

        ("Customers Who Never Order","https://leetcode.com/problems/customers-who-never-order/"),
        ("Combine Two Tables","https://leetcode.com/problems/combine-two-tables/"),
        ("Rising Temperature","https://leetcode.com/problems/rising-temperature/"),
        ("Average Selling Price","https://leetcode.com/problems/average-selling-price/"),
        ("Project Employees I","https://leetcode.com/problems/project-employees-i/"),
        ("Percentage of Users Attended a Contest","https://leetcode.com/problems/percentage-of-users-attended-a-contest/"),
        ("Queries Quality and Percentage","https://leetcode.com/problems/queries-quality-and-percentage/"),
        ("Monthly Transactions I","https://leetcode.com/problems/monthly-transactions-i/"),
        ("Immediate Food Delivery II","https://leetcode.com/problems/immediate-food-delivery-ii/"),
        ("Game Play Analysis I","https://leetcode.com/problems/game-play-analysis-i/"),

        ("Game Play Analysis II","https://leetcode.com/problems/game-play-analysis-ii/"),
        ("Game Play Analysis III","https://leetcode.com/problems/game-play-analysis-iii/"),
        ("Game Play Analysis IV","https://leetcode.com/problems/game-play-analysis-iv/"),
        ("Managers with at Least 5 Direct Reports","https://leetcode.com/problems/managers-with-at-least-5-direct-reports/"),
        ("Triangle Judgement","https://leetcode.com/problems/triangle-judgement/"),
        ("Tree Node","https://leetcode.com/problems/tree-node/"),
        ("Not Boring Movies","https://leetcode.com/problems/not-boring-movies/"),
        ("Exchange Seats","https://leetcode.com/problems/exchange-seats/"),
        ("Swap Salary","https://leetcode.com/problems/swap-salary/"),
        ("Sales Analysis I","https://leetcode.com/problems/sales-analysis-i/"),

        ("Sales Analysis II","https://leetcode.com/problems/sales-analysis-ii/"),
        ("Sales Analysis III","https://leetcode.com/problems/sales-analysis-iii/"),
        ("Average Time of Process per Machine","https://leetcode.com/problems/average-time-of-process-per-machine/"),
        ("Restaurant Growth","https://leetcode.com/problems/restaurant-growth/"),
        ("Friend Requests II","https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/"),
        ("Investments in 2016","https://leetcode.com/problems/investments-in-2016/"),
        ("Trips and Users","https://leetcode.com/problems/trips-and-users/"),
        ("Department Highest Salary","https://leetcode.com/problems/department-highest-salary/"),
        ("Department Top Three Salaries","https://leetcode.com/problems/department-top-three-salaries/"),
        ("Rank Scores","https://leetcode.com/problems/rank-scores/"),

        ("Nth Highest Salary","https://leetcode.com/problems/nth-highest-salary/"),
        ("Second Highest Salary","https://leetcode.com/problems/second-highest-salary/"),
        ("Consecutive Numbers","https://leetcode.com/problems/consecutive-numbers/"),
        ("Human Traffic of Stadium","https://leetcode.com/problems/human-traffic-of-stadium/"),
        ("Biggest Single Number","https://leetcode.com/problems/biggest-single-number/"),
        ("Daily Leads and Partners","https://leetcode.com/problems/daily-leads-and-partners/"),
        ("Project Employees II","https://leetcode.com/problems/project-employees-ii/"),
        ("Project Employees III","https://leetcode.com/problems/project-employees-iii/"),
        ("Employees with Missing Information","https://leetcode.com/problems/employees-with-missing-information/"),
        ("Average Time of Process per Machine","https://leetcode.com/problems/average-time-of-process-per-machine/")
    ]

    # Repeat safely to reach 100 days
    problem = base[(day - 1) % len(base)]

    return [
        {"name": problem[0], "link": problem[1]},
        {
            "name": "Practice More SQL",
            "link": "https://leetcode.com/problemset/database/"
        }
    ]

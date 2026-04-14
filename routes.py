from flask import render_template, request, redirect
import sqlite3

# existing imports
from utils import get_day_data, get_leetcode_problems

# SQL
from sql_utils import get_sql_day, get_sql_problems


def register_routes(app):

    # ---------------- HOME ----------------
    @app.route("/")
    def index():

        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        c.execute("SELECT day FROM progress WHERE completed=1")
        completed = [row[0] for row in c.fetchall()]

        done = len(completed)
        percent = int((done / 100) * 100) if done else 0

        c.execute("SELECT current_streak FROM streak")
        result = c.fetchone()
        streak = result[0] if result else 0

        conn.close()

        return render_template("index.html", percent=percent, streak=streak, done=done)


    # ---------------- DASHBOARD ----------------
    @app.route("/dashboard")
    def dashboard():

        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        c.execute("SELECT day FROM progress WHERE completed=1")
        completed = [row[0] for row in c.fetchall()]

        c.execute("SELECT current_streak FROM streak")
        result = c.fetchone()
        streak = result[0] if result else 0

        conn.close()

        percent = int((len(completed) / 100) * 100)

        days = []
        for d in range(1, 101):
            days.append({
                "day": d,
                "done": d in completed
            })

        return render_template("dashboard.html", days=days, percent=percent, streak=streak)


    # ---------------- DAY PAGE ----------------
    @app.route("/day/<int:day>")
    def day_page(day):

        data = get_day_data(day)
        problems = get_leetcode_problems(day)

        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        c.execute("SELECT content FROM notes WHERE day=?", (day,))
        note = c.fetchone()

        conn.close()

        return render_template(
            "day.html",
            day=day,
            dsa=data["dsa"],
            python=data["python"],
            java=data["java"],   # ✅ FIXED HERE
            problems=problems,
            note=note
        )


    # ---------------- SAVE NOTE ----------------
    @app.route("/save_note", methods=["POST"])
    def save_note():

        day = request.form["day"]
        content = request.form["content"]

        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        c.execute("DELETE FROM notes WHERE day=?", (day,))
        c.execute("INSERT INTO notes (day, content) VALUES (?, ?)", (day, content))

        conn.commit()
        conn.close()

        return redirect(f"/day/{day}")


    # ---------------- MARK DONE ----------------
    @app.route("/mark_done/<int:day>")
    def mark_done(day):

        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        c.execute("INSERT OR IGNORE INTO progress (day, completed) VALUES (?, ?)", (day, 1))
        c.execute("UPDATE progress SET completed=1 WHERE day=?", (day,))

        # streak calculation
        c.execute("SELECT day FROM progress ORDER BY day")
        days = [row[0] for row in c.fetchall()]

        streak = 0
        expected = 1

        for d in days:
            if d == expected:
                streak += 1
                expected += 1
            else:
                break

        c.execute("DELETE FROM streak")
        c.execute("INSERT INTO streak VALUES (?, ?)", (1, streak))

        conn.commit()
        conn.close()

        return redirect("/dashboard")


    # ---------------- SQL DASHBOARD ----------------
    @app.route("/sql")
    def sql_dashboard():
        return render_template("sql.html", days=range(1, 101))


    # ---------------- SQL DAY ----------------
    @app.route("/sql/day/<int:day>")
    def sql_day_page(day):

        data = get_sql_day(day)
        problems = get_sql_problems(day)

        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        c.execute("SELECT problem_name FROM solved_problems WHERE day=?", (day,))
        solved = [row[0] for row in c.fetchall()]

        conn.close()

        return render_template(
            "sql_day.html",
            day=day,
            sql=data,
            problems=problems,
            solved=solved
        )


    # ---------------- MARK SOLVED ----------------
    @app.route("/mark_solved", methods=["POST"])
    def mark_solved():

        day = request.form["day"]
        name = request.form["name"]

        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        c.execute(
            "INSERT INTO solved_problems (day, problem_name) VALUES (?, ?)",
            (day, name)
        )

        conn.commit()
        conn.close()

        return redirect(f"/sql/day/{day}")
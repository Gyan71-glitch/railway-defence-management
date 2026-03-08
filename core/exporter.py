import sqlite3
import csv
import os


def export_alerts_to_csv(
    db_name="railway_alerts.db",
    output_file="railway_alerts.csv"
):
    # Check database exists
    if not os.path.exists(db_name):
        print("❌ Database not found:", db_name)
        return

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alerts")
    rows = cursor.fetchall()

    if not rows:
        print("⚠️ No alerts found in database")
        conn.close()
        return

    with open(output_file, "w", newline="") as file:
        writer = csv.writer(file)

        # CSV header
        writer.writerow([
            "ID",
            "Time",
            "Severity",
            "Action",
            "Source",
            "Status"
        ])

        # CSV data
        writer.writerows(rows)

    conn.close()
    print(f"✅ Alerts exported successfully to '{output_file}'")


# Sales Trend Visualization

##  Internship Details

| Field | Details |
|-------|---------|
| **Intern ID** | CITS2445 |
| **Full Name** | Shreenithi Nallamuthu |
| **No. of Weeks** | 4 Weeks |
| **Project Name** | Sales Trend Visualization |
| **Project Scope** | A sales trend visualization project in Python involves building dynamic dashboards or automated reports to analyze historical sales data, track KPIs (like day-over-day growth, week-over-week growth, month-over-month growth, year-over-year growth), and forecast future revenue. It transforms raw sales figures into actionable business intelligence. |

---


Advanced Sales Trend Reporter

A Python-based Weekly Sales Analysis Tool that collects daily sales data, generates summary statistics, saves the data as a CSV file, and visualizes sales trends using both line charts and bar charts.



 Features:
 
 Collects sales data for all seven days of the week.

 Input validation to prevent invalid entries.
 
 Automatically saves data to weekly_sales.csv.
 
 Generates a Line Chart showing weekly sales trends.
 
 Generates a Bar Chart for daily sales comparison.



 Displays:

Total weekly sales

Average daily sales

Highest sales day

Lowest sales day

 
 Shows sales values directly on charts:

🇮🇳 Supports Indian Rupee (₹) formatting.



Technologies Used:

Python 3

Pandas – Data analysis and CSV handling

Matplotlib – Data visualization

OS Module – File path handling



 Project Structure:

Advanced-Sales-Trend-Reporter/
│
├── sales_report.py        # Main program
├── weekly_sales.csv       # Generated sales data
├── README.md
└── screenshots/
     ├── line_chart.png
     ├── bar_chart.png



Run the script:

python sales_report.py



Enter daily sales values when prompted:

Enter sales for Monday (₹): 5000

Enter sales for Tuesday (₹): 3200

Enter sales for Wednesday (₹): 4500
...



The program will:

Store your data.

Calculate weekly statistics.



Save data to:

Desktop/weekly_sales.csv



Display two charts:

 Weekly Sales Trend (Line Chart)

 Daily Sales Comparison (Bar Chart)



Example Visualization:-

Line Chart:

Displays weekly sales trends.

Highlights each day's sales value.

Bar Chart:

Compares sales across days.

Displays sales amount above each bar.


The program validates user input:

try:
    amount = float(user_input)
except ValueError:
    print("❌ Invalid input. Please enter a valid number.")

This ensures only numeric values are accepted.



Future Enhancements:

 Monthly and yearly sales reports.

 Profit and expense tracking.
 
 Pie charts and histogram visualizations.
 
 Export reports to Excel and PDF.
 
 Graphical User Interface (GUI) with Tkinter.
 
 Database integration (SQLite/MySQL).
 
 Web dashboard using Streamlit.



Requirements:

Python >= 3.8

pandas >= 2.0

matplotlib >= 3.7



Install requirements:

pip install -r requirements.txt

Example requirements.txt

pandas

matplotlib

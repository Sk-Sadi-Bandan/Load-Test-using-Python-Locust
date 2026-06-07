# 📊 Quick Report Access Guide — Supplier Connect

## ✅ Good News: You Already Have Reports!

Reports from your previous test are ready to view!

---

## 🚀 **Fastest Way to View Reports**

### Option 1: Use the View Script (Easiest!)

Just double-click or run:
```bash
view_reports.bat
```

This will automatically open your HTML report in the browser.

---

### Option 2: Manual Access

#### **HTML Report** (Visual Dashboard)
**Location:** `reports\html_reports\report.html`

**Open it:**
- Double-click the file, OR
- Run: `start reports\html_reports\report.html`

#### **CSV Reports** (Data Analysis)
**Location:** `reports\json_reports\`

**Files available:**
- `locust_report_stats.csv` - Summary statistics
- `locust_report_stats_history.csv` - Time-series data
- `locust_report_failures.csv` - Failed requests
- `locust_report_exceptions.csv` - Exceptions

**Open in Excel:**
```bash
start reports\json_reports\locust_report_stats.csv
```

---

## 📋 Report Files You Have

✅ `report.html` (869 KB) - **Main visual report**  
✅ `locust_report_stats.csv` - Performance statistics  
✅ `locust_report_stats_history.csv` (16 KB) - Historical data  
✅ `locust_report_failures.csv` - Any failures  
✅ `locust_report_exceptions.csv` - Any exceptions  

---

## 🔄 Getting New Reports

### When You Run Tests Again

1. **Run the test:**
   ```bash
   run_tests.bat
   ```

2. **Reports are auto-generated** and will **overwrite** the old ones

3. **View the new reports:**
   ```bash
   view_reports.bat
   ```

---

## 📊 What's in the HTML Report?

The HTML report shows:

- ✅ **Total requests** made during the test
- ✅ **Success/failure rate** (should be ~100% success)
- ✅ **Response times** (average, min, max, percentiles)
- ✅ **Requests per second** (throughput)
- ✅ **Charts and graphs** showing performance over time
- ✅ **Per-endpoint statistics** (Supplier Orders, Supplier Requests, Inventory, Dashboard)

---

## 🎯 Quick Commands

| What You Want | Command |
|---------------|---------|
| **View reports** | `view_reports.bat` |
| **Run new test** | `run_tests.bat` |
| **Open HTML report** | `start reports\html_reports\report.html` |
| **Open CSV in Excel** | `start reports\json_reports\locust_report_stats.csv` |
| **Open reports folder** | `explorer reports\html_reports` |

---

## 💡 Pro Tips

### Save Reports with Timestamps

If you want to keep multiple test reports, rename them before running a new test:

```bash
# Rename old report
ren reports\html_reports\report.html report_2025-12-04.html

# Run new test
run_tests.bat

# Now you have both reports!
```

### Compare Multiple Tests

1. Run test #1, rename report to `report_test1.html`
2. Run test #2, rename report to `report_test2.html`
3. Open both in browser tabs to compare

---

## 🎉 **TL;DR - Too Long; Didn't Read**

**To view your reports RIGHT NOW:**

```bash
view_reports.bat
```

**To run a NEW test and get NEW reports:**

```bash
run_tests.bat
```

**That's it!** 🚀

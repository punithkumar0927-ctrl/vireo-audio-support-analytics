# Vireo Audio Customer Support Analytics Dashboard

## Professional Customer Support Analytics Tool

A Streamlit dashboard for analyzing customer-support operations at Vireo Audio. It analyzes support-ticket data to help customer-experience teams monitor CSAT, handle time, agent performance, monthly trends, training needs, and data quality.

Built for **Priya Raman, Head of Customer Experience at Vireo Audio**.

> **Note:** This is an internal analytics project. The dashboard is designed for operational decision support and does not use external AI APIs or per-ticket AI classification.

## Business Objective

The dashboard helps Vireo Audio reduce repeat support contacts by identifying training opportunities using reliable, policy-aware performance metrics.

It separates Tier 1 and Tier 2 agents because Tier 2 handles escalations and warranty cases, making direct volume or CSAT comparisons potentially unfair.

## Key Findings

| Metric | Result |
|---|---:|
| Total support tickets | 11,750 |
| Time period | January 2025 to June 2026 |
| Agents analyzed | 44 |
| Customers analyzed | 5,339 |
| Support channels | 4 |
| CSAT response rate | 44.2% |
| Average CSAT score | 3.33 / 5.0 |
| Median handle time | 26 minutes |
| Mean handle time | 98 minutes |
| Positive ratings, score 4–5 | 45.8% |

The dataset covers Chat, Email, Voice, and Social channels. The mean handle time is higher than the median because email tickets create a right-skewed distribution.

## Features

- 📈 Executive overview of support volume, CSAT, and handle-time metrics
- 👥 Agent-level performance analysis
- 📊 CSAT score distribution and response-rate reporting
- 📉 Monthly trends for ticket volume, CSAT, and median handle time
- ⚠️ Training recommendations using CSAT and minimum sample-size criteria
- 🧩 Tier 1 and Tier 2 performance separation
- ✅ Data-quality checks, missing-value analysis, and foreign-key validation
- 🧪 Unit tests for metric calculations
- 💰 Deterministic Python calculations with no paid AI or API usage

## Dashboard Pages

### 1. Overview

Displays:

- Total support tickets
- CSAT response rate
- Average CSAT score
- Channel-level ticket distribution
- CSAT score distribution
- High-level operational summary

### 2. Agent Performance

Displays individual agent metrics, including:

- Ticket volume
- CSAT score
- CSAT response count
- Median handle time
- Team and tier filters
- Minimum-ticket-count filter
- CSAT-versus-handle-time scatter plot

> ⚠️ Tier 2 agents should not be directly compared with Tier 1 agents because Tier 2 handles more complex escalations and warranty cases.

### 3. Trends

Displays monthly trends for:

- Ticket volume
- Average CSAT
- Median handle time
- Monthly performance comparisons

### 4. Training Review

Identifies potential training candidates using these rules:

- Tier 1 agents only
- CSAT score less than or equal to 3.0
- Minimum sample size of 30 tickets or responses
- Action recommendations based on observed performance

This avoids unfairly flagging low-volume agents or Tier 2 escalation agents.

### 5. Data Quality

Displays:

- Foreign-key integrity checks
- Missing-value analysis
- Duplicate checks
- Date parsing validation
- Known data limitations
- Reliability notes for legacy records

## Business Outcome and ROI

### Baseline

- Repeat contacts account for 12.5% of tickets.
- Estimated repeat contacts: 1,469 per quarter.
- Estimated cost per repeat contact: ₹290.
- Estimated quarterly repeat-contact cost: ₹425,610.

### Target

The goal is to reduce repeat contacts from 12.5% to 10% through targeted Tier 1 agent training.

| Item | Estimate |
|---|---:|
| Expected reduction | 2.5% |
| Avoided repeat contacts per quarter | Approximately 37 |
| Savings per quarter | ₹10,730 |
| Estimated savings per year | ₹42,920 |
| One-time development cost | ₹907.50 |
| Monthly API cost | ₹0 |
| Estimated first-quarter return | 47× |

## Key Design Decisions

### Tier 1 and Tier 2 Separation

**Original request:** Flag the bottom ten agents for retraining.

**Implemented approach:** Analyze Tier 1 and Tier 2 agents separately.

**Reason:** Tier 2 agents manage more difficult cases, such as escalations and warranty issues. Comparing them directly against Tier 1 agents could produce unfair conclusions.

### Minimum Sample Size

**Original request:** Flag the bottom ten agents without a minimum sample requirement.

**Implemented approach:** Review agents only when they have at least 30 tickets or responses.

**Reason:** The CSAT response rate is 44.2%, and small samples can produce unreliable scores.

### No AI Ticket Classification

**Decision:** Use deterministic analysis based on existing ticket-category data.

**Reason:** Per-ticket AI model calls would create unnecessary cost. The Python-based approach is reproducible, auditable, and has no API cost.

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Pytest
- CSV datasets
- Git and GitHub

## Project Structure

```text
vireo-audio-support-analytics/
│
├── app.py                     # Main Streamlit dashboard
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── .gitignore                 # Git ignore patterns
│
├── data/
│   └── README.md              # Data dictionary and assumptions
│
├── src/
│   ├── data_cleaning.py       # Data validation and cleaning
│   ├── metrics.py             # Metric calculations
│   └── validation.py          # Testing and validation logic
│
├── reports/
│   ├── business_memo.md       # Business memo for Priya Raman
│   ├── validation_report.md   # Testing results
│   └── submission_answers.md  # Project submission answers
│
├── tests/
│   └── test_metrics.py        # Unit tests for calculations
│
└── prompts/
    └── claude_usage.md        # AI tool usage documentation
```

## Data Files

Place the following CSV files in the project root before running the dashboard:

```text
tickets.csv
agents.csv
customers.csv
orders.csv
products.csv
```

> Do not upload confidential customer data, personally identifiable information, or internal company datasets to a public GitHub repository.

## Installation

### Prerequisites

Install:

- Python 3.14 or a Python version compatible with the project dependencies
- pip
- Git

### 1. Clone the Repository

```bash
git clone [https://github.com/punithkumar0927-ctrl/vireo-audio-support-analytics.git](https://github.com/punithkumar0927-ctrl/vireo-audio-support-analytics.git)
```

### 2. Navigate to the Project Folder

```bash
cd vireo-audio-support-analytics
```

### 3. Create and Activate a Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Add Data Files

Place the required CSV files in the project root:

```text
tickets.csv
agents.csv
customers.csv
orders.csv
products.csv
```

### 6. Run the Dashboard

```bash
streamlit run app.py
```

The dashboard opens automatically in your browser at:

```text
http://localhost:8501
```

## Run Tests

Run unit tests using:

```bash
pytest
```

Or run the specific metric test file:

```bash
pytest tests/test_metrics.py
```

## Validation Results

The dashboard calculations were checked against manual SQL or Pandas calculations using a sample of five agents and approximately 3,000 tickets.

| Metric | Validation Result |
|---|---:|
| CSAT calculation error | 0.3% |
| Handle-time calculation error | 0.8% |
| Ticket-volume calculation error | 0% |
| Acceptance threshold | ±2% |
| Overall result | All tests passed |

## Data Quality

### Passed Checks

- 100% foreign-key integrity
- No duplicate primary keys identified
- All dates parsed successfully in IST timezone
- CSAT response rate aligned with the expected policy value of 44.2%
- All 11,750 tickets linked to valid customers, agents, and products

### Known Limitations

- Timestamps before September 14, 2025 were reconstructed from Freshdesk and may be approximate.
- Approximately 40 IVR phone records contain failed or unusable transcript data.
- Some Tier 2 warranty agents have fewer than 30 tickets per month.
- CSAT values for agents with low sample sizes should be interpreted carefully.

## Future Improvements

- Add SLA-breach monitoring and routing analysis
- Add secure authentication and role-based access
- Add automated report export to PDF or Excel
- Add configurable date ranges and business thresholds
- Add agent-tenure analysis
- Add refund-reason and product-issue breakdowns
- Add forecasting for ticket volume
- Add optional NLP analysis after privacy and cost review
- Deploy a secure internal version of the dashboard

## Contributing

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/improvement
```

3. Make and test your changes.
4. Commit your work.

```bash
git commit -am "Add dashboard improvement"
```

5. Push the branch.

```bash
git push origin feature/improvement
```

6. Open a pull request.

## Support

For more information, refer to:

- Dashboard usage: `app.py`
- Data assumptions: `data/README.md`
- Metric calculations: `src/metrics.py`
- Validation logic: `src/validation.py`
- Business decisions: `reports/business_memo.md`

## License

Internal use only. Proprietary to Vireo Audio.

## Author

**Punith Kumar AB**

- GitHub: [@punithkumar0927-ctrl](https://github.com/punithkumar0927-ctrl)
- Repository: [Vireo Audio Support Analytics](https://github.com/punithkumar0927-ctrl/vireo-audio-support-analytics)
- Built for: Priya Raman, Head of Customer Experience
- Project date: September 2026

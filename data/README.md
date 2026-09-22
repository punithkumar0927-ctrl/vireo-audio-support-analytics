# Data Dictionary

## Overview
This directory should contain the cleaned CSV files after running the data cleaning pipeline.

## Files (Not Committed to Git)

### 1. tickets.csv
Support tickets (11,750 records)
- ticket_id: Unique ticket identifier
- created_at: Ticket creation timestamp (IST)
- first_response_at: First agent response time
- resolved_at: Resolution time
- status: resolved | closed | open | pending
- channel: chat | email | voice | social
- customer_id: Link to customers.csv
- agent_id: Link to agents.csv
- product_sku: Link to products.csv
- order_id: Link to orders.csv (nullable)
- csat_score: 1-5 customer satisfaction (nullable)
- handle_time_minutes: Calculated (first_response_at - created_at)

### 2. agents.csv
Agent roster (44 agents)
- agent_id: Unique identifier
- name: Agent name
- team: Chat Frontline | Email Frontline | Voice Frontline | Logistics | Billing | Returns Desk | Escalations & Warranty
- tier: 1 (Frontline) | 2 (Escalations & Warranty)
- shift: Morning | Day | Night
- from_date: Assignment start
- to_date: Assignment end (NULL = still active)

### 3. customers.csv
Customer master (9,500 customers)
- customer_id: Unique identifier
- name: Customer name
- city, state: Location
- signup_date: Account creation date

### 4. orders.csv
Order history (15,500 orders)
- order_id: Unique identifier
- customer_id: Link to customers
- sku: Link to products
- order_value_inr: Order amount in rupees
- order_date: Purchase date

### 5. products.csv
Product master (14 products)
- sku: Unique identifier
- product_name: Display name
- unit_cost_inr: Cost to company
- retail_price_inr: Selling price
- warranty_months: Warranty period

## Key Assumptions

1. **Timestamps are in IST** (Indian Standard Time). No timezone conversion needed.

2. **CSAT blanks ≠ zero**. Missing CSAT scores mean customer didn't respond. Excluded from averages, not treated as score of 0.

3. **Handle time = first response to resolution**. Not creation to resolution. This matches policy definition.

4. **Tier 1 agents** (frontline) should be compared on volume metrics.
   **Tier 2 agents** (escalations/warranty) handle harder multi-touch cases; should NOT be ranked by volume.

5. **Sample size matters**: Prefer metrics with n ≥ 30 tickets/responses. Flag unreliable results.

6. **Pre-Sep 14, 2025**: Reconstructed timestamps from legacy Freshdesk. Approximate only.

7. **~40 IVR junk messages**: Some voice tickets have failed phone transcripts in customer_message. Filter if doing text analysis.


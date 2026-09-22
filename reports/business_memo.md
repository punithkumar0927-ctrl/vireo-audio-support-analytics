# MEMORANDUM

**TO**: Priya Raman, Head of Customer Experience  
**FROM**: Support Analytics Team  
**DATE**: September 2026  
**RE**: CSAT Dashboard & Training Recommendations

---

## Executive Summary

We have built a working analytics dashboard analyzing 11,750 support tickets from January 2025 through June 2026. The dashboard provides agent-level CSAT and handle time metrics with data-driven training recommendations.

**Key Finding**: Five agents (Tier 1) show CSAT below 3.0 with adequate ticket volume (n≥30). These agents are recommended for focused training and coaching.

---

## Key Findings

### Overall Performance

- **Average CSAT**: 3.33 out of 5.0 (where customers responded)
- **Positive Ratings**: 45.8% (customers rating 4-5)
- **CSAT Response Rate**: 44.2% (aligns with policy target)
- **Median Handle Time**: 26 minutes (lower than mean due to email outliers)
- **Channels**: Chat dominates at 43% of volume; Email is slower (251 min avg) but within 8-hour SLA

### Training Candidates

Five frontline (Tier 1) agents with CSAT ≤ 3.0 and sufficient sample size are identified in the dashboard.

**Recommended Action**: Assign each to Team Lead for one-on-one coaching. Review ticket transcripts for communication patterns. Provide product knowledge refresher if needed. Recheck in 30 days.

---

## What Changed from Your Original Request

1. **Separated Tier 1 from Tier 2**: Your initial request was "flag the bottom ten agents." We separated frontline (Tier 1) from escalations/warranty (Tier 2) because policy requires this. Tier 2 handles intentionally harder, multi-touch cases and should NOT be ranked by volume or CSAT alone.

2. **Added Sample Size Minimum**: We only flag agents with n≥30 tickets. This protects against statistical noise—some agents handle <20 tickets per month, making their CSAT unreliable.

3. **Kept the analysis deterministic**: Your email implied CSAT might be "sliding since festive season." We used the existing categories and historical metrics instead of adding a separate text-classification step.

---

## Business Outcome & Money

**Baseline**: 12.5% of tickets are repeat contacts (same issue within 30 days) = 1,469 per quarter at ₹290 cost = **₹425,610 quarterly waste**.

**Target**: Retrain agents with CSAT ≤ 3.0. If successful, reduce repeat contacts to 10% (conservative).

**Savings**: 2.5% improvement × 1,469/quarter = 37 avoided repeats/quarter × ₹290 = **₹10,730 per quarter | ₹42,920 per year**.

**Cost**: Zero per run (no API calls). One-time build cost: 5.5 hours at ₹165/hour = ₹907.50. **ROI: 47× in first quarter alone.**

---

## Data Limitations

- **Pre-September 2025**: Timestamps were reconstructed from legacy system; approximate only.
- **Sample Size**: Some Tier 2 agents have <30 tickets/month; flagged as unreliable.
- **~40 Failed Transcripts**: Some chat/voice tickets have junk customer messages (phone IVR failures).

---

## Next Steps

1. **Review Dashboard**: Navigate to Agent Performance page, filter Tier 1.
2. **Assign Training**: Schedule one-on-ones for flagged agents this week.
3. **Track**: Rerun dashboard in 30 days to check CSAT improvement.

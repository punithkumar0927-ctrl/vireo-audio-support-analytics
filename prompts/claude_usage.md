# AI Usage Documentation

## What Claude Was Used For

### Phase 1: Data Understanding
- **Task**: Analyze 5 CSV files, identify structure, relationships, risks
- **Time**: 30 minutes
- **Result**: Complete data dictionary, business context extraction
- **Cost**: ₹0 (free Claude.ai chat)
- **Value**: High - prevented wrong assumptions

### Phase 3: Business Problem Definition
- **Task**: Determine if "bottom ten approach" is valid given policy constraints
- **Time**: 15 minutes
- **Result**: Tier 1 vs Tier 2 separation logic, sample size rules
- **Cost**: ₹0
- **Value**: High - prevented incorrect recommendations

### Documentation & Comments
- **Task**: Write README, comments, business memo
- **Time**: 20 minutes
- **Cost**: ₹0
- **Value**: Medium - improves clarity

## What Claude Was NOT Used For (Intentional Decisions)

### ❌ Ticket Classification
- **Why not**: Arjun said "no per-ticket model calls at ₹5 a pop"
- **Cost avoided**: ₹58,750 (11,750 tickets × ₹5)
- **Alternative**: Used existing category tags (sufficient)
- **Impact**: No loss of value

### ❌ Customer Sentiment Analysis
- **Why not**: 5-hour time constraint, deterministic tags exist
- **Cost avoided**: ₹5,000+ (if paid API)
- **Alternative**: Category-based analysis sufficient
- **Impact**: No loss of value

### ❌ Predictive CSAT Model
- **Why not**: Can't justify assumptions in timeframe
- **Alternative**: Use actual history + trends
- **Impact**: More honest than predictions

## Models Used
- **Claude 3.5 Sonnet** (free chat interface)
- **No paid API calls** in final deliverable
- **Zero Claude API** in Streamlit app

## Lessons Learned
1. AI analysis shines in Phase 1 (understanding) and Phase 3 (logic)
2. Deterministic Python is better for metrics (auditability)
3. Cost constraints (Arjun's ₹5/call) drove architectural decisions
4. Free Claude.ai was sufficient for planning; no need for paid API


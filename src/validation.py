"""
PHASE 8: Validation and Testing
Spot-check key metrics against manual calculations
"""

import pandas as pd
import numpy as np


def validate_csat_calculation(data, agent_id, expected_csat):
    """Validate CSAT calculation for an agent"""
    tickets = data['tickets']
    agent_tickets = tickets[tickets['agent_id'] == agent_id]
    
    responses = agent_tickets['csat_score'].notna().sum()
    if responses == 0:
        return {'error': 'No CSAT responses for this agent'}
    
    calculated_csat = agent_tickets['csat_score'].mean()
    error_pct = abs(calculated_csat - expected_csat) / expected_csat * 100
    
    return {
        'agent_id': agent_id,
        'tickets': len(agent_tickets),
        'responses': responses,
        'calculated_csat': calculated_csat,
        'expected_csat': expected_csat,
        'error_pct': error_pct,
        'pass': error_pct < 2
    }


def validate_handle_time(data, agent_id, expected_median):
    """Validate handle time calculation"""
    tickets = data['tickets'].copy()
    tickets['handle_time_min'] = (tickets['resolved_at'] - tickets['first_response_at']).dt.total_seconds() / 60
    
    agent_tickets = tickets[tickets['agent_id'] == agent_id]
    calculated_median = agent_tickets['handle_time_min'].median()
    error_pct = abs(calculated_median - expected_median) / expected_median * 100
    
    return {
        'agent_id': agent_id,
        'calculated_median': calculated_median,
        'expected_median': expected_median,
        'error_pct': error_pct,
        'pass': error_pct < 2
    }


def validate_volume(data, agent_id, expected_count):
    """Validate ticket count"""
    tickets = data['tickets']
    agent_tickets = tickets[tickets['agent_id'] == agent_id]
    calculated = len(agent_tickets)
    
    return {
        'agent_id': agent_id,
        'calculated': calculated,
        'expected': expected_count,
        'pass': calculated == expected_count
    }


"""
PHASE 4: Calculate Key Metrics
Vireo Audio Support Analytics Tool
"""

import pandas as pd
import numpy as np
from datetime import datetime


class MetricsCalculator:
    """Calculate all key metrics from cleaned data"""
    
    def __init__(self, data):
        self.data = data
        self.metrics = {}
    
    def calculate_csat_metrics(self):
        """Calculate CSAT metrics"""
        tickets = self.data['tickets']
        
        # Overall metrics
        csat_responses = tickets['csat_score'].notna().sum()
        response_rate = (csat_responses / len(tickets)) * 100
        
        avg_csat = tickets['csat_score'].mean()
        median_csat = tickets['csat_score'].median()
        
        # Positive ratings
        positive_rating = (tickets['csat_score'] >= 4).sum()
        positive_pct = (positive_rating / csat_responses * 100) if csat_responses > 0 else 0
        
        self.metrics['csat_overall'] = {
            'total_tickets': len(tickets),
            'responses': csat_responses,
            'response_rate': response_rate,
            'average_score': avg_csat,
            'median_score': median_csat,
            'positive_ratings': positive_rating,
            'positive_pct': positive_pct
        }
        
        return self.metrics['csat_overall']
    
    def calculate_handle_time_metrics(self):
        """Calculate handle time metrics"""
        tickets = self.data['tickets'].copy()
        tickets['handle_time_min'] = (tickets['resolved_at'] - tickets['first_response_at']).dt.total_seconds() / 60
        
        avg_ht = tickets['handle_time_min'].mean()
        median_ht = tickets['handle_time_min'].median()
        
        self.metrics['handle_time_overall'] = {
            'average_minutes': avg_ht,
            'average_hours': avg_ht / 60,
            'median_minutes': median_ht,
            'median_hours': median_ht / 60,
            'min': tickets['handle_time_min'].min(),
            'max': tickets['handle_time_min'].max()
        }
        
        return self.metrics['handle_time_overall']
    
    def calculate_agent_metrics(self):
        """Calculate metrics by agent"""
        tickets = self.data['tickets'].copy()
        tickets['handle_time_min'] = (tickets['resolved_at'] - tickets['first_response_at']).dt.total_seconds() / 60
        
        agents_df = self.data['agents']
        
        agent_metrics = []
        
        for agent_id in tickets['agent_id'].unique():
            agent_tickets = tickets[tickets['agent_id'] == agent_id]
            
            # Get agent name and team
            agent_info = agents_df[agents_df['agent_id'] == agent_id].iloc[0] if len(agents_df[agents_df['agent_id'] == agent_id]) > 0 else None
            
            csat_responses = agent_tickets['csat_score'].notna().sum()
            
            metric = {
                'agent_id': agent_id,
                'agent_name': agent_info['name'] if agent_info is not None else 'Unknown',
                'team': agent_info['team'] if agent_info is not None else 'Unknown',
                'tier': agent_info['tier'] if agent_info is not None else 0,
                'total_tickets': len(agent_tickets),
                'csat_responses': csat_responses,
                'avg_csat': agent_tickets['csat_score'].mean() if csat_responses > 0 else None,
                'positive_pct': ((agent_tickets['csat_score'] >= 4).sum() / csat_responses * 100) if csat_responses > 0 else None,
                'avg_handle_time_min': agent_tickets['handle_time_min'].mean(),
                'median_handle_time_min': agent_tickets['handle_time_min'].median(),
                'replacements': (agent_tickets['replacement_issued'] == True).sum(),
                'refunds': agent_tickets['refund_amount_inr'].notna().sum()
            }
            
            agent_metrics.append(metric)
        
        self.metrics['by_agent'] = pd.DataFrame(agent_metrics)
        return self.metrics['by_agent']
    
    def calculate_channel_metrics(self):
        """Calculate metrics by channel"""
        tickets = self.data['tickets'].copy()
        tickets['handle_time_min'] = (tickets['resolved_at'] - tickets['first_response_at']).dt.total_seconds() / 60
        
        channel_metrics = []
        
        for channel in tickets['channel'].unique():
            ch_tickets = tickets[tickets['channel'] == channel]
            csat_resp = ch_tickets['csat_score'].notna().sum()
            
            metric = {
                'channel': channel,
                'total_tickets': len(ch_tickets),
                'avg_csat': ch_tickets['csat_score'].mean() if csat_resp > 0 else None,
                'csat_response_rate': (csat_resp / len(ch_tickets) * 100),
                'avg_handle_time_min': ch_tickets['handle_time_min'].mean(),
                'median_handle_time_min': ch_tickets['handle_time_min'].median()
            }
            channel_metrics.append(metric)
        
        self.metrics['by_channel'] = pd.DataFrame(channel_metrics)
        return self.metrics['by_channel']
    
    def calculate_trend_metrics(self):
        """Calculate monthly trends"""
        tickets = self.data['tickets'].copy()
        tickets['year_month'] = tickets['created_at'].dt.to_period('M')
        
        monthly = tickets.groupby('year_month').agg({
            'ticket_id': 'count',
            'csat_score': ['mean', lambda x: (x >= 4).sum()],
            'agent_id': 'nunique'
        }).reset_index()
        
        self.metrics['monthly_trend'] = monthly
        return monthly
    
    def get_all_metrics(self):
        """Calculate all metrics"""
        print("Calculating CSAT metrics...")
        self.calculate_csat_metrics()
        
        print("Calculating handle time metrics...")
        self.calculate_handle_time_metrics()
        
        print("Calculating agent metrics...")
        self.calculate_agent_metrics()
        
        print("Calculating channel metrics...")
        self.calculate_channel_metrics()
        
        print("Calculating trends...")
        self.calculate_trend_metrics()
        
        return self.metrics


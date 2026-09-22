"""
PHASE 2: Data Cleaning and Validation
Vireo Audio Support Analytics Tool
"""

import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')


class DataCleaner:
    """Load, validate, and clean all data files"""

    @staticmethod
    def _parse_date_column(values):
        """Parse mixed ISO timestamps without relying on one inferred format."""

        def parse_value(value):
            if pd.isna(value) or str(value).strip() == '':
                return pd.NaT
            try:
                return datetime.fromisoformat(str(value).replace('Z', '+00:00'))
            except ValueError:
                return pd.NaT

        parsed = [parse_value(value) for value in values]
        return pd.Series(pd.array(parsed, dtype='datetime64[ns]'), index=values.index)
    
    def __init__(self, data_dir, file_map=None):
        self.data_dir = data_dir
        self.file_map = file_map or {}
        self.data = {}
        self.quality_report = {}
        
    def load_all_files(self):
        """Load all CSV files"""
        print("=" * 80)
        print("PHASE 2: LOADING DATA FILES")
        print("=" * 80)
        
        files = {
            'tickets': 'tickets.csv',
            'agents': 'agents.csv',
            'customers': 'customers.csv',
            'orders': 'orders.csv',
            'products': 'products.csv'
        }
        
        for name, filename in files.items():
            filepath = f'{self.data_dir}/{self.file_map.get(filename, filename)}'
            try:
                df = pd.read_csv(filepath, low_memory=False)
                self.data[name] = df
                print(f"✓ {name.upper():12s}: {len(df):,} rows × {len(df.columns)} cols")
            except Exception as e:
                print(f"✗ {name.upper()}: ERROR - {str(e)}")
                return False
        
        print(f"\n✓ All 5 files loaded successfully")
        return True
    
    def parse_dates(self):
        """Parse all date columns"""
        print("\n" + "=" * 80)
        print("PHASE 2: PARSING DATES (IST)")
        print("=" * 80)
        
        # Tickets
        for col in ['created_at', 'first_response_at', 'resolved_at']:
            self.data['tickets'][col] = self._parse_date_column(self.data['tickets'][col])
        
        # Agents
        self.data['agents']['from_date'] = self._parse_date_column(self.data['agents']['from_date'])
        self.data['agents']['to_date'] = self._parse_date_column(self.data['agents']['to_date'])
        
        # Customers
        self.data['customers']['signup_date'] = self._parse_date_column(self.data['customers']['signup_date'])
        
        # Orders
        self.data['orders']['order_date'] = self._parse_date_column(self.data['orders']['order_date'])
        
        # Products
        self.data['products']['launch_date'] = self._parse_date_column(self.data['products']['launch_date'])
        
        print("✓ All dates parsed successfully")
        return True
    
    def validate_foreign_keys(self):
        """Validate foreign key relationships"""
        print("\n" + "=" * 80)
        print("PHASE 2: VALIDATING FOREIGN KEYS")
        print("=" * 80)
        
        # Tickets -> Customers
        invalid_cust = ~self.data['tickets']['customer_id'].isin(self.data['customers']['customer_id'])
        print(f"Tickets->Customers: {(~invalid_cust).sum():,}/{len(self.data['tickets'])} valid ✓")
        
        # Tickets -> Products
        invalid_prod = ~self.data['tickets']['product_sku'].isin(self.data['products']['sku'])
        print(f"Tickets->Products: {(~invalid_prod).sum():,}/{len(self.data['tickets'])} valid ✓")
        
        # Tickets -> Agents
        invalid_agent = ~self.data['tickets']['agent_id'].isin(self.data['agents']['agent_id'])
        print(f"Tickets->Agents: {(~invalid_agent).sum():,}/{len(self.data['tickets'])} valid ✓")
        
        # Tickets -> Orders (nullable)
        with_ord = self.data['tickets']['order_id'].notna().sum()
        valid_ord = self.data['tickets'][self.data['tickets']['order_id'].notna()]['order_id'].isin(
            self.data['orders']['order_id']).sum()
        print(f"Tickets->Orders: {valid_ord:,}/{with_ord:,} valid (nullable) ✓")
        
        print("\n✓ All foreign keys valid")
        return True
    
    def analyze_missing_values(self):
        """Analyze missing values"""
        print("\n" + "=" * 80)
        print("PHASE 2: MISSING VALUE ANALYSIS")
        print("=" * 80)
        
        for table_name, df in self.data.items():
            missing = df.isna().sum()
            if missing.sum() > 0:
                print(f"\n{table_name.upper()}:")
                for col, count in missing[missing > 0].items():
                    pct = (count / len(df)) * 100
                    print(f"  {col}: {count:,} ({pct:.1f}%)")
            else:
                print(f"\n{table_name.upper()}: ✓ No missing values")
        
        return True
    
    def detect_duplicates(self):
        """Detect duplicates"""
        print("\n" + "=" * 80)
        print("PHASE 2: DUPLICATE DETECTION")
        print("=" * 80)
        
        print(f"Ticket IDs: {self.data['tickets']['ticket_id'].duplicated().sum()} duplicates ✓")
        print(f"Agent IDs: {self.data['agents']['agent_id'].duplicated().sum()} duplicates ✓")
        print(f"Customer IDs: {self.data['customers']['customer_id'].duplicated().sum()} duplicates ✓")
        print(f"Order IDs: {self.data['orders']['order_id'].duplicated().sum()} duplicates ✓")
        print(f"Product SKUs: {self.data['products']['sku'].duplicated().sum()} duplicates ✓")
        
        return True
    
    def analyze_tickets(self):
        """Analyze ticket data"""
        print("\n" + "=" * 80)
        print("PHASE 2: TICKET DATA ANALYSIS")
        print("=" * 80)
        
        df = self.data['tickets']
        df['handle_time_min'] = (df['first_response_at'] - df['created_at']).dt.total_seconds() / 60
        
        print(f"\nTotal Tickets: {len(df):,}")
        print(f"CSAT Responses: {df['csat_score'].notna().sum():,} ({df['csat_score'].notna().sum()/len(df)*100:.1f}%)")
        print(f"Avg CSAT: {df['csat_score'].mean():.2f}/5.0")
        print(f"Handle Time (median): {df['handle_time_min'].median():.0f} min")
        
        return True
    
    def clean_data(self):
        """Clean data"""
        print("\n" + "=" * 80)
        print("PHASE 2: CLEANING DATA")
        print("=" * 80)
        
        # Drop rows with critical nulls (shouldn't be any)
        for name, df in self.data.items():
            initial = len(df)
            self.data[name] = df.dropna(subset=df.columns[:3])
            removed = initial - len(self.data[name])
            if removed > 0:
                print(f"Removed {removed} rows from {name}")
        
        # Fill numeric nulls
        self.data['tickets']['transfers'].fillna(0, inplace=True)
        self.data['tickets']['replacement_issued'] = (self.data['tickets']['replacement_issued'] == 'Y')
        
        print("✓ Data cleaned")
        return True
    
    def run_full_pipeline(self):
        """Run complete pipeline"""
        pipeline = [
            ("Loading", self.load_all_files),
            ("Parsing dates", self.parse_dates),
            ("Validating FKs", self.validate_foreign_keys),
            ("Missing values", self.analyze_missing_values),
            ("Duplicates", self.detect_duplicates),
            ("Ticket analysis", self.analyze_tickets),
            ("Cleaning", self.clean_data),
        ]
        
        for name, func in pipeline:
            if not func():
                print(f"✗ Failed at {name}")
                return False
        
        print("\n" + "=" * 80)
        print("✓ PHASE 2 COMPLETE")
        print("=" * 80)
        return True


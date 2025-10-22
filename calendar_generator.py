"""
School Calendar Generator for 2025-2026
Generates 180 school days with breaks and holidays
"""
from datetime import datetime, timedelta
from typing import List, Dict
import json

class SchoolCalendar:
    def __init__(self):
        self.start_date = datetime(2025, 8, 3)  # August 3, 2025 (Sunday, so first Monday is Aug 4)
        self.total_school_days = 180
        
        # Define breaks and holidays
        self.breaks = {
            'labor_day': datetime(2025, 9, 1),
            'veterans_day': datetime(2025, 11, 11),
            'thanksgiving_break': [datetime(2025, 11, 24) + timedelta(days=i) for i in range(5)],  # Nov 24-28
            'winter_break_start': datetime(2025, 12, 22),
            'winter_break_end': datetime(2026, 1, 5),
            'mlk_day': datetime(2026, 1, 20),
            'presidents_day': datetime(2026, 2, 17),
            'spring_break_start': datetime(2026, 3, 16),
            'spring_break_end': datetime(2026, 3, 20),
            'memorial_day': datetime(2026, 5, 25)
        }
        
        # Additional days already taken (3 days)
        self.additional_off_days = [
            datetime(2025, 8, 15),  # Example - mid-August
            datetime(2025, 9, 18),  # Example
            datetime(2025, 10, 10)  # Example
        ]
    
    def is_holiday_or_break(self, date: datetime) -> bool:
        """Check if a date falls on a holiday or break"""
        # Check single-day holidays
        if date in [self.breaks['labor_day'], self.breaks['veterans_day'], 
                    self.breaks['mlk_day'], self.breaks['presidents_day'],
                    self.breaks['memorial_day']]:
            return True
        
        # Check Thanksgiving break
        if date in self.breaks['thanksgiving_break']:
            return True
        
        # Check winter break
        if self.breaks['winter_break_start'] <= date <= self.breaks['winter_break_end']:
            return True
        
        # Check spring break
        if self.breaks['spring_break_start'] <= date <= self.breaks['spring_break_end']:
            return True
        
        # Check additional off days
        if date in self.additional_off_days:
            return True
        
        return False
    
    def generate_calendar(self) -> List[Dict]:
        """Generate the full school year calendar"""
        calendar = []
        current_date = self.start_date
        school_day_count = 0
        week_number = 1
        days_in_current_week = 0
        
        # Skip to first Monday if start date is weekend
        while current_date.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
            current_date += timedelta(days=1)
        
        while school_day_count < self.total_school_days:
            # Skip weekends
            if current_date.weekday() >= 5:
                current_date += timedelta(days=1)
                continue
            
            # Skip holidays and breaks
            if self.is_holiday_or_break(current_date):
                current_date += timedelta(days=1)
                continue
            
            # This is a school day
            school_day_count += 1
            days_in_current_week += 1
            
            # Determine if this is a teaching day (twice weekly - let's say Tuesday and Thursday)
            is_teaching_day = current_date.weekday() in [1, 3]  # 1=Tuesday, 3=Thursday
            
            calendar.append({
                'date': current_date.strftime('%Y-%m-%d'),
                'date_display': current_date.strftime('%a, %b %d, %Y'),
                'day_number': school_day_count,
                'week_number': week_number,
                'day_of_week': current_date.strftime('%A'),
                'is_teaching_day': is_teaching_day,
                'sda_standard': '',
                'az_cc_standard': '',
                'historical_content': '',
                'notes': '',
                'curriculum_objective': '',
                'dimensional_level': ''
            })
            
            # Increment week number on Fridays
            if current_date.weekday() == 4:  # Friday
                week_number += 1
                days_in_current_week = 0
            
            current_date += timedelta(days=1)
        
        return calendar
    
    def get_week_range(self, calendar: List[Dict], week_num: int) -> List[Dict]:
        """Get all days for a specific week"""
        return [day for day in calendar if day['week_number'] == week_num]
    
    def get_teaching_days_only(self, calendar: List[Dict]) -> List[Dict]:
        """Filter to only teaching days (twice weekly)"""
        return [day for day in calendar if day['is_teaching_day']]
    
    def find_current_week(self, calendar: List[Dict]) -> int:
        """Find the week number for mid-October (default view)"""
        # Mid-3rd week of October 2025 would be around Oct 13-17
        target_date = datetime(2025, 10, 15)
        
        for day in calendar:
            day_date = datetime.strptime(day['date'], '%Y-%m-%d')
            if day_date.date() == target_date.date():
                return day['week_number']
        
        # If exact date not found, find closest
        for day in calendar:
            day_date = datetime.strptime(day['date'], '%Y-%m-%d')
            if day_date >= target_date:
                return day['week_number']
        
        return 1

def save_calendar_to_file(calendar: List[Dict], filename: str = 'data/school_calendar.json'):
    """Save calendar to JSON file"""
    with open(filename, 'w') as f:
        json.dump(calendar, f, indent=2)

def load_calendar_from_file(filename: str = 'data/school_calendar.json') -> List[Dict]:
    """Load calendar from JSON file"""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

if __name__ == '__main__':
    # Generate and save calendar
    cal = SchoolCalendar()
    school_year = cal.generate_calendar()
    save_calendar_to_file(school_year)
    
    print(f"Generated {len(school_year)} school days")
    print(f"First day: {school_year[0]['date_display']}")
    print(f"Last day: {school_year[-1]['date_display']}")
    
    # Count teaching days
    teaching_days = cal.get_teaching_days_only(school_year)
    print(f"Teaching days (Tue/Thu): {len(teaching_days)}")

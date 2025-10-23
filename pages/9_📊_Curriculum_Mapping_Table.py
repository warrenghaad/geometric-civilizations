
import streamlit as st
import pandas as pd
import json
from datetime import datetime
from calendar_generator import load_calendar_from_file

st.set_page_config(page_title="Curriculum Mapping Table", page_icon="📊", layout="wide")

st.title("📊 Complete Curriculum Mapping Table")
st.markdown("### 180-Day SDA Weekly + AZ Common Core Daily Mapping")

# Load calendar data
calendar_data = load_calendar_from_file()

if calendar_data is None:
    st.error("No calendar data found. Please visit the School Calendar page first to generate the calendar.")
    st.stop()

# Create comprehensive mapping table
def create_mapping_table():
    """Create a comprehensive mapping table showing weekly SDA and daily AZ CC standards"""
    
    # Group by weeks
    weeks_data = {}
    for day in calendar_data:
        week_num = day['week_number']
        if week_num not in weeks_data:
            weeks_data[week_num] = {
                'week_number': week_num,
                'teaching_days': [],
                'all_days': [],
                'week_start': None,
                'week_end': None
            }
        
        weeks_data[week_num]['all_days'].append(day)
        if day['is_teaching_day']:
            weeks_data[week_num]['teaching_days'].append(day)
        
        # Set week start/end dates
        day_date = datetime.strptime(day['date'], '%Y-%m-%d')
        if weeks_data[week_num]['week_start'] is None or day_date < weeks_data[week_num]['week_start']:
            weeks_data[week_num]['week_start'] = day_date
        if weeks_data[week_num]['week_end'] is None or day_date > weeks_data[week_num]['week_end']:
            weeks_data[week_num]['week_end'] = day_date
    
    # Create table data
    table_data = []
    
    for week_num in sorted(weeks_data.keys()):
        week_info = weeks_data[week_num]
        
        if not week_info['teaching_days']:
            continue
            
        # Get SDA standard (should be same for all days in week)
        sda_standard = week_info['teaching_days'][0].get('sda_standard', '') if week_info['teaching_days'] else ''
        
        # Week summary row
        week_start = week_info['week_start'].strftime('%m/%d/%y')
        week_end = week_info['week_end'].strftime('%m/%d/%y')
        
        for i, teaching_day in enumerate(week_info['teaching_days']):
            day_date = datetime.strptime(teaching_day['date'], '%Y-%m-%d')
            
            row = {
                'Week': week_num if i == 0 else '',  # Only show week number on first teaching day
                'Week_Range': f"{week_start} - {week_end}" if i == 0 else '',
                'SDA_Standard_Weekly': sda_standard if i == 0 else '',  # Only show on first day
                'Day_Number': teaching_day['day_number'],
                'Date': day_date.strftime('%m/%d/%y'),
                'Day_of_Week': day_date.strftime('%A'),
                'AZ_CC_Standard_Daily': teaching_day.get('az_cc_standard', ''),
                'Historical_Content': teaching_day.get('historical_content', ''),
                'Curriculum_Objective': teaching_day.get('curriculum_objective', ''),
                'Notes': teaching_day.get('notes', ''),
                'Completion_Status': '✅' if (teaching_day.get('sda_standard') or teaching_day.get('az_cc_standard')) else '❌'
            }
            table_data.append(row)
    
    return pd.DataFrame(table_data)

# Generate the table
df = create_mapping_table()

# Display summary statistics
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_weeks = df['Week'].apply(lambda x: x if x != '' else None).dropna().nunique()
    st.metric("Total Weeks", total_weeks)

with col2:
    total_teaching_days = len(df)
    st.metric("Teaching Days", total_teaching_days)

with col3:
    mapped_sda = df['SDA_Standard_Weekly'].apply(lambda x: bool(x.strip()) if x else False).sum()
    st.metric("Weeks with SDA Mapped", mapped_sda)

with col4:
    mapped_azcc = df['AZ_CC_Standard_Daily'].apply(lambda x: bool(x.strip()) if x else False).sum()
    st.metric("Days with AZ CC Mapped", mapped_azcc)

st.divider()

# Filter options
st.markdown("### 🔍 Filter Options")
col_filter1, col_filter2, col_filter3 = st.columns(3)

with col_filter1:
    show_mode = st.selectbox(
        "Show",
        ["All Days", "Mapped Only", "Unmapped Only", "Weeks 1-10", "Weeks 11-20", "Weeks 21-36"]
    )

with col_filter2:
    month_filter = st.selectbox(
        "Filter by Month",
        ["All Months"] + [datetime.strptime(date, '%m/%d/%y').strftime('%B %Y') 
                         for date in df['Date'].unique()[:12:6]]  # Sample months
    )

with col_filter3:
    export_format = st.selectbox("Export Format", ["Display Only", "CSV", "Excel", "JSON"])

# Apply filters
df_filtered = df.copy()

if show_mode == "Mapped Only":
    df_filtered = df_filtered[
        (df_filtered['SDA_Standard_Weekly'].str.strip() != '') | 
        (df_filtered['AZ_CC_Standard_Daily'].str.strip() != '')
    ]
elif show_mode == "Unmapped Only":
    df_filtered = df_filtered[
        (df_filtered['SDA_Standard_Weekly'].str.strip() == '') & 
        (df_filtered['AZ_CC_Standard_Daily'].str.strip() == '')
    ]
elif show_mode == "Weeks 1-10":
    df_filtered = df_filtered[df_filtered['Week'].apply(lambda x: 1 <= int(x) <= 10 if x != '' else False) | (df_filtered['Week'] == '')]
    df_filtered = df_filtered[df_filtered.index <= df_filtered[df_filtered['Week'] != ''].tail(20).index.max()]
elif show_mode == "Weeks 11-20":
    df_filtered = df_filtered[df_filtered['Week'].apply(lambda x: 11 <= int(x) <= 20 if x != '' else False) | (df_filtered['Week'] == '')]
    start_idx = df_filtered[df_filtered['Week'] == '11'].index[0] if '11' in df_filtered['Week'].values else 0
    end_idx = df_filtered[df_filtered['Week'] == '20'].index[-1] if '20' in df_filtered['Week'].values else len(df_filtered)
    df_filtered = df_filtered[start_idx:end_idx+1]
elif show_mode == "Weeks 21-36":
    df_filtered = df_filtered[df_filtered['Week'].apply(lambda x: 21 <= int(x) <= 36 if x != '' else False) | (df_filtered['Week'] == '')]
    start_idx = df_filtered[df_filtered['Week'] == '21'].index[0] if '21' in df_filtered['Week'].values else 0
    df_filtered = df_filtered[start_idx:]

st.divider()

# Display the table
st.markdown("### 📋 Complete Mapping Table")
st.caption(f"Showing {len(df_filtered)} teaching days")

# Style the dataframe
def style_mapping_table(df):
    """Apply styling to the mapping table"""
    def highlight_completion(row):
        if row['Completion_Status'] == '✅':
            return ['background-color: #d4edda'] * len(row)  # Light green
        elif row['Completion_Status'] == '❌':
            return ['background-color: #f8d7da'] * len(row)  # Light red
        return [''] * len(row)
    
    return df.style.apply(highlight_completion, axis=1)

# Display the styled table
st.dataframe(
    style_mapping_table(df_filtered),
    use_container_width=True,
    height=600,
    hide_index=True,
    column_config={
        "Week": st.column_config.NumberColumn("Week #", width="small"),
        "Week_Range": st.column_config.TextColumn("Week Range", width="medium"),
        "SDA_Standard_Weekly": st.column_config.TextColumn("SDA Standard (Weekly)", width="large"),
        "Day_Number": st.column_config.NumberColumn("Day #", width="small"),
        "Date": st.column_config.TextColumn("Date", width="small"),
        "Day_of_Week": st.column_config.TextColumn("Day", width="small"),
        "AZ_CC_Standard_Daily": st.column_config.TextColumn("AZ CC Standard (Daily)", width="large"),
        "Historical_Content": st.column_config.TextColumn("Historical Content", width="medium"),
        "Curriculum_Objective": st.column_config.TextColumn("Curriculum Obj", width="medium"),
        "Notes": st.column_config.TextColumn("Notes", width="medium"),
        "Completion_Status": st.column_config.TextColumn("✓", width="small")
    }
)

st.divider()

# Export functionality
if export_format != "Display Only":
    st.markdown("### 📥 Export Data")
    
    if export_format == "CSV":
        csv_data = df_filtered.to_csv(index=False)
        st.download_button(
            label="📄 Download as CSV",
            data=csv_data,
            file_name="curriculum_mapping_180_days.csv",
            mime="text/csv"
        )
    
    elif export_format == "JSON":
        # Convert to a more structured JSON format
        json_data = {
            "school_year": "2025-2026",
            "total_weeks": total_weeks,
            "total_teaching_days": total_teaching_days,
            "mapping_completion": {
                "sda_weeks_mapped": mapped_sda,
                "azcc_days_mapped": mapped_azcc,
                "sda_completion_rate": f"{(mapped_sda/total_weeks*100):.1f}%" if total_weeks > 0 else "0%",
                "azcc_completion_rate": f"{(mapped_azcc/total_teaching_days*100):.1f}%" if total_teaching_days > 0 else "0%"
            },
            "curriculum_mapping": df_filtered.to_dict('records')
        }
        
        json_str = json.dumps(json_data, indent=2)
        st.download_button(
            label="📄 Download as JSON",
            data=json_str,
            file_name="curriculum_mapping_180_days.json",
            mime="application/json"
        )

# Quick stats and insights
st.divider()
st.markdown("### 📈 Mapping Insights")

col_insight1, col_insight2 = st.columns(2)

with col_insight1:
    st.markdown("**Weekly SDA Standards Progress:**")
    sda_progress = (mapped_sda / total_weeks * 100) if total_weeks > 0 else 0
    st.progress(sda_progress / 100)
    st.caption(f"{sda_progress:.1f}% of weeks have SDA standards mapped")

with col_insight2:
    st.markdown("**Daily AZ CC Standards Progress:**")
    azcc_progress = (mapped_azcc / total_teaching_days * 100) if total_teaching_days > 0 else 0
    st.progress(azcc_progress / 100)
    st.caption(f"{azcc_progress:.1f}% of teaching days have AZ CC standards mapped")

# Action items
if sda_progress < 100 or azcc_progress < 100:
    st.warning("🎯 **Action Items:** Visit the School Calendar page to complete your curriculum mapping!")
    
    unmapped_weeks = df[df['SDA_Standard_Weekly'].str.strip() == '']['Week'].apply(lambda x: int(x) if x != '' else None).dropna().unique()
    unmapped_days = df[df['AZ_CC_Standard_Daily'].str.strip() == '']['Day_Number'].tolist()
    
    if len(unmapped_weeks) > 0:
        st.info(f"📝 **Unmapped SDA Weeks:** {', '.join(map(str, sorted(unmapped_weeks)[:10]))}{'...' if len(unmapped_weeks) > 10 else ''}")
    
    if len(unmapped_days) > 0:
        st.info(f"📝 **Unmapped AZ CC Days:** {', '.join(map(str, unmapped_days[:15]))}{'...' if len(unmapped_days) > 15 else ''}")

else:
    st.success("🎉 **Congratulations!** Your curriculum mapping is 100% complete!")

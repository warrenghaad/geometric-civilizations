import streamlit as st
from calendar_generator import SchoolCalendar, save_calendar_to_file, load_calendar_from_file
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="School Calendar", page_icon="📆", layout="wide")

st.title("📆 2025-2026 School Calendar")
st.markdown("### 180 School Days • SDA & AZ CC Standards Mapping")

# Initialize calendar
if 'school_calendar' not in st.session_state:
    # Try to load existing calendar
    calendar_data = load_calendar_from_file()
    
    if calendar_data is None:
        # Generate new calendar
        cal_gen = SchoolCalendar()
        calendar_data = cal_gen.generate_calendar()
        save_calendar_to_file(calendar_data)
        st.session_state.school_calendar = calendar_data
        st.session_state.calendar_generator = cal_gen
    else:
        st.session_state.school_calendar = calendar_data
        st.session_state.calendar_generator = SchoolCalendar()

calendar = st.session_state.school_calendar

# Summary metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total School Days", len(calendar))
with col2:
    teaching_days = [d for d in calendar if d['is_teaching_day']]
    st.metric("Teaching Days (Tue/Thu)", len(teaching_days))
with col3:
    mapped_days = [d for d in calendar if d.get('sda_standard') or d.get('az_cc_standard')]
    st.metric("Days Mapped", len(mapped_days))
with col4:
    total_weeks = max([d['week_number'] for d in calendar])
    st.metric("Total Weeks", total_weeks)

st.divider()

# Navigation controls
col_nav1, col_nav2, col_nav3 = st.columns([2, 2, 1])

with col_nav1:
    # Week selector with default to mid-October
    default_week = st.session_state.calendar_generator.find_current_week(calendar)
    selected_week = st.number_input(
        "Jump to Week",
        min_value=1,
        max_value=total_weeks,
        value=default_week,
        step=1
    )

with col_nav2:
    view_mode = st.radio(
        "View Mode",
        ["All Days", "Teaching Days Only", "By Week", "By Month"],
        horizontal=True
    )

with col_nav3:
    if st.button("🔄 Refresh"):
        st.rerun()

st.divider()

# Filter calendar based on view mode
if view_mode == "Teaching Days Only":
    display_calendar = [d for d in calendar if d['is_teaching_day']]
elif view_mode == "By Week":
    display_calendar = [d for d in calendar if d['week_number'] == selected_week]
elif view_mode == "By Month":
    # Group by month
    months = {}
    for day in calendar:
        date_obj = datetime.strptime(day['date_display'], '%Y-%m-%d')
        month_key = date_obj.strftime('%Y-%m')
        month_name = date_obj.strftime('%B %Y')
        if month_key not in months:
            months[month_key] = {'name': month_name, 'days': []}
        months[month_key]['days'].append(day)
    
    selected_month = st.selectbox(
        "Select Month",
        options=list(months.keys()),
        format_func=lambda x: months[x]['name']
    )
    display_calendar = months[selected_month]['days']
else:
    display_calendar = calendar

# Display mode selector
if view_mode == "By Month":
    display_type = st.radio(
        "Display Type",
        ["Monthly Overview", "Full Mapping Table"],
        horizontal=True
    )
else:
    display_type = st.radio(
        "Display Type",
        ["Table View", "Edit Mode (Week by Week)"],
        horizontal=True
    )

if view_mode == "By Month" and display_type == "Monthly Overview":
    # Monthly overview with complete mapping
    st.markdown(f"### {months[selected_month]['name']} - Complete Curriculum Mapping")
    
    # Group by week within the month
    weeks_in_month = {}
    for day in display_calendar:
        week_num = day['week_number']
        if week_num not in weeks_in_month:
            weeks_in_month[week_num] = []
        weeks_in_month[week_num].append(day)
    
    # Display each week
    for week_num in sorted(weeks_in_month.keys()):
        week_days = weeks_in_month[week_num]
        teaching_days = [d for d in week_days if d['is_teaching_day']]
        
        with st.expander(f"📅 **Week {week_num}** ({week_days[0]['date_display']} to {week_days[-1]['date_display']}) - {len(teaching_days)} teaching days", expanded=True):
            
            if not teaching_days:
                st.info("No teaching days this week")
                continue
            
            # Show teaching days with full mapping
            for day in teaching_days:
                col_date, col_standards, col_content = st.columns([1, 2, 2])
                
                with col_date:
                    st.markdown(f"**{day['date_display']}**")
                    st.caption(f"Day {day['day_number']}")
                
                with col_standards:
                    st.markdown("**Standards Mapped:**")
                    if day.get('sda_standard'):
                        st.markdown(f"🔵 SDA: {day['sda_standard']}")
                    if day.get('az_cc_standard'):
                        st.markdown(f"🟠 AZ CC: {day['az_cc_standard']}")
                    if not day.get('sda_standard') and not day.get('az_cc_standard'):
                        st.caption("_No standards mapped yet_")
                
                with col_content:
                    st.markdown("**Content:**")
                    if day.get('curriculum_objective'):
                        st.markdown(f"📚 {day['curriculum_objective']}")
                    if day.get('historical_content'):
                        st.markdown(f"🏛️ {day['historical_content']}")
                    if not day.get('curriculum_objective') and not day.get('historical_content'):
                        st.caption("_No content mapped yet_")
                
                st.divider()
    
    # Download monthly mapping
    st.divider()
    import json
    month_mapping = {
        'month': months[selected_month]['name'],
        'teaching_days': len([d for d in display_calendar if d['is_teaching_day']]),
        'weeks': {}
    }
    
    for week_num in sorted(weeks_in_month.keys()):
        week_days = [d for d in weeks_in_month[week_num] if d['is_teaching_day']]
        month_mapping['weeks'][f'Week_{week_num}'] = week_days
    
    json_str = json.dumps(month_mapping, indent=2)
    st.download_button(
        label=f"📥 Download {months[selected_month]['name']} Mapping",
        data=json_str,
        file_name=f"mapping_{selected_month}.json",
        mime="application/json"
    )

elif display_type == "Table View" or display_type == "Full Mapping Table":
    # Convert to DataFrame for display
    df = pd.DataFrame(display_calendar)
    
    # Select columns to display
    display_cols = ['day_number', 'date_display', 'week_number', 'is_teaching_day', 
                    'sda_standard', 'az_cc_standard', 'historical_content', 'curriculum_objective']
    
    # Rename for better display
    df_display = df[display_cols].copy()
    df_display.columns = ['Day #', 'Date', 'Week', 'Teaching Day', 
                          'SDA Standard', 'AZ CC Standard', 'Historical Content', 'Curriculum Obj']
    
    # Style teaching days
    def highlight_teaching_days(row):
        if row['Teaching Day']:
            return ['background-color: #e8f4f8'] * len(row)
        return [''] * len(row)
    
    st.dataframe(
        df_display.style.apply(highlight_teaching_days, axis=1),
        use_container_width=True,
        height=600,
        hide_index=True
    )

else:  # Edit Mode
    st.markdown(f"### Editing Week {selected_week}")
    
    week_days = [d for d in calendar if d['week_number'] == selected_week]
    
    if not week_days:
        st.warning(f"No days found for week {selected_week}")
    else:
        st.caption(f"**Week {selected_week}:** {week_days[0]['date_display']} to {week_days[-1]['date_display']}")
        
        # Show each day in the week
        for day_data in week_days:
            day_idx = calendar.index(day_data)
            
            teaching_badge = "🎓 **TEACHING DAY**" if day_data['is_teaching_day'] else ""
            
            with st.expander(
                f"**Day {day_data['day_number']}** - {day_data['date_display']} {teaching_badge}",
                expanded=day_data['is_teaching_day']
            ):
                col_a, col_b = st.columns(2)
                
                with col_a:
                    sda = st.text_area(
                        "SDA Standard",
                        value=day_data.get('sda_standard', ''),
                        key=f"sda_{day_idx}",
                        height=80,
                        placeholder="Enter SDA standard for this day..."
                    )
                    
                    historical = st.text_input(
                        "Historical Content Focus",
                        value=day_data.get('historical_content', ''),
                        key=f"hist_{day_idx}",
                        placeholder="e.g., Ancient Egypt, Islamic Golden Age..."
                    )
                
                with col_b:
                    az_cc = st.text_area(
                        "AZ CC Standard (fill gaps)",
                        value=day_data.get('az_cc_standard', ''),
                        key=f"azcc_{day_idx}",
                        height=80,
                        placeholder="Enter AZ Common Core standard if SDA doesn't speak..."
                    )
                    
                    curriculum = st.text_input(
                        "Curriculum Objective",
                        value=day_data.get('curriculum_objective', ''),
                        key=f"curr_{day_idx}",
                        placeholder="Link to specific objective (e.g., 3.O5)..."
                    )
                
                notes = st.text_area(
                    "Notes",
                    value=day_data.get('notes', ''),
                    key=f"notes_{day_idx}",
                    height=60,
                    placeholder="Planning notes, resources, ideas..."
                )
                
                # Save button for this day
                if st.button(f"💾 Save Day {day_data['day_number']}", key=f"save_{day_idx}"):
                    # Update calendar data
                    st.session_state.school_calendar[day_idx]['sda_standard'] = sda
                    st.session_state.school_calendar[day_idx]['az_cc_standard'] = az_cc
                    st.session_state.school_calendar[day_idx]['historical_content'] = historical
                    st.session_state.school_calendar[day_idx]['curriculum_objective'] = curriculum
                    st.session_state.school_calendar[day_idx]['notes'] = notes
                    
                    # Save to file
                    save_calendar_to_file(st.session_state.school_calendar)
                    
                    st.success(f"Day {day_data['day_number']} saved!")
                    st.rerun()

st.divider()

# Week-by-week summary
st.markdown("### Week-by-Week Overview")

# Group by weeks
weeks_summary = {}
for day in calendar:
    week = day['week_number']
    if week not in weeks_summary:
        weeks_summary[week] = {
            'days': 0,
            'teaching_days': 0,
            'mapped': 0,
            'first_date': day['date_display']
        }
    weeks_summary[week]['days'] += 1
    if day['is_teaching_day']:
        weeks_summary[week]['teaching_days'] += 1
    if day.get('sda_standard') or day.get('az_cc_standard'):
        weeks_summary[week]['mapped'] += 1

# Display weeks in columns
weeks_list = sorted(weeks_summary.keys())
num_cols = 4
cols = st.columns(num_cols)

for idx, week_num in enumerate(weeks_list):
    with cols[idx % num_cols]:
        week_info = weeks_summary[week_num]
        completion = (week_info['mapped'] / week_info['days'] * 100) if week_info['days'] > 0 else 0
        
        status_emoji = "✅" if completion == 100 else "📝" if completion > 0 else "⚪"
        
        st.metric(
            f"{status_emoji} Week {week_num}",
            f"{week_info['teaching_days']} teaching days",
            f"{int(completion)}% mapped"
        )
        st.caption(week_info['first_date'])

st.divider()

# Export options
st.markdown("### Export Calendar")
col_exp1, col_exp2 = st.columns(2)

with col_exp1:
    if st.button("📥 Download as CSV"):
        df_export = pd.DataFrame(calendar)
        csv = df_export.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="school_calendar_2025_2026.csv",
            mime="text/csv"
        )

with col_exp2:
    if st.button("📥 Download as JSON"):
        import json
        json_str = json.dumps(calendar, indent=2)
        st.download_button(
            label="Download JSON",
            data=json_str,
            file_name="school_calendar_2025_2026.json",
            mime="application/json"
        )

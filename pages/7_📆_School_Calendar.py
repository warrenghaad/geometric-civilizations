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
        ["All Days", "Teaching Days Only", "By Week"],
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
else:
    display_calendar = calendar

# Display mode selector
display_type = st.radio(
    "Display Type",
    ["Table View", "Edit Mode (Week by Week)"],
    horizontal=True
)

if display_type == "Table View":
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

import streamlit as st
from calendar_generator import load_calendar_from_file
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="School Building Navigator", page_icon="🏫", layout="wide")

st.title("🏫 School Building Navigator")
st.markdown("### Open Floor Plan: See Across Grades & Through Weeks")

st.markdown("""
**Navigate your curriculum like a school building:**
- **Rooms** = Individual grades (K→8)
- **Hallways** = Horizontal time (weeks across all grades)
- **Plumbing** = Vertical standards (concepts building K→8)
- **Wiring** = Cognitive domains (messy network overlay)
- **Students** = Objectives placed in grade-week cells
- **Gaps** = Empty cells needing standards/objectives
""")

# Load calendar
calendar = load_calendar_from_file()
if not calendar:
    st.error("Calendar not found. Please generate it first from the School Calendar page.")
    st.stop()

# Convert to DataFrame for analysis
df = pd.DataFrame(calendar)

# Calculate weeks (assuming ~5 school days per week)
df['week_estimate'] = ((df['day_number'] - 1) // 5) + 1
max_week = df['week_estimate'].max()

st.divider()

# Control panel
col1, col2, col3 = st.columns(3)

with col1:
    view_mode = st.selectbox(
        "View Mode",
        ["Gap Analysis", "Plumbing (Vertical Standards)", "Wiring (Cognitive Domains)", "Students (Objectives)"]
    )

with col2:
    grade_filter = st.multiselect(
        "Filter Grades",
        ["K", "1", "2", "3", "4", "5", "6", "7", "8"],
        default=["K", "1", "2", "3", "4", "5", "6", "7", "8"]
    )

with col3:
    week_range = st.slider(
        "Week Range",
        min_value=1,
        max_value=int(max_week),
        value=(1, min(12, int(max_week))),
        step=1
    )

st.divider()

# Create grade-week grid data structure
grades = ["K", "1", "2", "3", "4", "5", "6", "7", "8"]
weeks = list(range(week_range[0], week_range[1] + 1))

# Initialize grid
grid_data = {
    'grade': [],
    'week': [],
    'has_sda': [],
    'has_azcc': [],
    'has_objective': [],
    'has_historical': [],
    'completion_score': [],
    'status': []
}

# Populate grid (simplified - you'd map your actual objectives by grade)
for grade in grades:
    if grade not in grade_filter:
        continue
    
    for week in weeks:
        # Find calendar days for this week
        week_days = df[df['week_estimate'] == week]
        
        # For now, check if ANY day in this week has mappings
        # (You'll enhance this to check grade-specific objectives)
        has_sda = any(week_days['sda_standard'] != '')
        has_azcc = any(week_days['az_cc_standard'] != '')
        has_obj = any(week_days['curriculum_objective'] != '')
        has_hist = any(week_days['historical_content'] != '')
        
        # Calculate completion
        completion = sum([has_sda, has_azcc, has_obj, has_hist]) / 4 * 100
        
        # Determine status
        if completion == 0:
            status = 'Empty (Gap)'
        elif has_sda and has_obj:
            status = 'Complete'
        elif has_sda:
            status = 'SDA Mapped'
        elif has_azcc:
            status = 'AZ CC Fill'
        else:
            status = 'Partial'
        
        grid_data['grade'].append(grade)
        grid_data['week'].append(week)
        grid_data['has_sda'].append(has_sda)
        grid_data['has_azcc'].append(has_azcc)
        grid_data['has_objective'].append(has_obj)
        grid_data['has_historical'].append(has_hist)
        grid_data['completion_score'].append(completion)
        grid_data['status'].append(status)

grid_df = pd.DataFrame(grid_data)

if view_mode == "Gap Analysis":
    st.markdown("### 📊 Curriculum Coverage: Gaps Highlighted")
    
    # Create heatmap showing gaps
    pivot_completion = grid_df.pivot(index='grade', columns='week', values='completion_score')
    
    # Create 3D bar chart or heatmap
    fig = go.Figure(data=go.Heatmap(
        z=pivot_completion.values,
        x=pivot_completion.columns,
        y=pivot_completion.index,
        colorscale=[
            [0, '#ff4444'],      # Red = Empty gap
            [0.25, '#ffaa44'],   # Orange = Partial
            [0.5, '#ffff44'],    # Yellow = AZ CC fill
            [0.75, '#44ff44'],   # Green = SDA mapped
            [1.0, '#4444ff']     # Blue = Complete
        ],
        hovertemplate='Grade: %{y}<br>Week: %{x}<br>Completion: %{z:.0f}%<extra></extra>',
        colorbar=dict(
            title="Completion %",
            tickvals=[0, 25, 50, 75, 100],
            ticktext=['Empty', 'Partial', 'AZ CC', 'SDA', 'Complete']
        )
    ))
    
    fig.update_layout(
        title="Open Floor Plan: Grade-Week Grid (Red = Gaps to Fill)",
        xaxis_title="Week Number →",
        yaxis_title="Grade →",
        height=600,
        xaxis=dict(side='bottom'),
        yaxis=dict(autorange='reversed')
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Gap statistics
    st.markdown("### Gap Statistics")
    col_a, col_b, col_c, col_d = st.columns(4)
    
    with col_a:
        empty_cells = len(grid_df[grid_df['status'] == 'Empty (Gap)'])
        st.metric("Empty Cells (Gaps)", empty_cells)
    
    with col_b:
        azcc_fills = len(grid_df[grid_df['status'] == 'AZ CC Fill'])
        st.metric("AZ CC Fills", azcc_fills)
    
    with col_c:
        sda_mapped = len(grid_df[grid_df['status'].isin(['SDA Mapped', 'Complete'])])
        st.metric("SDA Mapped", sda_mapped)
    
    with col_d:
        complete_cells = len(grid_df[grid_df['status'] == 'Complete'])
        st.metric("Complete Cells", complete_cells)

elif view_mode == "Plumbing (Vertical Standards)":
    st.markdown("### 🔧 Plumbing: Vertical Standards Building K→8")
    st.info("Coming soon: Show how concepts like 'pattern recognition' or 'geometric reasoning' build vertically through grades")
    
    # Placeholder visualization
    st.markdown("""
    **Vertical Standard Shafts:**
    - Pattern Recognition: K (spot) → 1 (extend) → 2 (explain rule) → 3 (classify) → ... → 8 (prove)
    - Geometric Reasoning: K (name shapes) → 1 (compose) → 2 (partition) → 3 (classify quadrilaterals) → ... → 8 (transformations)
    - Myth Analysis: K (retell) → 1 (compare) → 2 (sequence events) → 3 (extract theme) → ... → 8 (structural analysis)
    """)

elif view_mode == "Wiring (Cognitive Domains)":
    st.markdown("### ⚡ Wiring: Cognitive Domain Network")
    st.info("Coming soon: Show which cognitive domains are activated across the grade-week grid")
    
    st.markdown("""
    **Cognitive Domain Overlay:**
    - Attention (focus & shifting)
    - Memory (working, episodic, semantic)
    - Executive Functions (planning, flexibility, inhibition)
    - Language (vocabulary, syntax, discourse)
    - Learning (skill acquisition, feedback)
    - Visuospatial Processing (mental rotation, navigation)
    - Social Cognition (theory of mind, empathy)
    - Emotional Processing (regulation, integration)
    - Metacognition (self-monitoring, reflection)
    """)

else:  # Students (Objectives)
    st.markdown("### 👥 Students: Objectives Placed in Rooms")
    st.info("Coming soon: Show individual objectives placed in their grade-week locations")

st.divider()

# Detail view for selected cell
st.markdown("### 🔍 Drill Into a Cell")

col_detail1, col_detail2 = st.columns(2)

with col_detail1:
    selected_grade = st.selectbox("Select Grade", grades)

with col_detail2:
    selected_week = st.selectbox("Select Week", weeks)

# Find data for selected cell
cell_data = grid_df[(grid_df['grade'] == selected_grade) & (grid_df['week'] == selected_week)]

if not cell_data.empty:
    cell_info = cell_data.iloc[0]
    
    st.markdown(f"### Grade {selected_grade}, Week {selected_week}")
    
    col_status1, col_status2, col_status3 = st.columns(3)
    
    with col_status1:
        st.metric("Status", cell_info['status'])
    
    with col_status2:
        st.metric("Completion", f"{cell_info['completion_score']:.0f}%")
    
    with col_status3:
        days_in_week = df[df['week_estimate'] == selected_week]
        teaching_days = days_in_week[days_in_week['is_teaching_day']]
        st.metric("Teaching Days This Week", len(teaching_days))
    
    # Show what needs to be filled
    st.markdown("#### What's Missing:")
    missing = []
    if not cell_info['has_sda']:
        missing.append("❌ SDA Standard")
    else:
        missing.append("✅ SDA Standard")
    
    if not cell_info['has_azcc']:
        missing.append("❌ AZ CC Standard (if needed)")
    else:
        missing.append("✅ AZ CC Standard")
    
    if not cell_info['has_objective']:
        missing.append("❌ Curriculum Objective")
    else:
        missing.append("✅ Curriculum Objective")
    
    if not cell_info['has_historical']:
        missing.append("❌ Historical Content")
    else:
        missing.append("✅ Historical Content")
    
    for item in missing:
        st.markdown(item)
    
    if st.button("📝 Go to School Calendar to Edit This Week"):
        st.info(f"Navigate to the School Calendar page and jump to Week {selected_week}")

else:
    st.warning("No data for selected cell")

st.divider()
st.caption("💡 Red cells = gaps to fill. Navigate to School Calendar page to map SDA standards, fill with AZ CC, and link objectives.")

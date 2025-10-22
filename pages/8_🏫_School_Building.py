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
    st.markdown("### 📊 Open Floor Plan: Color by Subject")
    st.caption("Math = Blue | Arts = Purple | Mythology = Orange | Power = Red | Mixed = Green | Empty = Gray")
    
    # For now, assign subjects randomly (you'll map this from actual objectives)
    # This is placeholder - replace with actual variable mapping from objectives
    import random
    random.seed(42)
    
    subject_colors = {
        'Empty': 0,
        'Math': 1,
        'Arts': 2, 
        'Mythology': 3,
        'Power': 4,
        'Mixed': 5
    }
    
    # Assign subjects to grid (placeholder logic)
    grid_df['primary_subject'] = grid_df.apply(
        lambda row: 'Empty' if row['status'] == 'Empty (Gap)' 
        else random.choice(['Math', 'Arts', 'Mythology', 'Power', 'Mixed']),
        axis=1
    )
    grid_df['subject_code'] = grid_df['primary_subject'].map(subject_colors)
    
    # Create heatmap colored by subject
    pivot_subjects = grid_df.pivot(index='grade', columns='week', values='subject_code')
    
    fig = go.Figure(data=go.Heatmap(
        z=pivot_subjects.values,
        x=pivot_subjects.columns,
        y=pivot_subjects.index,
        colorscale=[
            [0, '#cccccc'],      # Gray = Empty
            [0.2, '#4472C4'],    # Blue = Math
            [0.4, '#9966CC'],    # Purple = Arts
            [0.6, '#FF8C42'],    # Orange = Mythology
            [0.8, '#E74C3C'],    # Red = Power
            [1.0, '#52C41A']     # Green = Mixed variables
        ],
        hovertemplate='Grade: %{y}<br>Week: %{x}<br>Subject: %{z}<extra></extra>',
        colorbar=dict(
            title="Subject",
            tickvals=[0, 1, 2, 3, 4, 5],
            ticktext=['Empty', 'Math', 'Arts', 'Mythology', 'Power', 'Mixed']
        ),
        showscale=True
    ))
    
    fig.update_layout(
        title="Open Floor Plan: No Walls - See All Subjects Across Grades & Weeks",
        xaxis_title="Week Number (Hallway) →",
        yaxis_title="Grade (Floor) →",
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
    st.caption("Shows how standards progress vertically through grades like plumbing shafts")
    
    # Define vertical standard progressions
    vertical_standards = {
        'Pattern Recognition': {
            'K': 'Spot repeating patterns',
            '1': 'Extend patterns',
            '2': 'Explain pattern rules',
            '3': 'Classify pattern families',
            '4': 'Create complex patterns',
            '5': 'Generalize pattern rules',
            '6': 'Algebraic patterns',
            '7': 'Pattern sequences',
            '8': 'Prove pattern properties'
        },
        'Geometric Reasoning': {
            'K': 'Name basic shapes',
            '1': 'Compose shapes',
            '2': 'Partition shapes',
            '3': 'Classify quadrilaterals',
            '4': 'Angle measurement',
            '5': 'Coordinate plane',
            '6': 'Area formulas',
            '7': 'Scale & similarity',
            '8': 'Transformations & proof'
        },
        'Myth Analysis': {
            'K': 'Retell simple myth',
            '1': 'Compare two myths',
            '2': 'Sequence story events',
            '3': 'Extract theme/moral',
            '4': 'Character analysis',
            '5': 'Cross-cultural motifs',
            '6': 'Archetypal patterns',
            '7': 'Structural analysis',
            '8': 'Critical interpretation'
        },
        'Writing Development': {
            'K': 'Label & draw',
            '1': '3-sentence story',
            '2': 'Topic sentence',
            '3': 'Paragraph structure',
            '4': 'Multi-paragraph essay',
            '5': 'Thesis & evidence',
            '6': 'Analytical writing',
            '7': 'Research synthesis',
            '8': 'Argumentative essay'
        }
    }
    
    selected_standard = st.selectbox("Select Vertical Standard", list(vertical_standards.keys()))
    
    progression = vertical_standards[selected_standard]
    
    # Create vertical flow visualization
    grades_list = ['K', '1', '2', '3', '4', '5', '6', '7', '8']
    
    cols = st.columns(9)
    for idx, grade in enumerate(grades_list):
        with cols[idx]:
            st.markdown(f"**{grade}**")
            if grade in progression:
                st.info(progression[grade])
            else:
                st.caption("—")
            if idx < 8:
                st.markdown("↓")
    
    st.divider()
    
    # Show all standards as heatmap
    st.markdown("#### All Vertical Standards Across Grades")
    
    # Create matrix
    standard_matrix = []
    for standard_name in vertical_standards.keys():
        row = []
        for grade in grades_list:
            if grade in vertical_standards[standard_name]:
                row.append(1)  # Has progression defined
            else:
                row.append(0)  # Gap
        standard_matrix.append(row)
    
    fig = go.Figure(data=go.Heatmap(
        z=standard_matrix,
        x=grades_list,
        y=list(vertical_standards.keys()),
        colorscale=[[0, '#eeeeee'], [1, '#4472C4']],
        showscale=False,
        hovertemplate='Standard: %{y}<br>Grade: %{x}<extra></extra>'
    ))
    
    fig.update_layout(
        title="Plumbing Shafts: Vertical Standard Coverage",
        xaxis_title="Grade →",
        yaxis_title="Standard Progression ↓",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

elif view_mode == "Wiring (Cognitive Domains)":
    st.markdown("### ⚡ Wiring: Cognitive Domain Network")
    st.caption("Messy network showing which cognitive domains are activated where")
    
    cognitive_domains = [
        "Attention",
        "Memory", 
        "Executive Functions",
        "Language",
        "Learning",
        "Visuospatial Processing",
        "Social Cognition",
        "Emotional Processing",
        "Metacognition"
    ]
    
    selected_domain = st.selectbox("Select Cognitive Domain to Highlight", cognitive_domains)
    
    # Domain descriptions
    domain_info = {
        "Attention": "Selecting and maintaining focus, shifting attention, divided attention",
        "Memory": "Working memory, episodic (events), semantic (facts), procedural (skills)",
        "Executive Functions": "Planning, problem-solving, flexibility, inhibition, decision-making",
        "Language": "Vocabulary, grammar, syntax, pragmatics, discourse comprehension",
        "Learning": "Skill acquisition, associative learning, practice, feedback integration",
        "Visuospatial Processing": "Mental rotation, spatial relationships, navigation, construction",
        "Social Cognition": "Theory of mind, emotion recognition, perspective-taking, empathy",
        "Emotional Processing": "Emotion identification, regulation, integration with cognition",
        "Metacognition": "Self-monitoring, strategy selection, reflection on thinking"
    }
    
    st.info(f"**{selected_domain}:** {domain_info[selected_domain]}")
    
    # Create activation heatmap (placeholder - will be filled from actual objective tags)
    import numpy as np
    np.random.seed(42)
    
    # Simulate domain activation intensity across grade-week grid
    activation_data = []
    for grade in grades:
        row = []
        for week in weeks:
            # Higher activation for certain domains in certain contexts
            if selected_domain == "Visuospatial Processing" and grade in ['K', '1', '2', '3']:
                intensity = np.random.choice([0, 2, 3], p=[0.3, 0.4, 0.3])
            elif selected_domain == "Social Cognition" and grade in ['6', '7', '8']:
                intensity = np.random.choice([0, 2, 3], p=[0.2, 0.3, 0.5])
            elif selected_domain == "Metacognition" and grade in ['5', '6', '7', '8']:
                intensity = np.random.choice([0, 1, 2, 3], p=[0.2, 0.3, 0.3, 0.2])
            else:
                intensity = np.random.choice([0, 1, 2, 3], p=[0.4, 0.3, 0.2, 0.1])
            row.append(intensity)
        activation_data.append(row)
    
    fig = go.Figure(data=go.Heatmap(
        z=activation_data,
        x=weeks,
        y=grades,
        colorscale=[
            [0, '#ffffff'],      # White = Not activated
            [0.33, '#ffeeaa'],   # Light yellow = Low activation
            [0.66, '#ffaa44'],   # Orange = Medium activation
            [1.0, '#ff4444']     # Red = High activation
        ],
        hovertemplate=f'{selected_domain}<br>Grade: %{{y}}<br>Week: %{{x}}<br>Intensity: %{{z}}<extra></extra>',
        colorbar=dict(
            title="Activation",
            tickvals=[0, 1, 2, 3],
            ticktext=['None', 'Low', 'Med', 'High']
        )
    ))
    
    fig.update_layout(
        title=f"Wiring: {selected_domain} Activation Across Building",
        xaxis_title="Week →",
        yaxis_title="Grade →",
        height=500,
        yaxis=dict(autorange='reversed')
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.caption("💡 Intensity reflects how heavily this cognitive domain is engaged in that grade-week cell. Map objectives with cognitive domain tags to see actual activation patterns.")

else:  # Students (Objectives)
    st.markdown("### 👥 Students: Objectives Placed in Grade-Week Rooms")
    st.caption("See individual learning objectives distributed across the building")
    
    # Load objectives from graph data
    from graph_manager import GraphManager
    from data_store import DataStore
    
    if 'graph_manager' not in st.session_state:
        st.session_state.graph_manager = GraphManager()
        st.session_state.data_store = DataStore()
        st.session_state.graph_manager.load_from_store(st.session_state.data_store)
    
    all_nodes = st.session_state.graph_manager.get_all_nodes()
    
    # Group objectives by grade
    objectives_by_grade = {}
    for grade in grades:
        grade_objs = [n for n in all_nodes if f"{grade}.O" in n]
        objectives_by_grade[grade] = grade_objs
    
    # Display objective counts per grade
    st.markdown("#### Objective Distribution")
    
    obj_counts = [len(objectives_by_grade.get(g, [])) for g in grades]
    
    fig = go.Figure(data=[
        go.Bar(
            x=grades,
            y=obj_counts,
            marker_color='#4472C4',
            text=obj_counts,
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title="Students (Objectives) per Grade",
        xaxis_title="Grade",
        yaxis_title="Number of Objectives",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Show sample objectives
    st.markdown("#### Sample Objectives by Grade")
    
    selected_grade_view = st.selectbox("View objectives for grade:", grades, key='student_view')
    
    grade_objectives = objectives_by_grade.get(selected_grade_view, [])
    
    if grade_objectives:
        st.markdown(f"**{len(grade_objectives)} objectives** found for Grade {selected_grade_view}")
        
        for obj_name in grade_objectives[:10]:  # Show first 10
            node_data = st.session_state.graph_manager.get_node_data(obj_name)
            
            with st.expander(f"📝 {obj_name}"):
                st.markdown(node_data.get('description', 'No description'))
                
                col_obj1, col_obj2 = st.columns(2)
                with col_obj1:
                    if node_data.get('dimensional_level'):
                        st.caption(f"**Dimension:** {node_data['dimensional_level']}")
                with col_obj2:
                    if node_data.get('variables'):
                        st.caption(f"**Variables:** {', '.join(node_data['variables'])}")
        
        if len(grade_objectives) > 10:
            st.caption(f"... and {len(grade_objectives) - 10} more objectives")
    else:
        st.info(f"No objectives loaded yet for Grade {selected_grade_view}. Use Manage Content to add them.")

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

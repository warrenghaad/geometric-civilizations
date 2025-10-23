import streamlit as st
from calendar_generator import load_calendar_from_file
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="Narrative Arc", page_icon="📖", layout="wide")

st.title("📖 Curriculum Narrative Arc")
st.markdown("### Subject Flow Through the School Year")

st.markdown("""
This view shows the **narrative arc** of subjects across four key moments in the school year:
- **Beginning** (Weeks 1-9)
- **Middle Point 1** (Weeks 10-18)
- **Middle Point 2** (Weeks 19-27)
- **End** (Weeks 28-36)
""")

# Load calendar
calendar_data = load_calendar_from_file()

if calendar_data is None:
    st.error("No calendar data found. Please visit the School Calendar page to generate it.")
    st.stop()

# Define the four arc points
arc_points = {
    "Beginning\n(Weeks 1-9)": {"weeks": range(1, 10), "color": "#4472C4"},
    "Middle 1\n(Weeks 10-18)": {"weeks": range(10, 19), "color": "#ED7D31"},
    "Middle 2\n(Weeks 19-27)": {"weeks": range(19, 28), "color": "#A5A5A5"},
    "End\n(Weeks 28-36)": {"weeks": range(28, 37), "color": "#FFC000"}
}

st.divider()

# Create visual timeline
st.markdown("### Timeline Overview")

fig_timeline = go.Figure()

# Add arc line
x_points = [0, 1, 2, 3]
y_points = [0, 2, 2, 0]  # Arc shape
labels = list(arc_points.keys())
colors_list = [arc_points[label]["color"] for label in labels]

fig_timeline.add_trace(go.Scatter(
    x=x_points,
    y=y_points,
    mode='lines+markers',
    line=dict(color='#666', width=3),
    marker=dict(size=20, color=colors_list),
    text=labels,
    hovertemplate='%{text}<extra></extra>',
    showlegend=False
))

fig_timeline.update_layout(
    height=300,
    xaxis=dict(
        showticklabels=False,
        showgrid=False,
        zeroline=False
    ),
    yaxis=dict(
        showticklabels=False,
        showgrid=False,
        zeroline=False
    ),
    plot_bgcolor='white',
    margin=dict(l=20, r=20, t=20, b=20)
)

st.plotly_chart(fig_timeline, use_container_width=True)

st.divider()

# Display each arc point
for point_name, point_data in arc_points.items():
    with st.expander(f"📚 {point_name}", expanded=True):
        
        # Get days in this range
        days_in_range = [d for d in calendar_data if d['week_number'] in point_data['weeks']]
        sda_days = [d for d in days_in_range if d['is_teaching_day']]
        
        col1, col2, col3 = st.columns([1, 2, 2])
        
        with col1:
            st.markdown(f"**📅 Weeks:** {min(point_data['weeks'])}-{max(point_data['weeks'])}")
            st.markdown(f"**📖 SDA Lessons:** {len(sda_days)}")
            st.markdown(f"**📝 Total Days:** {len(days_in_range)}")
        
        with col2:
            st.markdown("**Subject Focus:**")
            
            # Placeholder subject themes (you'll customize these)
            if "Beginning" in point_name:
                st.markdown("""
                - 📐 **Math**: Foundational patterns, number sense
                - 🎨 **Arts**: Introduction to design elements
                - 📖 **Mythology**: Creation stories, origin myths
                - ⚡ **Power**: Classroom community building
                """)
            elif "Middle 1" in point_name:
                st.markdown("""
                - 📐 **Math**: Geometric reasoning, transformations
                - 🎨 **Arts**: Cultural aesthetics, symbolism
                - 📖 **Mythology**: Hero's journey, character analysis
                - ⚡ **Power**: Resource allocation in ancient societies
                """)
            elif "Middle 2" in point_name:
                st.markdown("""
                - 📐 **Math**: Measurement, scale, proportion
                - 🎨 **Arts**: Architectural design, sacred geometry
                - 📖 **Mythology**: Cross-cultural motifs, comparative analysis
                - ⚡ **Power**: Gatekeeping knowledge, social hierarchies
                """)
            else:  # End
                st.markdown("""
                - 📐 **Math**: Synthesis - patterns across cultures
                - 🎨 **Arts**: Integration project, portfolio review
                - 📖 **Mythology**: Meta-analysis, storytelling traditions
                - ⚡ **Power**: Innovation, invention, legacy
                """)
        
        with col3:
            st.markdown("**Narrative Theme:**")
            
            if "Beginning" in point_name:
                st.info("**Foundation & Discovery**\n\nStudents build foundational understanding and begin exploring cultural patterns.")
            elif "Middle 1" in point_name:
                st.info("**Development & Connection**\n\nDeeper analysis emerges as students connect ideas across variables.")
            elif "Middle 2" in point_name:
                st.info("**Complexity & Synthesis**\n\nMultiple perspectives reveal sophisticated cultural systems.")
            else:  # End
                st.info("**Integration & Invention**\n\nAll variables align - students demonstrate mastery through innovation.")
        
        # Show sample mapped days
        st.markdown("**Sample Mapped Content:**")
        
        mapped_days = [d for d in sda_days[:3] if d.get('sda_standard') or d.get('curriculum_objective')]
        
        if mapped_days:
            for day in mapped_days:
                st.caption(f"**{day['date_display']}** - {day.get('sda_standard', day.get('curriculum_objective', 'Not mapped'))}")
        else:
            st.caption("_No content mapped yet for this period. Use School Calendar to add._")

st.divider()

# Visualization of subject distribution across arc
st.markdown("### Subject Distribution Across Year")

# Count subjects per arc point (placeholder data)
subjects = ["Math", "Arts", "Mythology", "Power"]
arc_names = list(arc_points.keys())

fig_dist = go.Figure()

for subject in subjects:
    # Placeholder - in real version, would count from actual mapped objectives
    if subject == "Math":
        values = [15, 18, 20, 16]
    elif subject == "Arts":
        values = [14, 17, 18, 18]
    elif subject == "Mythology":
        values = [16, 16, 17, 19]
    else:  # Power
        values = [12, 14, 15, 18]
    
    fig_dist.add_trace(go.Bar(
        name=subject,
        x=arc_names,
        y=values,
        text=values,
        textposition='auto'
    ))

fig_dist.update_layout(
    barmode='group',
    height=400,
    xaxis_title="",
    yaxis_title="Number of Lessons",
    showlegend=True
)

st.plotly_chart(fig_dist, use_container_width=True)

st.divider()

st.info("""
💡 **Customize Your Narrative Arc:**
1. Map SDA standards and objectives in the School Calendar
2. Tag them with Variables (Math, Arts, Mythology, Power)
3. This page will automatically show the narrative flow through the year
4. Use this to ensure balanced coverage and meaningful progression
""")

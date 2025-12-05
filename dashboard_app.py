import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Student Wellbeing Analysis", page_icon="🏫", layout="wide"
)


@st.cache_data
def load_and_prepare_data():
    df = pd.read_csv(
        r"C:\Users\Eni-o\OneDrive\Desktop\Kanyin\CI_Data_Analytics_Bootcamp\Group_Project\social_mental_health_project\data\socialmedia_clean.csv"
    )

    # wellbeing score
    df["Wellbeing_Score"] = (
        df["Happiness_Index(1-10)"]
        + df["Sleep_Quality(1-10)"]
        + df["Exercise_Frequency(week)"]
        + (11 - df["Stress_Level(1-10)"])
    )

    # bins
    df["Age_Group"] = pd.cut(
        df["Age"],
        bins=[15, 20, 25, 35, 49],
        labels=["Teen", "Young Adult", "Adult", "Older Adult"],
    )
    df["Days_Bin"] = pd.cut(
        df["Days_Without_Social_Media"],
        bins=[-0.1, 0, 2, 4, 7],
        labels=["0", "1-2", "3-4", "5-7"],
    )
    return df


df = load_and_prepare_data()

# Title and description
st.title("Student Wellbeing Analysis 🏫")
st.write(
    """
This analysis explores how digital habits and lifestyle factors influence student wellbeing.

- We examine key social media variables, including daily screen time, platform usage, and breaks from social media, to understand their impact on
overall student health and happiness.
- Wellness factors such as sleep quality, stress levels, and exercise frequency are also analysed to provide a broader view of wellbeing.
- We also consider personal demographics like age and gender to identify trends and see whether they influence wellbeing outcomes.

The goal is to uncover insights that can help improve student wellbeing in the digital age.
"""
)

# Sidebar filters
st.sidebar.markdown("## Filter Data")
gender = st.sidebar.selectbox(
    "Gender", ["All"] + sorted(df["Gender"].unique().tolist())
)

age_group = st.sidebar.selectbox(
    "Age Group", ["All"] + [str(x) for x in df["Age_Group"].cat.categories]
)

dff = df.copy()
if gender != "All":
    dff = dff[dff["Gender"] == gender]

if age_group != "All":
    dff = dff[dff["Age_Group"] == age_group]

# Tabs
tab1, tab2, tab3 = st.tabs(["Overview", "Question 1", "Question 2"])


with tab1:
    st.header("Overview of Student Wellbeing and Social Media Usage")
    st.write(
        """This section provides a general overview of the dataset. It gives a better understaning of the feautures present by
        highlighting key statistics, and a easy view of the dataset."""
    )
    st.markdown("---")

    # Basic statistics
    st.subheader("Statistics")
    st.write("Here are some basic statistics of the filtered dataset:")
    st.write(dff.describe())

    # Raw data display
    st.header("Raw Data")
    st.dataframe(df)

    # Download button
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download Filtered Data",
        data=csv,
        file_name="filtered_divorce_data.csv",
        mime="text/csv",
    )

with tab2:
    st.header("Impact of Days Without Social Media on Wellbeing")
    st.write(
        "Q1. To what extent is the number of Days_Without_Social_Media related to an individual's overall Wellbeing_Score?"
    )
    st.markdown("---")

    # Scatter
    st.subheader("Days without social media vs Wellbeing Score")
    fig1 = px.scatter(
        dff,
        x="Days_Without_Social_Media",
        y="Wellbeing_Score",
        color="Social_Media_Platform",
        hover_data=["User_ID", "Age", "Gender", "Daily_Screen_Time(hrs)"],
    )
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown(
        """##### Scatter Plot - Key Insights:
- There is no clear positive or negative linear trend in the data. The dots are scattered vertically across all detox durations (0 to 9 days).
This suggests that the number of days without social media alone is not a strong predictor of the highest or lowest Wellbeing Scores.
- High wellbeing scores are achieved by users across the entire spectrum of detox, but are most present between 2-5 days of social media.
- LinkedIn users (dark blue dots) have the widest spread of of days off social media, ranging from 0 to 9 days, indicating diverse usage patterns
among its users.
- Whilst LinkedIn users display the shortest range of days off social media (0-6 days)."""
    )

    # Box
    st.subheader("Wellbeing distribution by Days (binned)")
    fig2 = px.box(dff, x="Days_Bin", y="Wellbeing_Score", color="Days_Bin")
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown(
        """##### Wellbeing Distribution by Detox Bin - Key Insights:
- The 3-4 and 5-7 day detox bins shows the highest median wellbeing score (22), meaning typically users in these groups reported the best score.
- The 3-4 day and 5-7 day bins have the tightest distribution (smallest interquartile range), indicating that wellbeing scores are the most
predictable and consistent during these moderate detox periods.
- The median scores for all detox periods (1-7 days) are slightly higher than the 0-day bin, suggesting taking any social media break tends to
improve the typical wellbeing level."""
    )

    # Stacked bar
    st.subheader("Mean wellbeing components by individual days without social media")

    comps = (
        dff.groupby("Days_Without_Social_Media")
        .agg(
            {
                "Happiness_Index(1-10)": "mean",
                "Sleep_Quality(1-10)": "mean",
                "Exercise_Frequency(week)": "mean",
                "Stress_Level(1-10)": "mean",
            }
        )
        .reset_index()
        .dropna()
    )

    if not comps.empty:
        # Convert stress so higher = better
        comps["Stress_inverse"] = 11 - comps["Stress_Level(1-10)"]

        # Melt for stacked bar formatting
        comps_plot = comps[
            [
                "Days_Without_Social_Media",
                "Happiness_Index(1-10)",
                "Sleep_Quality(1-10)",
                "Exercise_Frequency(week)",
                "Stress_inverse",
            ]
        ].melt(
            id_vars="Days_Without_Social_Media",
            var_name="component",
            value_name="Wellbeing_Mean_Values",
        )

        # Plot stacked bar
        fig3 = px.bar(
            comps_plot,
            x="Days_Without_Social_Media",
            y="Wellbeing_Mean_Values",
            color="component",
            barmode="stack",
        )

        st.plotly_chart(fig3, use_container_width=True)

    else:
        st.write("No data for the chosen filters.")
    st.markdown(
        """##### Overall Wellbeing Score - Key Insights:
- The total wellbeing average is highest for users who take a moderate break of 4 to 6 days without social media.
- There's no immediate, dramatic improvement during the first 1 to 3 days compared to 0 days off.
- The overall score significantly decreases at the longest detox durations (8 and 9 days), suggesting potential negative side effects
(like isolation) or that these users have other underlining issues."""
    )

with tab3:
    st.header(
        "User Profiles on Social Media Platforms and How They Compare in Daily Screen Time"
    )
    st.write("Q2. What is the typical Age and Gender profile for users of different Social_Media_Platform, and how does their average"
             " Daily_Screen_Time compare?")
    st.markdown("---")

    # Scatter
    st.subheader("Daily Screen Time vs Age")
    fig1 = px.scatter(
        dff,
        x="Daily_Screen_Time(hrs)",
        y="Age",
        color="Social_Media_Platform",
        hover_data=["User_ID", "Gender", "Wellbeing_Score"],
        size="Daily_Screen_Time(hrs)",
    )
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown(
        """##### Scatter Plot - Key Insights:
At first glance, the scatter plot appears quite dispersed, making it difficult to identify strong patterns due to the wide spread across both
age and screen-time values. However, examining the extremes of the x-axis reveals some useful observations:
- **High Screen Time Users (8-11 hrs):**
Most platforms show only a small cluster of users in this range (around five to six points each).
Instagram, however, stands out with the largest concentration of high-screen-time users, around nine users fall between 7.5 and 11 hours per day.
This suggests that Instagram users are more likely to have longer daily screen-time hours compared to users of other platforms.
- **Low Screen Time Users (0-2 hrs):**
This range is mainly occupied by users of LinkedIn and Twitter. Age does not show any clear trend here, the points are scattered
across different age groups. From young adults to older adults, there are users with low screen time on these platforms.""")

    # Aggregation for sunburst
    agg_df = (
        dff.groupby(["Age_Group", "Gender", "Social_Media_Platform"])
        .agg(
            user_count=("Age", "size"),
            avg_screen_time=("Daily_Screen_Time(hrs)", "mean"),
        )
        .reset_index()
    )

    # Sunburst
    st.subheader("Profile Hierarchy: Age Group → Gender → Social Media Platform")
    try:
        fig = px.sunburst(
            agg_df,
            path=["Age_Group", "Gender", "Social_Media_Platform"],
            values="user_count",  # Size of the slice is the number of users
            color="avg_screen_time",  # Color is determined by the average screen time
            color_continuous_scale="Plasma",
            title="Wellbeing Components by Days Without Social Media",
            height=650,
        )

        fig.update_traces(
            hovertemplate="<b>%{label}</b><br>Count: %{value}<br>Avg Screen Time: %{color:.2f} hrs<extra></extra>"
        )

        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"An error occurred while generating the sunburst plot: {e}")
        st.write(
            "Please check your DataFrame columns and ensure the 'Age_Group' column was created correctly."
        )
    st.markdown(
        """##### Sunburst Plot - Key Insights:
The sunburst chart shows that most demographic groups fall within the 5-6.5 hours daily screen-time range, shown by the dominant orange and light-red
segments. Lower screen-time levels (the purple segments) are far less common and mainly appear among teen and young adult females, especially those
using LinkedIn or Twitter.
- **Older Adults (226):**
Females represent the largest share (112 users). Their most commonly used platform is LinkedIn (24 users), with an average screen time of 5.41 hours
per day.
- **Adults (134):**
Males form the biggest subgroup (69 users). They tend to favour Instagram (17 users), recording an average screen time of 6.09 hours, one of the
highest across all groups.
- **Young Adults (65):**
Mostly males (35 users). They overwhelmingly prefer Twitter (12 users), with an average screen time of 4.98 hours. This is double the count of their
second-most used platform, LinkedIn (6 users), highlighting a clear preference trend.
- **Teens (n = 75):**
The group is male-dominant (38 users), and TikTok is the preferred platform (9 users), with an average screen time of 4.82 hours."""
    )

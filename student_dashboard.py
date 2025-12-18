import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page title
st.title("🎓 Student Interactive Dashboard")

# Student data
data = {
    "Subject": ["Maths", "Physics", "Chemistry", "Computer", "English"],
    "Marks": [45, 38, 20, 52, 10],
    "Attendance": [10, 8, 64, 25, 32]
}

df = pd.DataFrame(data)

# Slider to filter marks
min_marks = st.slider("Select Minimum Marks", 0, 100, 50)

filtered_df = df[df["Marks"] >= min_marks]

# Show table
st.subheader("📋 Student Performance Table")
st.dataframe(filtered_df)

# Average metrics
st.subheader("📊 Performance Summary")
st.metric("Average Marks", round(filtered_df["Marks"].mean(), 2))
st.metric("Average Attendance", round(filtered_df["Attendance"].mean(), 2))

# Marks chart
st.subheader("📈 Marks Dashboard")
fig1, ax1 = plt.subplots()
ax1.bar(filtered_df["Subject"], filtered_df["Marks"])
ax1.set_xlabel("Subjects")
ax1.set_ylabel("Marks")
st.pyplot(fig1)

# Attendance chart
st.subheader("📉 Attendance Dashboard")
fig2, ax2 = plt.subplots()
ax2.plot(filtered_df["Subject"], filtered_df["Attendance"])
ax2.set_xlabel("Subjects")
ax2.set_ylabel("Attendance (%)")
st.pyplot(fig2)

# Attendance warning
st.subheader("⚠️ Attendance Alert")
low_att = filtered_df[filtered_df["Attendance"] < 75]

if not low_att.empty:
    st.warning("Attendance below 75% in:")
    st.write(low_att)
else:
    st.success("All subjects have good attendance 👍")

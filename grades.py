
data = {
    "Student_ID": ["S101", "S102", "S103"],
    "Written_Works": [88, 92, 79],
    "Performance_Tasks": [90, 85, 82],
    "Quarterly_Exam": [85, 88, 78],
}

df = pd.DataFrame(data)

# Example weighting: 30% Written Works, 50% Performance Tasks, 20% Quarterly Exam
df["Final_Grade"] = (
    (df["Written_Works"] * 0.30)
    + (df["Performance_Tasks"] * 0.50)
    + (df["Quarterly_Exam"] * 0.20)
)

print(df)

# Save updated grades back to CSV
df.to_csv("grades.csv", index=False)

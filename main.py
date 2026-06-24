import pandas as pd
df = pd.read_csv("social_media_engagement_dataset.csv")
print(df.head())
print(df.describe())

print(df.columns)

df["Total_Engagement"] = (
    df["Likes"] +
    df["Comments"] +
    df["Shares"] +
    df["Saves"]
)

best_hour = df.groupby("Hour_of_Day")["Total_Engagement"].mean()
print(best_hour.sort_values(ascending=False))

best_content = df.groupby("Content_Type")["Total_Engagement"].mean()
print(best_content.sort_values(ascending=False))

best_platform = df.groupby("Platform")["Total_Engagement"].mean()
print(best_platform.sort_values(ascending=False))

best_day = df.groupby("Day_of_Week")["Total_Engagement"].mean()
print(best_day.sort_values(ascending=False))

df.to_csv("social_media_analysis.csv", index=False)

best_content = df.groupby("Content_Type")["Total_Engagement"].mean()
print(best_content.sort_values(ascending=False))

best_platform = df.groupby("Platform")["Total_Engagement"].mean()
print(best_platform.sort_values(ascending=False))

best_day = df.groupby("Day_of_Week")["Total_Engagement"].mean()
print(best_day.sort_values(ascending=False))

best_platform = df.groupby("Platform")["Total_Engagement"].mean()
print(best_platform.sort_values(ascending=False))

df.to_csv("social_media_analysis.csv",index=False)
print("file saved successfully!")
import pandas as pd
import os

# =============================
# 1. LOAD DATA FILES
# =============================

daily_activity = pd.read_csv("dailyActivity_merged.csv")
sleep_day = pd.read_csv("sleepDay_merged.csv")
weight_log = pd.read_csv("weightLogInfo_merged.csv")
hourly_steps = pd.read_csv("hourlySteps_merged.csv")
heartrate_data = pd.read_csv("heartrate_seconds_merged.csv")

# =============================
# 2. CLEAN DAILY ACTIVITY
# =============================

daily_activity.drop_duplicates(inplace=True)
daily_activity.dropna(inplace=True)
daily_activity['ActivityDate'] = pd.to_datetime(daily_activity['ActivityDate'])
daily_activity['DayOfWeek'] = daily_activity['ActivityDate'].dt.day_name()

# =============================
# 3. CLEAN SLEEP DAY
# =============================

sleep_day.drop_duplicates(inplace=True)
sleep_day.dropna(inplace=True)
sleep_day['SleepDay'] = pd.to_datetime(sleep_day['SleepDay'], format="%m/%d/%Y %I:%M:%S %p")
sleep_day['DayOfWeek'] = sleep_day['SleepDay'].dt.day_name()

# =============================
# 4. CLEAN WEIGHT LOG
# =============================

weight_log.drop_duplicates(inplace=True)
weight_log.dropna(inplace=True)
weight_log['Date'] = pd.to_datetime(weight_log['Date'], format="%m/%d/%Y %I:%M:%S %p")

# =============================
# 5. CLEAN HOURLY STEPS
# =============================

hourly_steps.drop_duplicates(inplace=True)
hourly_steps.dropna(inplace=True)
hourly_steps['ActivityHour'] = pd.to_datetime(hourly_steps['ActivityHour'], format="%m/%d/%Y %I:%M:%S %p")
hourly_steps['Hour'] = hourly_steps['ActivityHour'].dt.hour
hourly_steps['DayOfWeek'] = hourly_steps['ActivityHour'].dt.day_name()

# =============================
# 6. CLEAN HEARTRATE DATA
# =============================

heartrate_data.drop_duplicates(inplace=True)
heartrate_data.dropna(inplace=True)
heartrate_data['Time'] = pd.to_datetime(heartrate_data['Time'])
heartrate_data['Hour'] = heartrate_data['Time'].dt.hour
heartrate_data['DayOfWeek'] = heartrate_data['Time'].dt.day_name()

# =============================
# 7. EXPORT CLEANED FILES
# =============================

daily_activity.to_csv("cleaned_daily_activity.csv", index=False)
sleep_day.to_csv("cleaned_sleep_day.csv", index=False)
weight_log.to_csv("cleaned_weight_log.csv", index=False)
hourly_steps.to_csv("cleaned_hourly_steps.csv", index=False)
heartrate_data.to_csv("cleaned_heartrate_data.csv", index=False)

print("✅ All datasets cleaned and saved successfully!")

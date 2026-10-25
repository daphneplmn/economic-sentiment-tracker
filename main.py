import pandas as pd
import matplotlib.pyplot as plt

# 1. Δημιουργία συνθετικών δεδομένων οικονομικού κλίματος & αναζητήσεων
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"],
    "Search_Inflation": [45, 50, 65, 80, 75, 70, 85, 90, 88, 95],
    "Search_Recession": [20, 22, 30, 45, 40, 38, 55, 60, 62, 70],
    "Consumer_Confidence_Index": [98, 96, 90, 82, 84, 85, 78, 75, 74, 70]
}

df = pd.DataFrame(data)

# 2. Υπολογισμός ενός απλού "Economic Anxiety Index"
# (Μέσος όρος των αναζητήσεων για πληθωρισμό και ύφεση)
df["Economic_Anxiety_Index"] = (df["Search_Inflation"] + df["Search_Recession"]) / 2

print("--- Economic Sentiment Summary ---")
print(df[["Month", "Economic_Anxiety_Index", "Consumer_Confidence_Index"]])

# 3. Δημιουργία διαγράμματος
plt.figure(figsize=(10, 5))
plt.plot(df["Month"], df["Economic_Anxiety_Index"], label="Economic Anxiety Index (Search Sentiment)", color="red", marker="o")
plt.plot(df["Month"], df["Consumer_Confidence_Index"], label="Consumer Confidence Index", color="blue", marker="s", linestyle="--")

plt.title("Economic Anxiety vs. Consumer Confidence")
plt.xlabel("Month")
plt.ylabel("Score / Index")
plt.legend()
plt.grid(True)

# Αποθήκευση του διαγράμματος ως εικόνα
plt.savefig("economic_sentiment_plot.png")
print("\nPlot saved successfully as 'economic_sentiment_plot.png'")

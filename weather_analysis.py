import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperature = [28, 30, 29, 32, 31, 27, 26]
humidity = [60, 55, 62, 50, 53, 68, 72]

fig, ax1 = plt.subplots(figsize=(9, 5))
ax1.plot(days, temperature, marker="o", label="Temperature (C)")
ax1.set_xlabel("Day")
ax1.set_ylabel("Temperature (C)")
ax1.set_title("Weekly Weather Report")

ax2 = ax1.twinx()
ax2.plot(days, humidity, marker="s", linestyle="--", label="Humidity (%)")
ax2.set_ylabel("Humidity (%)")

fig.tight_layout()
plt.savefig("weather_report.png")
plt.show()

print("Highest temperature:", max(temperature), "C")
print("Average humidity:", round(sum(humidity) / len(humidity), 1), "%")

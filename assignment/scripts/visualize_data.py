import matplotlib.pyplot as plt
import numpy as np

# Data: Altitude, Temperature, Dewpoint, Wind speed components (u, v)
gpheight = np.array([57.5, 128.4, 228.8, 359.4, 463.8, 571.9, 651.4, 755.8, 898.0, 1003.3, 1106.4, 1206.4, 1310.0])
temp = np.array([296.15, 294.4, 293.22, 291.89, 290.8, 289.77, 288.99, 288.18, 286.9, 286.09, 285.07, 284.07, 283.17])
dewpoint = np.array([288.0, 285.46, 284.93, 283.23, 283.69, 284.04, 283.92, 283.22, 282.54, 281.66, 281.14, 281.34, 279.96])
wind_u = np.array([2.87, 2.21, 1.87, 1.99, 2.93, 2.92, 2.61, 1.7, 1.26, 2.01, 1.81, 1.91, 2.46])
wind_v = np.array([4.1, 3.69, 4.2, 4.91, 4.18, 2.28, 2.9, 2.94, 0.99, 0.89, 1.57, 2.44, 3.65])

# 1. Temperature Plot
plt.plot(gpheight, temp, 'r-o', label="Temperature (K)")
plt.title("Temperature vs Altitude")
plt.xlabel("Altitude (m)")
plt.ylabel("Temperature (K)")
plt.grid(True)
plt.savefig("temperature_plot.png")
plt.show()

# 2. Wind Speed Plot
wind_speed = np.sqrt(wind_u**2 + wind_v**2)
plt.plot(gpheight, wind_speed, 'b-o', label="Wind Speed (m/s)")
plt.title("Wind Speed vs Altitude")
plt.xlabel("Altitude (m)")
plt.ylabel("Wind Speed (m/s)")
plt.grid(True)
plt.savefig("wind_speed_plot.png")
plt.show()

# 3. Humidity Plot (Approximation)
def saturation_vapor_pressure(T_celsius):
    return 6.11 * 10**((7.5 * T_celsius) / (T_celsius + 237.3))

e_temp = saturation_vapor_pressure(temp - 273.15)  # Convert temperature to Celsius
e_dew = saturation_vapor_pressure(dewpoint - 273.15)
relative_humidity = 100 * (e_dew / e_temp)

plt.plot(gpheight, relative_humidity, 'g-o', label="Relative Humidity (%)")
plt.title("Relative Humidity vs Altitude")
plt.xlabel("Altitude (m)")
plt.ylabel("Relative Humidity (%)")
plt.grid(True)
plt.savefig("humidity_plot.png")
plt.show()

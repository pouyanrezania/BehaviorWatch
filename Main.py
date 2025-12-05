import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

data = pd.read_csv('data/user_activity_500.csv')
features = data[['login_count','avg_session_time','purchase_amount','click_count']]

model = IsolationForest(contamination=0.1, random_state=42)
data['anomaly'] = model.fit_predict(features)
normal = data[data['anomaly'] == 1]
anomaly = data[data['anomaly'] == -1]

plt.figure(figsize=(10,6))
plt.scatter(normal['login_count'], normal['purchase_amount'], c='green', label='Normal', alpha=0.6)
plt.scatter(anomaly['login_count'], anomaly['purchase_amount'], c='red', label='Anomaly', alpha=0.6)
plt.xlabel('Login Count')
plt.ylabel('Purchase Amount')
plt.title('User Behavior Anomaly Detection')
plt.legend()
plt.grid(True)
plt.show()

predictions = model.decision_function(features)
mse = mean_squared_error(features.values, predictions.reshape(-1,1))
r2 = r2_score(features.values, predictions.reshape(-1,1))
print('MSE:', mse)
print('R²:', r2)

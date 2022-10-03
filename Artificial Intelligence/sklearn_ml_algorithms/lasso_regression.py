from sklearn.linear_model import Lasso
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the dataset
boston = load_boston()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    boston.data, boston.target, test_size=0.2, random_state=42)

# Create lasso regression object
lasso = Lasso(alpha=0.1)

# Train the model using the training sets
lasso.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = lasso.predict(X_test)

# The coefficients
print('Coefficients: ', lasso.coef_)
# The mean squared error
print('Mean squared error: %.2f' % mean_squared_error(y_test, y_pred))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f' % r2_score(y_test, y_pred))

# Plot outputs
plt.scatter(X_test[:, 5], y_test,  color='black')

plt.plot(X_test[:, 5], y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())
plt.show()

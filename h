from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, f1_score

print("System: Initializing Project 2 Pipeline...\n")

iris = load_iris()
X = iris.data  
y = iris.target 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, shuffle=True)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)

predictions = model.predict(X_test_scaled)

conf_matrix = confusion_matrix(y_test, predictions)
f1 = f1_score(y_test, predictions, average='macro')

print("--- OUTPUT VALIDATION ---")
print("Confusion Matrix:")
print(conf_matrix)
print(f"\nF1 Score: {f1:.4f}")
print("\nSystem: Supervised Learning Pipeline Complete.")
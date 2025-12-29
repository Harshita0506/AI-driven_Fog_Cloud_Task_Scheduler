from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import random

# generate n number of tasks to train the model 
def generate_dataset(n_samples=200):
    X, y = [], []
    for _ in range(n_samples):
        cpu = random.randint(100,1000)
        data=random.randint(5,50)
        deadline=random.randint(2,20)
        priority=random.randint(1,3)
        fog_load = round(random.uniform(0.1,0.9),2)
        cloud_load = round(random.uniform(0.1,0.9),2)

        # Score-based decision for balanced labels
        fog_score = 0
        cloud_score = 0

        # Deadline urgency
        if deadline <= 8:
            fog_score += 1
        else:
            cloud_score += 1

        # CPU requirement
        if cpu <= 600:
            fog_score += 1
        else:
            cloud_score += 1

        # Data size
        if data <= 25:
            fog_score += 1
        else:
            cloud_score += 1

        # Load awareness
        if fog_load < cloud_load:
            fog_score += 1
        else:
            cloud_score += 1

        label = 0 if fog_score >= cloud_score else 1


        X.append([cpu,data,deadline,priority,fog_load,cloud_load])
        y.append(label)

    return X, y

#  function to train the model

def train_model():
    X, y = generate_dataset()

    # 1. Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # 2. Feature scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 3. Model training
    model = MLPClassifier(hidden_layer_sizes=(16, 8), max_iter=1000, random_state=42)
    model.fit(X_train_scaled, y_train)

    # 4. Accuracy calculation
    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)

    # 5. Return everything needed
    return model, scaler, accuracy


# predicts output for the given training samples
def predict_environment(task, model, scaler):
    features = [[               #convert features into numbers 
        task["cpu_cycles"],
        task["data_size"],
        task["deadline"],
        task["priority"],
        task["fog_load"],
        task["cloud_load"]
    ]]
    features = scaler.transform(features)
    return model.predict(features)[0]
from ml.model import train_model
from scheduler.scheduler import run_scheduler
from visualization import (
    plot_acceptance_rejection,
    plot_priority_distribution,
    plot_fog_cloud_distribution
)


model, scaler, ml_accuracy = train_model()

print("Neural Network model trained successfully.")
print(f"Neural Network Accuracy: {ml_accuracy:.2f}")
metrics = run_scheduler(model, scaler, num_tasks=50)


accepted_tasks = metrics["accepted_tasks"]
rejected_tasks = metrics["rejected_tasks"]
priority_accepted = metrics["priority_accepted"]
priority_rejected = metrics["priority_rejected"]
fog_count = metrics["fog_count"]
cloud_count = metrics["cloud_count"]

plot_acceptance_rejection(accepted_tasks, rejected_tasks)
plot_fog_cloud_distribution(fog_count, cloud_count)
plot_priority_distribution(priority_accepted, priority_rejected)
# visualization.py
import matplotlib.pyplot as plt

def plot_acceptance_rejection(accepted, rejected):
    labels = ['Accepted Tasks', 'Rejected Tasks']
    values = [accepted, rejected]

    plt.figure()
    plt.bar(labels, values)
    plt.title("Task Acceptance vs Rejection")
    plt.ylabel("Number of Tasks")
    plt.show()

# visualization.py
def plot_fog_cloud_distribution(fog_tasks, cloud_tasks):
    labels = ['Fog', 'Cloud']
    values = [fog_tasks, cloud_tasks]

    plt.figure()
    plt.bar(labels, values)
    plt.title("Fog vs Cloud Task Distribution")
    plt.ylabel("Number of Tasks")
    plt.show()

# visualization.py
def plot_priority_distribution(accepted_dict, rejected_dict):
    priorities = ['Priority 1', 'Priority 2', 'Priority 3']
    accepted = [
        accepted_dict[1],
        accepted_dict[2],
        accepted_dict[3]
    ]
    rejected = [
        rejected_dict[1],
        rejected_dict[2],
        rejected_dict[3]
    ]

    x = range(len(priorities))

    plt.figure()
    plt.bar(x, accepted)
    plt.bar(x, rejected, bottom=accepted)
    plt.xticks(x, priorities)
    plt.title("Priority-wise Accepted vs Rejected Tasks")
    plt.ylabel("Number of Tasks")
    plt.legend(['Accepted', 'Rejected'])
    plt.show()

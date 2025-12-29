#this funtion is for making metrics evaluation 
def init_metrics():
    return {
        "total": 0,
        "accepted": 0,
        "rejected": 0,
        "fog": 0,
        "cloud": 0,
        "accepted_priority": {1: 0, 2: 0, 3: 0},
        "rejected_priority": {1: 0, 2: 0, 3: 0}
    }

def print_metrics(m):
    print("\n========== METRICS SUMMARY ==========")
    print(f"Total tasks: {m['total']}")
    print(f"Accepted tasks: {m['accepted']}")
    print(f"Rejected tasks: {m['rejected']}")
    print(f"Acceptance rate: {(m['accepted']/m['total'])*100:.2f}%")
    print(f"Rejection rate: {(m['rejected']/m['total'])*100:.2f}%")

    print("\n--- Environment Distribution ---")
    print(f"Fog tasks: {m['fog']}")
    print(f"Cloud tasks: {m['cloud']}")

    print("\n--- Priority-wise Accepted ---")
    for k, v in m["accepted_priority"].items():
        print(f"Priority {k}: {v}")

    print("\n--- Priority-wise Rejected ---")
    for k, v in m["rejected_priority"].items():
        print(f"Priority {k}: {v}")

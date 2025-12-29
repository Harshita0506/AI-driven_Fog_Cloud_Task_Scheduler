from scheduler.task_generator import generate_task
from scheduler.feasibility import check_feasibility
from scheduler.node_allocator import create_nodes, allocate_node, apply_decay
from metrics.metrics import init_metrics, print_metrics
from llm_explainer.explainer import explain_task
from ml.model import predict_environment

# -----------------------------
# Decay parameters
# -----------------------------
FOG_DECAY = 0.05
CLOUD_DECAY = 0.08


def run_scheduler(model, scaler, num_tasks=30):
    """
    Runs ML-driven Fog–Cloud scheduling simulation
    with feasibility check and LLM explainability.
    """

    # -----------------------------
    # Initial system load
    # -----------------------------
    current_fog_load = 0.0
    current_cloud_load = 0.0

    # -----------------------------
    # Create nodes
    # -----------------------------
    fog_nodes = create_nodes("Fog", 3)
    cloud_nodes = create_nodes("Cloud", 3)

    # -----------------------------
    # Initialize metrics (SINGLE SOURCE OF TRUTH)
    # -----------------------------
    metrics = init_metrics()

    print("\n--- ML-Driven Scheduling Simulation with feasibility check ---\n")

    # -----------------------------
    # Main scheduling loop
    # -----------------------------
    for i in range(num_tasks):
        task = generate_task()
        metrics["total"] += 1

        # ML decision: 0 = Fog, 1 = Cloud
        decision = predict_environment(task, model, scaler)
        env = "FOG" if decision == 0 else "CLOUD"

        feasible, task_load = check_feasibility(
            task,
            decision,
            current_fog_load,
            current_cloud_load
        )

        print(f"\nTask {i+1}: {task}")

        # -----------------------------
        # If task is feasible
        # -----------------------------
        if feasible:
            metrics["accepted"] += 1
            metrics["accepted_priority"][task["priority"]] += 1

            if decision == 0:
                node_id = allocate_node(fog_nodes, task_load)
                current_fog_load += task_load
                metrics["fog"] += 1
            else:
                node_id = allocate_node(cloud_nodes, task_load)
                current_cloud_load += task_load
                metrics["cloud"] += 1

            print(f"ML Scheduler Decision: {env} -> Assigned to {node_id}")

        # -----------------------------
        # If task is rejected
        # -----------------------------
        else:
            metrics["rejected"] += 1
            metrics["rejected_priority"][task["priority"]] += 1
            print("Task Rejected (Deadline / Load constraint violated)")

        # -----------------------------
        # LLM Explainability (FOR BOTH CASES)
        # -----------------------------
        explanation = explain_task(task, env, feasible)
        print("LLM Explanation:", explanation)

        # -----------------------------
        # Apply decay (task completion simulation)
        # -----------------------------
        current_fog_load = max(0, current_fog_load - FOG_DECAY)
        current_cloud_load = max(0, current_cloud_load - CLOUD_DECAY)

        fog_nodes = apply_decay(fog_nodes, FOG_DECAY / 3)
        cloud_nodes = apply_decay(cloud_nodes, CLOUD_DECAY / 3)

    # -----------------------------
    # Print final metrics
    # -----------------------------
    print_metrics(metrics)

    # -----------------------------
    # Return metrics for visualization
    # -----------------------------
    return {
        "accepted_tasks": metrics["accepted"],
        "rejected_tasks": metrics["rejected"],
        "priority_accepted": metrics["accepted_priority"],
        "priority_rejected": metrics["rejected_priority"],
        "fog_count": metrics["fog"],
        "cloud_count": metrics["cloud"]
    }

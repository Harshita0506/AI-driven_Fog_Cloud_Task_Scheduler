import random

def generate_task():
    return {
        "cpu_cycles": random.randint(100,1000),
        "data_size": random.randint(5,50),
        "deadline": random.randint(2,20),
        "priority": random.randint(1,3),
        "fog_load":round(random.uniform(0.1,0.9),2),
        "cloud_load":round(random.uniform(0.1,0.9),2)
    }
    
 
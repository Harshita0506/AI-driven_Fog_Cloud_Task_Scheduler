MAX_FOG_LOAD = 1.0              #maximmum fog capacity
MAX_CLOUD_LOAD = 2.0            #maximum cloud capacity

FOG_HIGH_LOAD = 0.75            #points after which we consider priority of tasks
CLOUD_HIGH_LOAD = 2.5

def check_feasibility(task, decision, fog_load, cloud_load):            #check the feasibility of the task
    task_load = task["cpu_cycles"] / 2000.0
    priority = task["priority"]

    if decision == 0:                                   #fog network
        if fog_load + task_load > MAX_FOG_LOAD:           #if adding this task will exceed fog limit , task will not accepted
            return False, task_load
        if fog_load > FOG_HIGH_LOAD and priority == 3:      #if network is heavily loaded and task is of low priority , reject
            return False, task_load
        return True, task_load
    else:                                               #cloud network
        if cloud_load + task_load > MAX_CLOUD_LOAD:         #if adding this task exceeds cloud limit , then reject
            return False, task_load
        if cloud_load > CLOUD_HIGH_LOAD and priority == 3:      #if neywork is heavily loaded , and task is of low priority , reject it
            return False, task_load
        return True, task_load

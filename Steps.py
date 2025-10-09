def walk(steps):
    if steps == 0:
        return
    
    
    walk(steps - 1)
    print(f"You took - {steps} steps")
    
walk(100)
    
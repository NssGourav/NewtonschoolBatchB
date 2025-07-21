rods = {'A', 'B', 'C'}

def move(n, source, destination):
    if n==0:
        return 
    
    current = {source, destination}

    extra = (rods - current).pop()

    move(n-1, source, extra)
    print(f"Move disk {n} from {source} to {destination}")
    move(n-1, extra, destination)

move(3, "A", "B")

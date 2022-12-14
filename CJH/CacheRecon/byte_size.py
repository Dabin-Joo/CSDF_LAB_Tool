def size(x):
    end = x.seek(0,2)
    x.seek(-end,2)
    return end
def check(x,y):
    if x < y:
        return False
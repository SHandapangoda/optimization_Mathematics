cur_x = 1 
rate = 0.01
precision = 0.000001
prev_step_size = 1 
max_iters = 10000
iters = 0
df = lambda x: 2 * (x - 6)

while prev_step_size > precision and iters < max_iters:
    prev_x = cur_x
    cur_x = cur_x - rate * df(prev_x) 
    prev_step_size = abs(cur_x - prev_x)
    iters = iters + 1
    print("Iter num",iters,"\nX value is",cur_x)

print("The min occ @ ", cur_x)


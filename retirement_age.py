def retirement_age(PMT, i, FV, start_age):
    age = 0
    c = 0
    future_value = 0
    while(future_value <= FV):
        interest = future_value * i
        future_value = future_value + interest
        future_value = future_value + PMT
        c = c + 1
        age = c + start_age
    return age
retirement_age(10000,0.1,572749.99,40)

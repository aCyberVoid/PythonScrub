people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can not decide")

if trucks > cars:
    print("That's too many trucks. Where did they come from!?")
elif trucks < cars:
    print("Maybe we could take the trucks instead.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks!")
else:
    print("FINE! I give up. Let's stay home since we can't decide!")

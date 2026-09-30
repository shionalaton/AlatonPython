
patients={"Siah":(96,120,400),
"Fart":(70,180,100)}
print(patients)

normal=120
for key, value in patients.items():
    print(key)
    for v in value:
        if v>normal:
            print(v, "diabetic")
        else:
            print(v, "normal")
    highest=max(value)
    print(highest, key)
    lowest=min(value)
    print(lowest, key)
    diff=highest-lowest
    print(diff)


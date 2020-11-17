print("Origin Distance width(px): ", end="")
print(str((float(input())*100)/1920)+"vw")
for _ in range(10000):
    print("Change vh to vw (vh): ", end="")
    print(str(((float(input()[:-2])*1080)/100*100)/1920)+"vw")
print("Font Size(pt): ", end="")
print(str(((float(input())*1.3281472327365)*100)/1920)+"vw")

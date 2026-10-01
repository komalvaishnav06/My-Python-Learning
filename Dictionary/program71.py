# using zip
days = ("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]

print({i:j for (i,j) in zip(days,temp_C)})
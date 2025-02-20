start_h = int(input("Starting time (hours): "))
start_m = int(input("Starting time (minutes): "))
duration = int(input("Event duration (minutes): "))

end_h = (start_h + (start_m + duration) // 60) % 24
end_m = (start_m + duration) % 60

print(f"End: {end_h} : {end_m}")


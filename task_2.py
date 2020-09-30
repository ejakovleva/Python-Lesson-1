script_time = int(input("How long did it take for your PC to run a script? "))
seconds = script_time % 60
minutes_overall = script_time // 60
minutes = minutes_overall % 60
hours = minutes_overall // 60
print(f'{hours:02}:{minutes:02}:{seconds:02}')

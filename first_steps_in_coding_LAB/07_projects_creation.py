# Напишете програма, която изчислява колко часа ще са необходими на един архитект,
# за да изготви проектите на няколко строителни обекта. Изготвянето на един проект отнема три часа.


architect_name = input()
projects_number = int(input())

working_hours = projects_number * 3;

print(f'The architect {architect_name} will need {working_hours} hours to complete {projects_number} project/s.')
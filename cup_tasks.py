import csv

input_file_task = "LKVL_600_2024_task_test.cup"
output_file_task = "LKVL_600_2024_task_processed.cup"

input_file_waypoint = ''
output_file_waypoint = ''


def process_observation_zones(entries, output_file):
    """
    Adds styles to observation zones in .cup tasks
    Takeoff - style 2
    Landing - style 3
    All other waypoints - style 3
    """
    obs_zone = 0
    for i, entry in enumerate(entries):
        print(f'{i=}, entry: {entry}, index: {entries.index(entry)} / entries: {len(entries)}, {obs_zone=}')
        if str(entry) in "???" or i == 0:
            print('skipping')
        else:
            # style = 2 if obs_zone == 0 else (3 if entries.index(entry) == len(entries) - 2 else 1)
            if obs_zone == 0:
                style = 2
            elif i == len(entries) - 2:
                style = 3
            else:
                style = 1

            # style = ((obs_zone == 0) * 2) + ((i == len(entries) - 2 and obs_zone != 0) * 3) + (obs_zone != 0 and i != len(entries) - 2)

            print(f'entry: {entry}, obsZone: {obs_zone}, style: {style}, ')
            output_file.write(f"ObsZone={obs_zone},Style={style},R1=500m,A1=180\n")
            obs_zone += 1

            print('------')
    print('------------')


# def process_task_line(entries, output_file):
#     """Add 'Options,Short=false' text under each task line"""
#     output_file.write("Options,Short=false\n")
#     process_observation_zones(entries, output_file)

def process_cup_tasks(input_file_path, output_file_path):
    print(f'starting processing {input_file_path}')
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        csv_reader = csv.reader(input_file)
        for row in csv_reader:
            if row and row[0].startswith("TSK"):
                output_file.write(','.join(f'"{item}"' for item in row) + '\n')  # Write the original line with double quotes
                # process_task_line(row, output_file)
                output_file.write("Options,Short=false\n")   # Add text under each task line
                process_observation_zones(row, output_file)  # Assign styles to observation zones
    print(f'processing, done, output: {output_file_path}')


def sort_waypoints(input_file_path, output_file_path):
    """Alphabetically sorts entries in file"""
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    lines.sort()

    with open(output_file_path, 'w') as output_file:
        for line in lines:
            output_file.write(line)


if __name__ == "__main__":

    process_cup_tasks(input_file_task, output_file_task)

    # sort_waypoints(input_file_waypoint, output_file_waypoint)




"""
fun max(x: Int, y: Int): Int {
    if (x >  y) return x
    return y
    
    ((x > y) * x) + ((y >= x) * y)
}
"""


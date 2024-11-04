import pandas as pd
import glob
import os

# Define mappings with exact matches for each unique class name identified
mappings = {
    "run1": {
        "class_mapping": {"0": 0, "3": 0, "1": 1, "4": 1, "2": 2, "5": 2},
        "old_to_new_class": {
            "6N10A": "A_8N8D", "8N8A": "B_8N8D", "10N6A": "W_8N8D",
            "6N10D": "A_8N8D", "8N8D": "B_8N8D", "10N6D": "W_8N8D"
        },
        "event_name": "Disgust-Neutral"
    },
    "run2": {
        "class_mapping": {"0": 0, "3": 0, "1": 1, "4": 1, "2": 2, "5": 2},
        "old_to_new_class": {
            "6N10A": "A_8H8A", "8N8A": "B_8H8A", "10N6A": "W_8H8A",
            "6N10D": "A_8H8A", "8N8D": "B_8H8A", "10N6D": "W_8H8A"
        },
        "event_name": "Angry-Happy"
    },
    "run3": {
        "class_mapping": {"0": 0, "3": 0, "1": 1, "4": 1, "2": 2, "5": 2},
        "old_to_new_class": {
            "6N10A": "A_8H8S", "8N8A": "B_8H8S", "10N6A": "W_8H8S",
            "6N10D": "A_8H8S", "8N8D": "B_8H8S", "10N6D": "W_8H8S"
        },
        "event_name": "Sad-Happy"
    }
}

# Initialize total class counts across all files for each run
total_class_counts = {"run1": {}, "run2": {}, "run3": {}}

# Locate the input files
input_timing_files = glob.glob("timing/notUsed/*.txt")
for file_path in input_timing_files:
    # Read the file and separate the data into runs
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Initialize variables to store data for each run and cumulative count for each file
    runs = {"run1": [], "run2": [], "run3": []}
    current_run = None
    class_counts = {"run1": {}, "run2": {}, "run3": {}}  # Track cumulative counts for each class within each run

    # Parse the lines to separate runs
    for line in lines:
        line = line.strip()
        if "-- run 1 events --" in line:
            current_run = "run1"
        elif "-- run 2 events --" in line:
            current_run = "run2"
        elif "-- run 3 events --" in line:
            current_run = "run3"
        elif current_run and line and not line.startswith("class") and not line.startswith("-----"):
            # Split the line into columns based on whitespace
            split_line = line.split()
            class_old = split_line[0]  # Extract the original class (e.g., 0, 1, etc.)
            class_name = split_line[1][1:-1]  # Extract the class code inside the parentheses
            start, dur, rest = map(float, split_line[2:5])

            # Map class_old to class_new and class_name to class_name_new based on mappings
            class_new = mappings[current_run]["class_mapping"].get(class_old, class_old)
            new_class_name = mappings[current_run]["old_to_new_class"].get(class_name, class_name)

            # Format the `class` column with both class_new and new_class_name
            class_combined = f"{class_new} ({new_class_name})"

            # Update cumulative count for the current class in the current run
            if class_combined not in class_counts[current_run]:
                class_counts[current_run][class_combined] = 1
            else:
                class_counts[current_run][class_combined] += 1

            # Get the cumulative count for this class occurrence
            cumulative_count = class_counts[current_run][class_combined]

            # Append to the respective run's data with cumulative count
            runs[current_run].append([class_combined, start, dur, rest, cumulative_count])

    # Limit each run to the first half (30 events)
    for run_key in runs:
        runs[run_key] = runs[run_key][:30]

    # Re-calculate class counts based on the first half only
    first_half_class_counts = {key: {} for key in class_counts}
    for run_key, run_data in runs.items():
        for row in run_data:
            class_combined = row[0]
            if class_combined not in first_half_class_counts[run_key]:
                first_half_class_counts[run_key][class_combined] = 1
            else:
                first_half_class_counts[run_key][class_combined] += 1

    # Update total class counts across all files for the first half only
    for run_key, counts in first_half_class_counts.items():
        for class_combined, count in counts.items():
            if class_combined not in total_class_counts[run_key]:
                total_class_counts[run_key][class_combined] = count
            else:
                total_class_counts[run_key][class_combined] += count

    # Define the output file path based on the original input file path
    output_dir = "timing_meghan/notUsed"  # Change this directory if needed
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, os.path.basename(file_path))

    # Write each run with headers to the output file
    with open(output_file_path, "w") as output_file:
        for run_key, run_data in runs.items():
            # Write the run header
            output_file.write(f"-- {run_key} events --\n")

            # Write cumulative count summary for each class at the beginning of each block (first half only)
            output_file.write("Cumulative count per class (first half only):\n")
            for class_combined, count in first_half_class_counts[run_key].items():
                output_file.write(f"{class_combined}: {count}\n")
            output_file.write("\n")

            # Write table headers for event data
            output_file.write("class          start      dur     rest    cumulative_count\n")
            output_file.write("-----          -----      ----    ----    ----------------\n")

            # Write the data for the run
            for row in run_data:
                class_combined, start, dur, rest, cum_count = row
                output_file.write(f"{class_combined:<15}{start:<10}{dur:<8}{rest:<8}{cum_count}\n")

    print(f"Data for all runs with headers and cumulative count summaries saved to {output_file_path}")

# After processing all files, print out accumulated class counts across all files for each run (first half only)
print("Accumulated class counts across all files (first half only):")
for run_key, counts in total_class_counts.items():
    print(f"\n{run_key} cumulative counts:")
    for class_combined, total_count in counts.items():
        print(f"{class_combined}: {total_count}")

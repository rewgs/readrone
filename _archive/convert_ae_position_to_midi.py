import re

import mido

# Input and output file names
input_file = "input_position.txt"
output_file = "output_position.mid"

# MIDI CC numbers for X, Y, and Z
cc_x = 1
cc_y = 2
cc_z = 3

# Read the input file
with open(input_file, "r") as file:
    lines = file.readlines()

# Extract position data
positions = []
for line in lines:
    match = re.match(r"\s*(\d+)\s+([-\d\.]+)\s+([-\d\.]+)\s+([-\d\.]+)", line)
    if match:
        frame = int(match.group(1))
        x = float(match.group(2))
        y = float(match.group(3))
        z = float(match.group(4))
        positions.append((frame, x, y, z))


# Normalize values to MIDI range (0-127)
def normalize(value, min_val, max_val):
    return int((value - min_val) / (max_val - min_val) * 127)


if positions:
    x_vals = [p[1] for p in positions]
    y_vals = [p[2] for p in positions]
    z_vals = [p[3] for p in positions]

    min_x, max_x = min(x_vals), max(x_vals)
    min_y, max_y = min(y_vals), max(y_vals)
    min_z, max_z = min(z_vals), max(z_vals)

# Create a MIDI file
midi_file = mido.MidiFile()
track = mido.MidiTrack()
midi_file.tracks.append(track)

time_factor = 480  # Adjust timing based on frame rate if needed

for frame, x, y, z in positions:
    track.append(
        mido.Message(
            "control_change",
            control=cc_x,
            value=normalize(x, min_x, max_x),
            time=time_factor,
        )
    )
    track.append(
        mido.Message(
            "control_change", control=cc_y, value=normalize(y, min_y, max_y), time=0
        )
    )
    track.append(
        mido.Message(
            "control_change", control=cc_z, value=normalize(z, min_z, max_z), time=0
        )
    )

# Save the MIDI file
midi_file.save(output_file)
print(f"MIDI file saved as {output_file}")

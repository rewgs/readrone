import mido
import numpy as np

# Define input and output files
input_file = "input_orientation.txt"
output_midi = "output_orientation.mid"

# Read data from After Effects export
frames = []
x_degrees = []
y_degrees = []
z_degrees = []

with open(input_file, "r") as file:
    lines = file.readlines()

# Parse the lines, skipping headers
for line in lines:
    parts = line.strip().split()
    if len(parts) == 4 and parts[0].isdigit():
        frame = int(parts[0])
        x, y, z = map(float, parts[1:])
        frames.append(frame)
        x_degrees.append(x)
        y_degrees.append(y)
        z_degrees.append(z)

# Unwrap angles to avoid discontinuities
x_degrees = np.unwrap(np.radians(x_degrees))
y_degrees = np.unwrap(np.radians(y_degrees))
z_degrees = np.unwrap(np.radians(z_degrees))

# Convert back to degrees after unwrapping
x_degrees = np.degrees(x_degrees)
y_degrees = np.degrees(y_degrees)
z_degrees = np.degrees(z_degrees)

# Normalize values to MIDI range (0-127)
def scale_to_midi(values):
    min_val, max_val = min(values), max(values)
    return [int(127 * (v - min_val) / (max_val - min_val)) for v in values]

x_midi = scale_to_midi(x_degrees)
y_midi = scale_to_midi(y_degrees)
z_midi = scale_to_midi(z_degrees)

# Create a MIDI file
mid = mido.MidiFile()
track = mido.MidiTrack()
mid.tracks.append(track)

# Convert frames to MIDI time (assuming 24 fps)
fps = 23.977  # Adjust if necessary
ticks_per_frame = int(mid.ticks_per_beat / fps)

for i, frame in enumerate(frames):
    time = frame * ticks_per_frame
    track.append(mido.Message('control_change', control=1, value=x_midi[i], time=time))
    track.append(mido.Message('control_change', control=2, value=y_midi[i], time=0))
    track.append(mido.Message('control_change', control=3, value=z_midi[i], time=0))

# Save the MIDI file
mid.save(output_midi)
print(f"MIDI file saved: {output_midi}")

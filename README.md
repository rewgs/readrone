# readrone

Takes two .txt files of drone tracking information from Adobe After Effects and translates it to MIDI data and imports it into a Reaper project.

Example usage, assuming `cwd` = this directory:

```
python src/readrone.py \
    --orientation test_files/input_orientation.txt \
    --position test_files/input_position.txt
```

Still very much in progress!

#!/usr/bin/env python3
"""
Generate clean, non-overlapping per-clip SRT subtitle files from YouTube VTT captions.
Timestamps are shifted so each clip starts at 00:00:00,000.
"""

import os
import re
import json

VTT_PATH = "/tmp/doug_leone.en.vtt"
OUTPUT_DIR = "/home/antigravity/gdennngiamm/openreel-video/clips"
MANIFEST_PATH = os.path.join(OUTPUT_DIR, "clips_manifest.json")

def parse_time(ts_str):
    parts = ts_str.split(":")
    h = int(parts[0])
    m = int(parts[1])
    s, ms = parts[2].split(".")
    return h * 3600 + m * 60 + int(s) + int(ms) / 1000.0

def format_srt_time(seconds):
    if seconds < 0:
        seconds = 0
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int(round((seconds - int(seconds)) * 1000))
    if ms >= 1000:
        ms = 999
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def clean_cues():
    with open(VTT_PATH, "r") as f:
        content = f.read()

    pattern = re.compile(r'(\d{2}:\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}:\d{2}\.\d{3})[^\n]*\n([\s\S]*?)(?=\n\n|\Z)')
    raw_cues = []
    for m in pattern.finditer(content):
        start_sec = parse_time(m.group(1))
        end_sec = parse_time(m.group(2))
        # Filter out 10ms flicker transitions in YouTube auto-subs
        if end_sec - start_sec < 0.2:
            continue
        lines = [re.sub(r'<[^>]+>', '', l).strip() for l in m.group(3).split('\n')]
        clean_text = ' '.join(filter(None, lines))
        # If repeated prefix, keep only new part or last line
        if lines:
            line_to_use = lines[-1] if len(lines) > 1 and lines[-1] else clean_text
        else:
            line_to_use = clean_text
        if line_to_use and (not raw_cues or raw_cues[-1][2] != line_to_use):
            raw_cues.append((start_sec, end_sec, line_to_use))
    return raw_cues

def generate_srt_for_clips():
    with open(MANIFEST_PATH, "r") as f:
        manifest = json.load(f)
        
    raw_cues = clean_cues()

    for clip in manifest["clips"]:
        clip_id = clip["id"]
        clip_start = clip["start_sec"]
        clip_end = clip["end_sec"]
        srt_file = os.path.join(OUTPUT_DIR, f"{clip_id}.srt")
        
        clip_cues = []
        for s, e, text in raw_cues:
            if e > clip_start and s < clip_end:
                rel_s = max(0.0, s - clip_start)
                rel_e = min(clip_end - clip_start, e - clip_start)
                if rel_e - rel_s >= 0.3:
                    if not clip_cues or clip_cues[-1][2] != text:
                        clip_cues.append((rel_s, rel_e, text))
                        
        with open(srt_file, "w") as out:
            for idx, (s, e, text) in enumerate(clip_cues, 1):
                out.write(f"{idx}\n")
                out.write(f"{format_srt_time(s)} --> {format_srt_time(e)}\n")
                out.write(f"{text}\n\n")
                
        print(f"[✓] Generated {len(clip_cues)} clean subtitle cues for {clip_id}.srt")

if __name__ == "__main__":
    generate_srt_for_clips()

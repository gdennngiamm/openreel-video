#!/usr/bin/env python3
"""
High-Speed Clip Extraction and Processing Pipeline
Target Video: Sequoia's Doug Leone on Building Enduring Companies in the AI Era | ElevenLabs Summit London 2026
URL: https://youtu.be/afSmwxT0Y3o
Master File: /tmp/doug_leone_full.webm
"""

import os
import json
import subprocess
import time

CLIPS = [
    {
        "id": "clip_1_experience_a_problem",
        "title": "Go Experience A Problem (The Conference Room Startup Fallacy)",
        "hook": "Why talking to 5 CIOs in a conference room scares Sequoia's Doug Leone",
        "start": "00:29:55",
        "end": "00:30:35",
        "start_sec": 1795,
        "end_sec": 1835,
        "quote": "If you want to scare the shit out of me as an investor, tell me you and two friends got in a conference room and decided to talk to five CIOs to figure out what their problem was. Go experience a problem.",
        "tags": ["startups", "venture_capital", "founders", "dougleone", "sequoia"]
    },
    {
        "id": "clip_2_strategy_is_later",
        "title": "Strategy Is Later: Get To 500 Customers First",
        "hook": "You know what a great strategy is? Get to 500 customers.",
        "start": "00:15:45",
        "end": "00:16:20",
        "start_sec": 945,
        "end_sec": 980,
        "quote": "Strategy is later. Right now: execution, execution, execution. You know what a great strategy is? Get to 500 customers! Sell, sell, sell. Once you get to 500 customers, we'll talk about positioning and Super Bowl ads.",
        "tags": ["execution", "sales", "startups", "b2b", "gtm"]
    },
    {
        "id": "clip_3_most_board_members_noops",
        "title": "Most Board Members Are No-Ops (They Add Zero Value)",
        "hook": "You're lucky if you get a no-op board member who does no damage.",
        "start": "00:21:15",
        "end": "00:22:00",
        "start_sec": 1275,
        "end_sec": 1320,
        "quote": "Keep in mind that most board members—and this is going to shock you—are no-ops. You're lucky if you get a no-op board member. They do no damage, they add no value: zero. A great board member is a shock absorber.",
        "tags": ["board_of_directors", "governance", "venture_capital", "leadership"]
    },
    {
        "id": "clip_4_architect_cap_table",
        "title": "Architect Your Cap Table Like You Architect The Product",
        "hook": "Don't brag about term sheets. Architect your cap table.",
        "start": "00:27:50",
        "end": "00:28:40",
        "start_sec": 1670,
        "end_sec": 1720,
        "quote": "Architect your cap table the same way you architect the product. Don't give us this 'I got two term sheets'... Who cares? Align the equity early. Don't wake up 90 days in arguing over who owns what.",
        "tags": ["cap_table", "equity", "co-founders", "fundraising"]
    }
]

MASTER_VIDEO = "/tmp/doug_leone_full.webm"
VIDEO_URL = "https://www.youtube.com/watch?v=afSmwxT0Y3o"
OUTPUT_DIR = "/home/antigravity/gdennngiamm/openreel-video/clips"

def extract_all():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Save clips manifest
    manifest_path = os.path.join(OUTPUT_DIR, "clips_manifest.json")
    with open(manifest_path, "w") as f:
        json.dump({
            "source_url": VIDEO_URL,
            "source_title": "Sequoia's Doug Leone on Building Enduring Companies in the AI Era | ElevenLabs Summit London 2026",
            "video_id": "afSmwxT0Y3o",
            "total_clips": len(CLIPS),
            "clips": CLIPS
        }, f, indent=2)
    print(f"[✓] Saved manifest to {manifest_path}")

    start_all = time.time()
    for idx, clip in enumerate(CLIPS, 1):
        clip_id = clip["id"]
        start_sec = clip["start_sec"]
        end_sec = clip["end_sec"]
        
        print(f"\n[{idx}/{len(CLIPS)}] Processing '{clip['title']}' ({start_sec}s -> {end_sec}s)...")
        
        # 1. 16:9 Landscape MP4
        landscape_out = os.path.join(OUTPUT_DIR, f"{clip_id}_landscape.mp4")
        cmd_landscape = [
            "ffmpeg", "-y",
            "-ss", str(start_sec), "-to", str(end_sec),
            "-i", MASTER_VIDEO,
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "22",
            "-c:a", "aac", "-b:a", "192k",
            "-movflags", "+faststart",
            landscape_out
        ]
        subprocess.run(cmd_landscape, check=True)
        print(f"  -> Generated landscape: {os.path.basename(landscape_out)} ({os.path.getsize(landscape_out) // 1024} KB)")

        # 2. 9:16 Vertical MP4 (Shorts / Reels / TikTok)
        vertical_out = os.path.join(OUTPUT_DIR, f"{clip_id}_vertical_9x16.mp4")
        filter_complex = (
            "[0:v]fps=30,scale=540:960:force_original_aspect_ratio=increase,crop=540:960,boxblur=10:2[bg];"
            "[0:v]fps=30,scale=540:960:force_original_aspect_ratio=decrease[fg];"
            "[bg][fg]overlay=(W-w)/2:(H-h)/2"
        )
        cmd_vertical = [
            "ffmpeg", "-y",
            "-ss", str(start_sec), "-to", str(end_sec),
            "-i", MASTER_VIDEO,
            "-filter_complex", filter_complex,
            "-c:v", "libx264", "-preset", "ultrafast", "-crf", "23",
            "-c:a", "aac", "-b:a", "192k",
            "-movflags", "+faststart",
            vertical_out
        ]
        subprocess.run(cmd_vertical, check=True)
        print(f"  -> Generated vertical: {os.path.basename(vertical_out)} ({os.path.getsize(vertical_out) // 1024} KB)")

    elapsed = round(time.time() - start_all, 1)
    print(f"\n[🎉] All {len(CLIPS)} clips (8 video files) extracted successfully in {elapsed} seconds!")

if __name__ == "__main__":
    extract_all()

# Video Clipping Process & Memory: Doug Leone on Building Enduring Companies

## 1. Saved Reference & Video Memory
- **Video Title:** Sequoia's Doug Leone on Building Enduring Companies in the AI Era | ElevenLabs Summit London 2026
- **YouTube URL:** [https://youtu.be/afSmwxT0Y3o](https://youtu.be/afSmwxT0Y3o)
- **Direct Link:** [https://www.youtube.com/watch?v=afSmwxT0Y3o](https://www.youtube.com/watch?v=afSmwxT0Y3o)
- **Duration:** 30 minutes 53 seconds (1,853 seconds)
- **Speakers:** Doug Leone (Sequoia Capital), Mati Staniszewski (co-founder, ElevenLabs)
- **Key Themes:** Laws of physics in business, founder execution vs strategy, AI transformation, board dynamics, cap table architecture, IPO preparation, and identifying authentic problems.

---

## 2. Selected High-Impact Clips

### Clip 1: Go Experience A Problem (The Conference Room Startup Fallacy)
- **Timecode:** `00:29:55` - `00:30:35` (Duration: 40s)
- **Files:**
  - Landscape (16:9): `clip_1_experience_a_problem_landscape.mp4`
  - Vertical (9:16 Shorts/Reels): `clip_1_experience_a_problem_vertical_9x16.mp4`
- **Key Quote:**
  > *"If you want to scare the shit out of me as an investor, tell me that you and two of your friends got in a conference room and wanted to start a company and decided to talk to five CIOs to figure out what their problem was. That is not what I want to hear. Go experience a problem. Airbnb needed money, they laid some mats on the floor. Yahoo couldn't find anything on the internet. Go figure out a problem that you have an inherent feel for."*
- **Best Use Case:** TikTok, YouTube Shorts, LinkedIn, Twitter/X hook for founders.

### Clip 2: Strategy Is Later: Get To 500 Customers First
- **Timecode:** `00:15:45` - `00:16:20` (Duration: 35s)
- **Files:**
  - Landscape (16:9): `clip_2_strategy_is_later_landscape.mp4`
  - Vertical (9:16 Shorts/Reels): `clip_2_strategy_is_later_vertical_9x16.mp4`
- **Key Quote:**
  > *"At the end of the day, building a company is putting one foot in front of the other. Strategy is later. Right now: execution, execution, execution. You know what a great strategy is? Get to 500 customers! That's what a great strategy is. Sell, sell, sell. Once you get to 500 customers, we'll talk about positioning and Super Bowl ads."*
- **Best Use Case:** Early-stage startup motivation, sales discipline, GTM advice.

### Clip 3: Most Board Members Are No-Ops (They Add Zero Value)
- **Timecode:** `00:21:15` - `00:22:00` (Duration: 45s)
- **Files:**
  - Landscape (16:9): `clip_3_most_board_members_noops_landscape.mp4`
  - Vertical (9:16 Shorts/Reels): `clip_3_most_board_members_noops_vertical_9x16.mp4`
- **Key Quote:**
  > *"Keep in mind that most board members—and this is going to shock you, and it's not a kind line—most board members are no-ops. You're lucky if you get a no-op board member. They do no damage, they add no value: zero. You think I'm joking? I am not joking... You want a board member who has built a business from whatever your run rate is to five times your run rate."*
- **Best Use Case:** Founder governance tips, investor relations.

### Clip 4: Architect Your Cap Table Like You Architect The Product
- **Timecode:** `00:27:50` - `00:28:40` (Duration: 50s)
- **Files:**
  - Landscape (16:9): `clip_4_architect_cap_table_landscape.mp4`
  - Vertical (9:16 Shorts/Reels): `clip_4_architect_cap_table_vertical_9x16.mp4`
- **Key Quote:**
  > *"I would tell you to architect your cap table the same way you architect the product. Don't give us this 'I got two term sheets'... Who cares? It's like going to a bar and saying 'this girl or this guy talked to me, I'm going to get married.' Look for skill sets, align equity, don't wake up 90 days in arguing over who owns what."*
- **Best Use Case:** Fundraising strategy, co-founder equity alignment.

---

## 3. End-to-End Extraction Pipeline & Automation

The extraction and editing pipeline is codified in `clips/extract_clips.py`.

### Step 1: Subtitle Extraction & Timestamp Discovery
Fetch auto-generated or manual subtitles using `yt-dlp` to pinpoint exact cue points without manual scanning:
```bash
uvx yt-dlp --write-auto-subs --sub-lang en --sub-format vtt --skip-download "https://www.youtube.com/watch?v=afSmwxT0Y3o" -o "/tmp/video.%(ext)s"
```

### Step 2: Keyframe-Accurate Stream Slicing
Download only the specified time sections directly from YouTube using HTTP range requests:
```bash
uvx yt-dlp \
  --download-sections "*<START_SEC>-<END_SEC>" \
  -f "bv*[height<=720]+ba/b[height<=720]/b" \
  --force-keyframes-at-cuts \
  "https://www.youtube.com/watch?v=afSmwxT0Y3o" \
  -o "/tmp/clip_raw.mp4"
```

### Step 3: Dual-Format Rendering (FFmpeg)
1. **16:9 Master (Universal MP4):**
   ```bash
   ffmpeg -y -i /tmp/clip_raw.mp4 \
     -c:v libx264 -preset fast -crf 22 \
     -c:a aac -b:a 192k -movflags +faststart \
     clips/clip_landscape.mp4
   ```
2. **9:16 Vertical Video (Shorts / Reels / TikTok):**
   Scales and blurs the background to fit 9:16 without distortion or black bars, placing the speaker in the center:
   ```bash
   ffmpeg -y -i /tmp/clip_raw.mp4 \
     -filter_complex "[0:v]scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,boxblur=20:5[bg];[0:v]scale=720:1280:force_original_aspect_ratio=decrease[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2" \
     -c:v libx264 -preset fast -crf 23 \
     -c:a aac -b:a 192k -movflags +faststart \
     clips/clip_vertical_9x16.mp4
   ```

---

## 4. Editing with OpenReel Video

Because we cloned [OpenReel Video](https://github.com/Augani/openreel-video) into this repository:
1. You can launch OpenReel locally:
   ```bash
   cd /home/antigravity/gdennngiamm/openreel-video
   pnpm install
   pnpm dev
   ```
2. Drag and drop any of the generated `.mp4` clips from `clips/` into the OpenReel media panel.
3. Add text captions, title cards, waveform audio visualizations, and color grading directly on the OpenReel timeline.
4. Export without watermarks at native resolutions.

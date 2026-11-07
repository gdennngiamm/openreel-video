# OpenReel Video: Viral YouTube Shorts & Subtitle Styling Guide

This guide walks you through creating high-retention YouTube Shorts, Instagram Reels, and TikTok clips using **OpenReel Video** and the pre-extracted clips and `.srt` files.

---

## 1. Launching OpenReel Video
You can edit directly in your browser:
- **Web Editor (Instant, no install):** [https://openreel.video](https://openreel.video)
- **Local Dev Build:** Run `pnpm dev` in `/home/antigravity/gdennngiamm/openreel-video`

---

## 2. Step-by-Step Shorts Workflow

### Step 1: Set Canvas to 9:16 (Vertical)
1. In OpenReel, open **Project Settings** (top toolbar or gear icon).
2. Set the aspect ratio preset to **9:16 (Portrait)** or set resolution to `1080 x 1920`.

### Step 2: Import Video & Subtitles
1. Download the clip and matching `.srt` from your Google Drive **`exports`** folder:
   - Example: `clip_1_experience_a_problem_landscape.mp4`
   - Matching subtitle: `clip_1_experience_a_problem.srt`
2. Drag both files into the OpenReel **Media Library**.
3. Drag the video onto the main video track on the timeline.
4. Drag the `.srt` file onto the dedicated **Caption / Subtitle Track** directly above the video.

### Step 3: Format the Vertical Framing (Blurred Background)
1. Duplicate the video clip onto a lower track.
2. For the background clip:
   - Scale to fill the vertical frame (`1080x1920`).
   - In the **Effects / Inspector** panel, add **Gaussian Blur** (intensity 20–30) and reduce brightness slightly (85–90%).
3. For the foreground clip (speaker):
   - Center it in the middle of the frame so Doug Leone and Mati Staniszewski are clearly visible.

### Step 4: The Viral "YouTube Shorts" Subtitle Style
To get the high-engagement Alex Hormozi / MrBeast subtitle aesthetic:
1. Select the **Caption Track** on the timeline.
2. In the right-hand **Inspector Panel**:
   - **Font Family:** Select a bold, punchy sans-serif: `Inter Bold`, `Montserrat ExtraBold`, or `Impact`.
   - **Font Size:** `48px` to `64px` (easy to read on mobile screens).
   - **Primary Color:** High-contrast `#FFFFFF` (Crisp White) or `#FFDE00` (Electric Yellow).
   - **Outline / Stroke:** Black (`#000000`), thickness `4px` to `6px`.
   - **Shadow:** Drop shadow with 40–50% opacity, distance `4px`.
   - **Vertical Alignment:** **Lower-Third** or **Center** (keep it at least 250px above the bottom so TikTok/Reels UI buttons don't block the words).
   - **Animation (Optional):** Add a subtle pop or zoom transition (scale 0.95 -> 1.05) on word/line transitions.

### Step 5: Export at Full Resolution
1. Click **Export** in the top right.
2. Select:
   - Format: **MP4 (H.264)**
   - Resolution: **1080 x 1920 (Full HD)**
   - Frame Rate: **30 fps** or **60 fps**
   - Bitrate: High / Default (no watermark)
3. Hit **Download**.

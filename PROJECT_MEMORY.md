# Project Memory & Preferences

## 1. Core Resources
- **Source Video:** [Sequoia's Doug Leone on Building Enduring Companies in the AI Era | ElevenLabs Summit London 2026](https://youtu.be/afSmwxT0Y3o)
  - URL: `https://youtu.be/afSmwxT0Y3o` (or `https://www.youtube.com/watch?v=afSmwxT0Y3o`)
  - Video ID: `afSmwxT0Y3o`
- **GitHub Repository Fork:** [gdennngiamm/openreel-video](https://github.com/gdennngiamm/openreel-video)
  - Upstream: [Augani/openreel-video](https://github.com/Augani/openreel-video)
  - Local Clone: `/home/antigravity/gdennngiamm/openreel-video`
- **Google Drive Exports Folder:** [Google Drive - exports](https://drive.google.com/drive/folders/12-3_qvcycbTaYaj5ZCBVt2IHDmmcpCcx)
  - Folder ID: `12-3_qvcycbTaYaj5ZCBVt2IHDmmcpCcx`

---

## 2. User Preferences & Standards
1. **Resolution Default:** Always export/render in **Full HD 1080p**:
   - Landscape: `1920 x 1080` (16:9)
   - Vertical: `1080 x 1920` (9:16)
2. **Subtitle & Caption Style (Viral YouTube Shorts / Reels Look):**
   - **Font:** Bold, clean sans-serif (`Roboto Bold`, `Inter Bold`, or `Montserrat ExtraBold`).
   - **Color:** Electric Yellow (`#FFDE00`) or High-Contrast White (`#FFFFFF`).
   - **Border / Stroke:** Solid Black (`#000000`), thickness `4px` - `6px` (`Outline=3` in ASS/FFmpeg).
   - **Shadow:** Subtle black drop shadow for readability on complex backgrounds.
   - **Positioning:** Lower-third / elevated (~250–280px above bottom) so it is never obscured by TikTok, Instagram Reels, or YouTube Shorts UI overlays.
3. **OpenReel Video Integration:**
   - Pre-generate synchronized `.srt` subtitle files alongside every clip.
   - OpenReel editor accessible at [https://openreel.video](https://openreel.video).
   - Support both browser-based editing in OpenReel and automated FFmpeg burn-in.

---

## 3. Extracted Clips Catalog
- **Clip 1 (`1795s - 1835s`):** *Go Experience A Problem (The Conference Room Startup Fallacy)*
- **Clip 2 (`945s - 980s`):** *Strategy Is Later: Get To 500 Customers First*
- **Clip 3 (`1275s - 1320s`):** *Most Board Members Are No-Ops (They Add Zero Value)*
- **Clip 4 (`1670s - 1720s`):** *Architect Your Cap Table Like You Architect The Product*

---

## 4. Automation Scripts
- Subtitle Generator: `clips/generate_subtitles.py`
- Clip Extractor & Transcoder: `clips/extract_clips.py`
- OpenReel Shorts Guide: `clips/OPENREEL_SHORTS_GUIDE.md`
- Process Documentation: `clips/CLIPS_PROCESS.md`
- Manifest: `clips/clips_manifest.json`

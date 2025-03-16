# Loudly Technical Test – Beat Tracking Solution

**Author:** Shiqing Tang  
**Role Applied:** AI Working Student at Loudly

---

## 🔍 Beat Tracking Approaches (beat_tracking.ipynb)

### ✅ librosa.beat.beat_track

- **Easy to use**: Simple API for detecting beats in audio.
- **Light dependency**: Relatively lightweight and widely used in academic and production environments.
- **Visualization enabled**:
  - Integrated with `librosa.display.waveshow` for easy beat visualization over waveform plots.

### ⚠️ BeatNet

- **Heavy dependency**: Requires multiple additional packages and model weights.
- **Little gain for simple cases**: Overkill for straightforward beat tracking tasks (see the comparison in ipynb).

---

## 💡 Other Thoughts

- **Generate video from photos based on audio beats**:  
  - Photos are arranged and timed to match the rhythm of a given track  
  - Uses `bonus.py` to analyze the audio  
  - Example output: [`final_with_audio.mp4`](https://github.com/shiqueenTang/loudly_test/blob/dev/final_with_audio.mp4)

- **Detect beats in audio and generate video segments accordingly**:  
  - Analyze the audio to identify rhythmic patterns and transitions  
  - Tools like [Spleeter](https://github.com/deezer/spleeter) can assist with beat tracking and segmentation

- **Real-world applications**  
  - Automated music video generation  
  - Rhythmic video editing for reels, shorts, TikToks, etc.  
  - Rapid prototyping of audio-visual experiences

- **Generative Tools (💡 the coolest part!)**  
  - Input **keywords**, **genre**, or **mood**, and let the system auto-generate videos  
  - Example: _"Make me a funky video with Bruno Marz vibes"_  
  - Potential for use in content automation, music platforms, and visual storytelling tools

---

Let the beats drive the visuals 🌀
# 💗 Birthday Wishes

A full-screen, animated, romantic birthday web experience built with
**Python + Streamlit + HTML/CSS/JS**. It plays through four scenes —
a soft opening, a birthday reveal, a magical growing "heart tree",
and a final personal message with a surprise button — then can be
shared as a single link.

This is an **original** design (pastel/glassmorphism romantic theme,
letter-by-letter reveal, procedurally-grown SVG heart tree). It does
not copy any third-party branding, watermark, or code.

---

## 1. Project structure

```
birthday-wishes/
│
├── app.py                 # the whole app (Streamlit + embedded HTML/CSS/JS)
├── requirements.txt
├── README.md
├── assets/
│   ├── birthday.mp3       # optional — add your own music here
│   └── README.txt
└── .streamlit/
    └── config.toml        # Streamlit theme settings
```

---

## 2. Install dependencies

You need Python 3.9+.

```bash
cd birthday-wishes
python -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate

pip install -r requirements.txt
```

---

## 3. Run it locally

```bash
streamlit run app.py
```

Streamlit will print a local URL (usually `http://localhost:8501`) —
open it in your browser. The app hides Streamlit's default UI so it
looks like a standalone full-screen website.

---

## 4. Personalize it

Open **`app.py`** and edit the three variables near the top of the
file — no HTML/JS knowledge needed:

```python
BIRTHDAY_NAME = "Ava"

PERSONAL_MESSAGE = (
    "May your day be filled with happiness, love, beautiful memories "
    "and everything that makes you smile."
)

SURPRISE_MESSAGE = "Today is your day. Keep smiling and keep shining. ❤️"
```

- **`BIRTHDAY_NAME`** — shows up as "Happy Birthday, *Name* ❤️" on the
  final scene.
- **`PERSONAL_MESSAGE`** — the message shown under the name.
- **`SURPRISE_MESSAGE`** — revealed when the "Click for a Surprise ❤️"
  button is pressed.

Save the file and refresh your browser (or re-run `streamlit run app.py`).

---

## 5. Add your own music (optional)

1. Find/create an MP3 you have the rights to use.
2. Rename it to `birthday.mp3`.
3. Put it in the `assets/` folder, replacing the placeholder:

   ```
   birthday-wishes/assets/birthday.mp3
   ```

4. Restart the app. A small round music button will now appear in the
   bottom-right corner, letting the visitor play/pause the track.

If no file is present at `assets/birthday.mp3`, the app runs exactly
the same — the music button just doesn't appear. No extra
configuration needed.

> The audio file is embedded directly into the page (base64) so it
> works out-of-the-box on Streamlit Community Cloud with no extra
> static-file hosting setup.

---

## 6. Push the project to GitHub

```bash
cd birthday-wishes
git init
git add .
git commit -m "Birthday wishes app"

# create a new empty repo on GitHub first, then:
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

> If your `birthday.mp3` file is large, GitHub's normal size limits
> still apply (100 MB per file on standard repos). Keep the track
> short/compressed for best results.

---

## 7. Deploy on Streamlit Community Cloud

1. Go to **https://share.streamlit.io** and sign in with GitHub.
2. Click **"New app"**.
3. Choose the repository and branch you just pushed.
4. Set **Main file path** to:
   ```
   app.py
   ```
5. Click **Deploy**.
6. Streamlit Cloud will install `requirements.txt` automatically and
   give you a public URL like:
   ```
   https://<your-app-name>.streamlit.app
   ```
7. Share that URL with the birthday person 🎉

Whenever you push new commits (e.g. after changing `BIRTHDAY_NAME`),
Streamlit Community Cloud redeploys automatically.

---

## 8. How the experience works

| Scene | What happens |
|---|---|
| 1 — Opening | Soft gradient background, a pulsing heart, floating particles, and the line *"Someone special has a little surprise for you…"*. Auto-advances after ~4 seconds (or tap to skip). |
| 2 — Reveal | *"Happy Birthday ❤️"* animates in letter by letter with sparkles and floating hearts. |
| 3 — Growing tree | A tree grows branch by branch (pure SVG, animated with CSS), then blossoms into a heart-shaped crown made of many small hearts. |
| 4 — Final message | The completed heart tree, the personalized name + message, and a **"Click for a Surprise ❤️"** button that releases a burst of hearts/sparkles and reveals a bonus message. |

Everything — the tree growth, hearts, sparkles, and scene transitions —
is done with CSS animations, inline SVG, and vanilla JavaScript inside
a single `st.components.v1.html()` component, so no extra JS
libraries or backend are required.

---

## 9. Notes

- No API keys, backend, or database required.
- No copyrighted music is bundled — you supply your own (optional).
- Works on desktop, tablet, and mobile (responsive layout + `vw`/`vh`
  based sizing).
- Streamlit's default chrome (menu, header, footer, padding) is
  hidden via CSS so the page reads as a standalone site rather than a
  dashboard.
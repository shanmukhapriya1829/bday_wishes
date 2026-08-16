"""
Birthday Wishes — a full-screen animated birthday experience
built with Streamlit + HTML/CSS/JS.

Run locally:
    streamlit run app.py

Deploy on Streamlit Community Cloud — see README.md.
"""

import base64
import html
import os

import streamlit as st

# ============================================================
# 🎂  PERSONALISE YOUR BIRTHDAY MESSAGE HERE
# ============================================================
BIRTHDAY_NAME = "Nani"
PERSONAL_MESSAGE = (
    "May your day be filled with happiness, love, beautiful memories "
    "and everything that makes you smile."
)
SURPRISE_MESSAGE = "Today is your day. Keep smiling and keep shining. ❤️"

# Optional: put an .mp3 file at this path to enable background music.
AUDIO_PATH = os.path.join("assets", "birthday.mp3")
CAKE_IMAGE_PATH = os.path.join("assets", "birthday_cake.png")
# ============================================================


st.set_page_config(
    page_title=f"Happy Birthday {BIRTHDAY_NAME}",
    page_icon="💗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --------------------------------------------------------------
# Hide Streamlit chrome and stretch the component to fill the
# whole viewport so the app feels like a standalone website.
# --------------------------------------------------------------
st.markdown(
    """
    <style>
        #MainMenu, header, footer {visibility: hidden; height: 0;}
        div[data-testid="stToolbar"] {visibility: hidden; height: 0;}
        div[data-testid="stDecoration"] {visibility: hidden; height: 0;}
        div[data-testid="stStatusWidget"] {visibility: hidden; height: 0;}
        .block-container {padding: 0 !important; margin: 0 !important; max-width: 100% !important;}
        section[data-testid="stMain"] {padding: 0 !important;}
        html, body {overflow: hidden; margin: 0; padding: 0; background: #fff6f2;}
        iframe {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            border: none !important;
        }
    
  /* ---------- REAL DOWNLOADED CAKE IMAGE ---------- */
  .cake-card{
    position:relative !important;
    overflow:hidden !important;
    min-height:720px !important;
    justify-content:flex-start !important;
  }
  .cake-stage{
    position:relative !important;
    width:100% !important;
    height:500px !important;
    flex:0 0 500px !important;
    display:flex !important;
    align-items:flex-end !important;
    justify-content:center !important;
  }
  .cake-aura{
    position:absolute !important;
    width:520px !important;height:320px !important;
    left:50% !important;bottom:20px !important;
    transform:translateX(-50%) !important;
    border-radius:50% !important;
    background:radial-gradient(ellipse,rgba(255,120,170,.45),transparent 72%) !important;
    filter:blur(14px) !important;
    animation:cakeAura 2.3s ease-in-out infinite alternate !important;
    z-index:1 !important;
  }
  @keyframes cakeAura{
    from{opacity:.55;transform:translateX(-50%) scale(.94)}
    to{opacity:1;transform:translateX(-50%) scale(1.08)}
  }
  .cake-sparkles{
    position:absolute !important;inset:30px 6% 50px !important;
    z-index:20 !important;pointer-events:none !important;
  }
  .cake-sparkles span{
    position:absolute !important;color:#d84e76 !important;
    font-size:28px !important;
    text-shadow:0 0 10px rgba(255,150,185,.6) !important;
    animation:cakeSpark 1.8s ease-in-out infinite alternate !important;
  }
  .cake-sparkles span:nth-child(1){left:8%;top:28%}
  .cake-sparkles span:nth-child(2){right:8%;top:35%;animation-delay:.4s}
  .cake-sparkles span:nth-child(3){left:14%;top:65%;animation-delay:.8s}
  .cake-sparkles span:nth-child(4){right:14%;top:68%;animation-delay:1.1s}
  @keyframes cakeSpark{
    to{transform:translateY(-14px) rotate(20deg) scale(1.2);opacity:.45}
  }
  .real-cake-wrap{
    position:relative !important;
    width:min(540px,92vw) !important;
    height:475px !important;
    margin-bottom:5px !important;
    display:flex !important;
    align-items:flex-end !important;
    justify-content:center !important;
    z-index:10 !important;
    animation:realCakeFloat 3.2s ease-in-out infinite !important;
  }
  .real-cake{
    display:block !important;
    width:min(490px,88vw) !important;
    max-height:465px !important;
    height:auto !important;
    object-fit:contain !important;
    object-position:center bottom !important;
    filter:drop-shadow(0 18px 20px rgba(80,30,50,.23)) !important;
    user-select:none !important;
    -webkit-user-drag:none !important;
  }
  @keyframes realCakeFloat{
    0%,100%{transform:translateY(0)}
    50%{transform:translateY(-8px)}
  }
  .cake-cut-glow{
    position:absolute !important;
    left:50% !important;top:13% !important;
    width:7px !important;height:72% !important;
    transform:translateX(-50%) scaleY(0) !important;
    transform-origin:top !important;opacity:0 !important;
    border-radius:10px !important;
    background:linear-gradient(180deg,transparent,#fff,#ff3f72,#fff,transparent) !important;
    box-shadow:0 0 18px #fff,0 0 30px rgba(255,50,110,.9) !important;
    z-index:30 !important;
  }
  .big-knife{
    position:absolute !important;right:3% !important;top:75px !important;
    width:90px !important;height:230px !important;
    z-index:40 !important;opacity:0 !important;
    transform:rotate(-25deg) !important;pointer-events:none !important;
  }
  .knife-blade{
    position:absolute !important;left:30px !important;top:0 !important;
    width:23px !important;height:150px !important;
    border-radius:12px 12px 4px 4px !important;
    background:linear-gradient(90deg,#8d969e,#fff 45%,#a9b0b8) !important;
    box-shadow:0 4px 8px rgba(50,50,50,.3) !important;
  }
  .knife-handle{
    position:absolute !important;left:18px !important;top:135px !important;
    width:48px !important;height:88px !important;
    border-radius:12px 12px 20px 20px !important;
    background:linear-gradient(90deg,#351f2a,#a23c5d,#402430) !important;
    box-shadow:0 6px 10px rgba(50,20,30,.3) !important;
  }
  .cake-card.cutting .big-knife{
    animation:realKnifeCut 1.5s cubic-bezier(.2,.8,.2,1) forwards !important;
  }
  @keyframes realKnifeCut{
    0%{opacity:0;transform:translate(140px,-60px) rotate(-25deg)}
    12%{opacity:1}
    45%{opacity:1;transform:translate(5px,65px) rotate(2deg)}
    72%{transform:translate(-15px,155px) rotate(8deg)}
    100%{opacity:1;transform:translate(-30px,205px) rotate(12deg)}
  }
  .cake-card.cutting .cake-cut-glow{
    animation:realCutLine 1.15s ease .35s forwards !important;
  }
  @keyframes realCutLine{
    0%{opacity:0;transform:translateX(-50%) scaleY(0)}
    30%{opacity:1;transform:translateX(-50%) scaleY(1)}
    100%{opacity:0;transform:translateX(-50%) scaleY(1)}
  }
  .cake-card.cutting .real-cake-wrap{
    animation:realCakeShake .7s ease .35s !important;
  }
  @keyframes realCakeShake{
    0%,100%{transform:translateX(0)}
    20%{transform:translateX(-7px) rotate(-1deg)}
    40%{transform:translateX(7px) rotate(1deg)}
    60%{transform:translateX(-5px)}
    80%{transform:translateX(3px)}
  }
  .cake-title{
    margin:4px 0 8px !important;color:var(--plum) !important;
    font-size:30px !important;
  }
  .cake-subtitle{
    margin:0 0 20px !important;color:var(--plum-soft) !important;
    font-size:17px !important;
  }
  .cake-btn{
    border:0 !important;border-radius:999px !important;
    padding:15px 30px !important;
    background:linear-gradient(135deg,#df6484,#b73559) !important;
    color:#fff !important;font:700 17px 'Quicksand',sans-serif !important;
    cursor:pointer !important;box-shadow:0 10px 25px rgba(183,53,89,.32) !important;
  }
  @media(max-width:520px){
    .cake-card{min-height:650px !important}
    .cake-stage{height:420px !important;flex-basis:420px !important}
    .real-cake-wrap{height:395px !important;width:96vw !important}
    .real-cake{width:94vw !important;max-height:390px !important}
    .cake-title{font-size:23px !important}
    .cake-subtitle{font-size:15px !important}
    .big-knife{right:-2% !important}
  }

</style>
    """,
    unsafe_allow_html=True,
)


def _load_audio_base64(path: str):
    """Return a base64 data-URI for the audio file if it exists."""
    if os.path.isfile(path):
        with open(path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
        return f"data:audio/mpeg;base64,{encoded}"
    return None



def _load_image_base64(path: str):
    """Return a base64 data-URI for the local cake image if it exists."""
    if os.path.isfile(path):
        with open(path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
        return f"data:image/png;base64,{encoded}"
    return ""


cake_data_uri = _load_image_base64(CAKE_IMAGE_PATH)

audio_data_uri = _load_audio_base64(AUDIO_PATH)
has_audio = "true" if audio_data_uri else "false"
audio_src = audio_data_uri or ""


def _escape_js(text: str) -> str:
    """Make a Python string safe to drop inside a JS template literal."""
    return text.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")


HTML_TEMPLATE = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;1,500&family=Quicksand:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root{
    --cream:#fff6f2;
    --blush:#f7dde3;
    --blush-2:#f2c7d2;
    --rose:#d9738f;
    --deep-rose:#b23a56;
    --plum:#4a2a3a;
    --plum-soft:#7a5063;
    --gold:#e3b873;
    --trunk:#8a5a44;
  }
  *{box-sizing:border-box; -webkit-tap-highlight-color:transparent;}
  html,body{
    margin:0; padding:0; width:100%; height:100%;
    overflow:hidden;
    font-family:'Quicksand', sans-serif;
    background:linear-gradient(160deg, var(--cream) 0%, var(--blush) 55%, var(--blush-2) 100%);
    -webkit-font-smoothing:antialiased;
  }
  #stage{
    position:relative;
    width:100vw; height:100vh;
    overflow:hidden;
  }
  .scene{
    position:absolute; inset:0;
    display:flex;
    flex-direction:column;
    text-align:center;
    padding:6vw;
    opacity:0;
    visibility:hidden;
    transform:scale(0.94);
    transition:opacity 1.1s ease, transform 1.3s ease, visibility 0s linear 1.1s;
    pointer-events:none;
    overflow-y:auto;
    -webkit-overflow-scrolling:touch;
    scrollbar-width:none;
  }
  .scene::-webkit-scrollbar{display:none;}
  /* margin:auto on the card (rather than justify/align-content:center on the
     parent) centers it when it fits, but still scrolls cleanly from the very
     top when the card is taller than the viewport — centering via
     justify-content on an overflowing flex container would otherwise make
     the top of the content unreachable. */
  .scene > .glass-card{margin:auto;}
  .scene.active{
    opacity:1;
    visibility:visible;
    transform:scale(1);
    transition:opacity 1.1s ease, transform 1.3s ease;
    pointer-events:auto;
  }

  /* ---------- soft ambient background shapes ---------- */
  .bg-glow{
    position:absolute; border-radius:50%;
    filter:blur(60px);
    opacity:0.55;
    pointer-events:none;
  }
  .bg-glow.g1{width:38vw;height:38vw; top:-10vw; left:-8vw; background:radial-gradient(circle, var(--blush-2), transparent 70%);}
  .bg-glow.g2{width:44vw;height:44vw; bottom:-16vw; right:-10vw; background:radial-gradient(circle, var(--gold), transparent 70%); opacity:0.28;}

  /* ---------- particles (hearts / sparkles) ---------- */
  .particle-layer{position:absolute; inset:0; overflow:hidden; pointer-events:none;}
  .p-heart, .p-spark{
    position:absolute;
    bottom:-8vh;
    opacity:0;
    animation-name:floatUp;
    animation-timing-function:ease-in;
    animation-iteration-count:infinite;
  }
  .p-heart{color:var(--rose); filter:drop-shadow(0 2px 6px rgba(178,58,86,0.25));}
  .p-spark{color:var(--gold);}
  @keyframes floatUp{
    0%{ transform:translateY(0) translateX(0) rotate(0deg) scale(0.6); opacity:0;}
    10%{opacity:0.9;}
    50%{ transform:translateY(-55vh) translateX(var(--drift,10px)) rotate(180deg) scale(1);}
    90%{opacity:0.7;}
    100%{ transform:translateY(-105vh) translateX(calc(var(--drift,10px) * 2)) rotate(360deg) scale(0.5); opacity:0;}
  }

  /* ---------- Scene 1 : opening ---------- */
  .pulse-heart{
    width:56px; height:56px;
    animation:pulse 1.6s ease-in-out infinite;
    filter:drop-shadow(0 6px 14px rgba(178,58,86,0.35));
    margin-bottom:28px;
  }
  @keyframes pulse{
    0%,100%{transform:scale(1);}
    50%{transform:scale(1.18);}
  }
  .opening-text{
    font-family:'Playfair Display', serif;
    font-style:italic;
    font-weight:500;
    font-size:clamp(1.1rem, 2.6vw, 1.7rem);
    color:var(--plum-soft);
    letter-spacing:0.02em;
    max-width:640px;
    opacity:0;
    animation:fadeInSlow 1.8s ease 0.4s forwards;
  }
  @keyframes fadeInSlow{
    from{opacity:0; transform:translateY(14px);}
    to{opacity:1; transform:translateY(0);}
  }
  .hint{
    margin-top:38px;
    font-size:0.78rem;
    letter-spacing:0.14em;
    text-transform:uppercase;
    color:var(--plum-soft);
    opacity:0;
    animation:fadeInSlow 1.4s ease 2s forwards;
  }

  /* ---------- Scene 2 : reveal ---------- */
  .reveal-title{
    font-family:'Playfair Display', serif;
    font-weight:600;
    font-size:clamp(2.4rem, 8vw, 5.2rem);
    color:var(--deep-rose);
    line-height:1.15;
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    gap:0.05em;
    text-shadow:0 6px 24px rgba(178,58,86,0.18);
  }
  .reveal-title .ch{
    display:inline-block;
    opacity:0;
    transform:translateY(28px) rotate(4deg);
    animation:letterIn 0.7s cubic-bezier(.2,.9,.3,1.4) forwards;
  }
  @keyframes letterIn{
    to{opacity:1; transform:translateY(0) rotate(0);}
  }
  .reveal-sub{
    margin-top:18px;
    font-size:clamp(0.95rem,2.2vw,1.2rem);
    color:var(--plum-soft);
    opacity:0;
    animation:fadeInSlow 1.2s ease 1.8s forwards;
    letter-spacing:0.03em;
  }

  /* ---------- Scene 3 : growing tree ---------- */
  .tree-wrap{
    width:min(90vw, 560px);
    height:min(62vh, 560px);
  }
  .tree-wrap svg{width:100%; height:100%; overflow:visible;}
  .branch{
    fill:none;
    stroke:var(--trunk);
    stroke-linecap:round;
    stroke-linejoin:round;
  }
  .heart-leaf{
    transform-origin:center;
    opacity:0;
    transform:scale(0);
    animation:bloom 0.6s cubic-bezier(.25,1.4,.4,1) forwards;
  }
  @keyframes bloom{
    to{opacity:1; transform:scale(1);}
  }
  .tree-caption{
    margin-top:10px;
    font-family:'Playfair Display', serif;
    font-style:italic;
    color:var(--plum-soft);
    font-size:clamp(0.95rem,2.2vw,1.15rem);
    opacity:0;
    animation:fadeInSlow 1.4s ease 3.6s forwards;
  }

  /* ---------- Scene 4 : final message ---------- */
  .final-tree{width:min(60vw, 300px); height:min(34vh,300px); margin-bottom:6px;}
  .final-tree svg{width:100%; height:100%; overflow:visible;}
  .final-name{
    font-family:'Playfair Display', serif;
    font-weight:600;
    font-size:clamp(1.8rem, 5.5vw, 3.2rem);
    color:var(--deep-rose);
    margin:6px 0 10px;
    text-shadow:0 4px 18px rgba(178,58,86,0.16);
  }
  .final-message{
    max-width:560px;
    font-size:clamp(0.95rem,2.3vw,1.15rem);
    color:var(--plum-soft);
    line-height:1.7;
    margin-bottom:26px;
  }
  .surprise-btn{
    font-family:'Quicksand', sans-serif;
    font-weight:700;
    font-size:1rem;
    letter-spacing:0.02em;
    color:#fff;
    background:linear-gradient(135deg, var(--rose), var(--deep-rose));
    border:none;
    padding:14px 30px;
    border-radius:999px;
    cursor:pointer;
    box-shadow:0 10px 26px rgba(178,58,86,0.35), inset 0 1px 0 rgba(255,255,255,0.35);
    transition:transform 0.25s ease, box-shadow 0.25s ease;
    backdrop-filter:blur(6px);
  }
  .surprise-btn:hover{transform:translateY(-3px) scale(1.03); box-shadow:0 14px 30px rgba(178,58,86,0.42);}
  .surprise-btn:active{transform:translateY(0) scale(0.98);}
  .surprise-text{
    margin-top:22px;
    max-width:520px;
    font-family:'Playfair Display', serif;
    font-style:italic;
    font-size:clamp(1.05rem,2.6vw,1.35rem);
    color:var(--deep-rose);
    opacity:0;
    transform:translateY(10px);
    transition:opacity 0.8s ease, transform 0.8s ease;
  }
  .surprise-text.show{opacity:1; transform:translateY(0);}

  /* glassmorphism card wrapper used across scenes */
  .glass-card{
    background:rgba(255,255,255,0.38);
    border:1px solid rgba(255,255,255,0.55);
    border-radius:28px;
    padding:clamp(18px, 3.5vh, 44px) clamp(22px, 4vw, 44px);
    backdrop-filter:blur(14px);
    -webkit-backdrop-filter:blur(14px);
    box-shadow:0 20px 50px rgba(178,58,86,0.10);
    display:flex; flex-direction:column; align-items:center;
  }

  /* ---------- music control ---------- */
  #music-toggle{
    position:absolute;
    bottom:22px; right:22px;
    width:52px; height:52px;
    border-radius:50%;
    background:rgba(255,255,255,0.55);
    border:1px solid rgba(255,255,255,0.7);
    backdrop-filter:blur(10px);
    display:flex; align-items:center; justify-content:center;
    cursor:pointer;
    box-shadow:0 8px 20px rgba(178,58,86,0.18);
    z-index:50;
    transition:transform 0.2s ease;
  }
  #music-toggle:hover{transform:scale(1.08);}
  #music-toggle svg{width:22px;height:22px; color:var(--deep-rose);}

  @media (max-width:520px){
    .glass-card{border-radius:22px;}
    #music-toggle{width:46px;height:46px; bottom:16px; right:16px;}
  }

  ::selection{background:var(--blush-2);}
</style>
</head>
<body>

<div id="stage">
  <div class="bg-glow g1"></div>
  <div class="bg-glow g2"></div>
  <div class="particle-layer" id="particleLayer"></div>

  <!-- SCENE 1 : OPENING -->
  <section class="scene active" id="scene1">
    <div class="glass-card">
      <svg class="pulse-heart" viewBox="0 0 32 29" fill="var(--rose)">
        <path d="M16 28.5c-.4 0-.8-.15-1.1-.4C7.4 22.2 2 17.4 2 11.2 2 6.6 5.6 3 10.1 3c2.5 0 4.9 1.2 6.4 3.1C18 4.2 20.4 3 22.9 3 27.4 3 31 6.6 31 11.2c0 6.2-5.4 11-12.9 17-.3.2-.7.3-1.1.3Z"/>
      </svg>
      <p class="opening-text">Someone special has a little surprise for you&hellip;</p>
      <p class="hint">tap anywhere to continue</p>
    </div>
  </section>

  <!-- SCENE 2 : REVEAL -->
  <section class="scene" id="scene2">
    <div class="glass-card">
      <h1 class="reveal-title" id="revealTitle"></h1>
      <p class="reveal-sub">A little something is growing for you&hellip;</p>
    </div>
  </section>

  <!-- SCENE 3 : REAL CAKE IMAGE + ANIMATED CUTTING -->
  <section class="scene" id="scene3">
    <div class="glass-card cake-card">
      <div class="cake-stage">
        <div class="cake-aura"></div>
        <div class="cake-sparkles">
          <span>✦</span><span>✧</span><span>♥</span><span>✦</span>
        </div>

        <div class="real-cake-wrap" id="realCakeWrap">
          <img class="real-cake" id="realCake" src="{{CAKE_SRC}}" alt="Birthday cake">
          <div class="cake-cut-glow"></div>
        </div>

        <div class="big-knife" id="bigKnife">
          <div class="knife-blade"></div>
          <div class="knife-handle"></div>
        </div>
      </div>

      <h2 class="cake-title">Make a wish, {{BIRTHDAY_NAME}} 🎂</h2>
      <p class="cake-subtitle" id="cakeSubtitle">Your birthday cake is ready! ✨</p>
      <button class="cake-btn" id="cutCakeBtn">🔪 Cut the Cake 🎂</button>
    </div>
  </section>

  <!-- SCENE 4 : FINAL MESSAGE -->
  <section class="scene" id="scene4">
    <div class="glass-card">
<h2 class="final-name">Happy Birthday, {{BIRTHDAY_NAME}} ❤️</h2>
      <p class="final-message">{{PERSONAL_MESSAGE}}</p>
      <button class="surprise-btn" id="surpriseBtn">Click for a Surprise ❤️</button>
      <p class="surprise-text" id="surpriseText">{{SURPRISE_MESSAGE}}</p>
    </div>
  </section>

  <div id="music-toggle" style="display:{{MUSIC_DISPLAY}};">
    <svg id="musicIconPlay" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
    <svg id="musicIconPause" viewBox="0 0 24 24" fill="currentColor" style="display:none;"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>
  </div>
  <audio id="bgAudio" loop preload="none">
    <source src="{{AUDIO_SRC}}" type="audio/mpeg">
  </audio>
</div>

<script>
(function(){
  const HAS_AUDIO = {{HAS_AUDIO}};
  const NAME = `{{NAME_JS}}`;

  /* ---------------- particles ---------------- */
  const layer = document.getElementById('particleLayer');
  const heartPath = "M16 28.5c-.4 0-.8-.15-1.1-.4C7.4 22.2 2 17.4 2 11.2 2 6.6 5.6 3 10.1 3c2.5 0 4.9 1.2 6.4 3.1C18 4.2 20.4 3 22.9 3 27.4 3 31 6.6 31 11.2c0 6.2-5.4 11-12.9 17-.3.2-.7.3-1.1.3Z";

  function spawnParticle(kind){
    const el = document.createElement('div');
    const size = 10 + Math.random()*16;
    const left = Math.random()*100;
    const duration = 6 + Math.random()*6;
    const drift = (Math.random()*80 - 40) + 'px';
    el.style.left = left + 'vw';
    el.style.setProperty('--drift', drift);
    el.style.animationDuration = duration + 's';
    el.style.animationDelay = (Math.random()*2) + 's';

    if(kind === 'heart'){
      el.className = 'p-heart';
      el.innerHTML = `<svg width="${size}" height="${size*0.9}" viewBox="0 0 32 29" fill="currentColor"><path d="${heartPath}"/></svg>`;
    } else {
      el.className = 'p-spark';
      const s = size*0.6;
      el.innerHTML = `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0l2.2 8.8L23 11l-8.8 2.2L12 22l-2.2-8.8L1 11l8.8-2.2z"/></svg>`;
    }
    layer.appendChild(el);
    setTimeout(()=>el.remove(), (duration+2)*1000);
  }
  setInterval(()=>spawnParticle(Math.random()>0.55?'heart':'spark'), 550);
  for(let i=0;i<6;i++) setTimeout(()=>spawnParticle('heart'), i*300);

  /* ---------------- scene machine ---------------- */
  const scenes = ['scene1','scene2','scene3','scene4'].map(id=>document.getElementById(id));
  let current = 0;
  let advanced = {1:false, 2:false, 3:false};


  // ---------- premium cake cutting ----------
  let cakeCut = false;

  function cakeCelebration(){
    const layer=document.getElementById('particleLayer'); if(!layer) return;
    const symbols=['♥','❤','✦','✧','✨','🎉'], colors=['#d64f72','#e36d8c','#f19ab0','#f6c2cf','#d9a441'];
    for(let i=0;i<95;i++){
      const el=document.createElement('span');
      el.textContent=symbols[Math.floor(Math.random()*symbols.length)];
      el.style.position='absolute'; el.style.left=(44+Math.random()*12)+'vw'; el.style.top=(48+Math.random()*9)+'vh';
      el.style.fontSize=(13+Math.random()*20)+'px'; el.style.color=colors[Math.floor(Math.random()*colors.length)];
      el.style.zIndex='60'; el.style.pointerEvents='none';
      el.style.transition='transform 1.8s cubic-bezier(.15,.8,.2,1),opacity 1.8s ease';
      layer.appendChild(el);
      requestAnimationFrame(()=>{el.style.transform=`translate(${(Math.random()-.5)*560}px,${-100-Math.random()*360}px) rotate(${Math.random()*900-450}deg)`;el.style.opacity='0';});
      setTimeout(()=>el.remove(),2100);
    }
  }

  function blowCandles(){
    document.querySelectorAll('.flame').forEach((flame,i)=>{
      setTimeout(()=>{flame.style.animation='none';flame.style.opacity='0';flame.style.transform='translateX(-50%) scale(.2)';flame.style.transition='all .45s ease';},i*90);
    });
  }

  function setupCake(){
    const btn=document.getElementById('cutCakeBtn');
    const card=document.querySelector('.cake-card');
    const subtitle=document.getElementById('cakeSubtitle');
    if(!btn || !card || !subtitle || btn.dataset.ready) return;
    btn.dataset.ready='1';

    btn.addEventListener('click',()=>{
      if(cakeCut) return;
      cakeCut=true;
      card.classList.add('cutting');
      btn.disabled=true;
      btn.innerHTML='✨ Cutting the Cake... ✨';
      subtitle.textContent='Make a wish and watch the magic happen...';

      setTimeout(()=>cakeCelebration(),950);

      setTimeout(()=>{
        card.classList.remove('cutting');
        card.classList.add('cut-complete');
        subtitle.textContent='Cake cut! Happy Birthday! 🎉❤️';
        btn.style.opacity='0';
        btn.style.transform='scale(.7)';
        setTimeout(()=>goTo(3),2200);
      },1750);
    });
  }

  function goTo(index){
    if(index===current) return;
    scenes[current].classList.remove('active');
    current=index; scenes[current].classList.add('active');
    if(current===1) runReveal();
    if(current===2) setupCake();
  }

  scenes[0].addEventListener('click',()=>{if(current===0) goTo(1);});
  scenes[1].addEventListener('click',()=>{if(current===1) goTo(2);});
  setTimeout(()=>{if(current===0) goTo(1);},4200);

  /* ---------------- scene 2 : letter reveal ---------------- */
  function runReveal(){
    const title=document.getElementById('revealTitle');
    if(title.dataset.built){scheduleAdvance();return;}
    title.dataset.built='1'; const revealText='Happy Birthday ❤️'; let delay=0;
    [...revealText].forEach(ch=>{const span=document.createElement('span');span.className='ch';span.textContent=ch===' '?'\u00A0':ch;span.style.animationDelay=delay+'s';title.appendChild(span);delay+=.06;});
    scheduleAdvance();
  }
  function scheduleAdvance(){setTimeout(()=>{if(current===1) goTo(2);},5200);}

  /* ---------------- scene 4 : surprise button ---------------- */
  const surpriseBtn = document.getElementById('surpriseBtn');
  const surpriseText = document.getElementById('surpriseText');
  surpriseBtn.addEventListener('click', ()=>{
    surpriseText.classList.add('show');
    for(let i=0;i<26;i++){
      setTimeout(()=>spawnParticle(Math.random()>0.4 ? 'heart':'spark'), i*45);
    }
    surpriseBtn.style.transform = 'scale(0.96)';
    setTimeout(()=> surpriseBtn.style.transform = '', 180);
  });

  /* ---------------- music control ---------------- */
  if(HAS_AUDIO){
    const audio = document.getElementById('bgAudio');
    const toggle = document.getElementById('music-toggle');
    const playIcon = document.getElementById('musicIconPlay');
    const pauseIcon = document.getElementById('musicIconPause');
    let playing = false;
    toggle.addEventListener('click', ()=>{
      if(!playing){
        audio.play().catch(()=>{});
        playing = true;
        playIcon.style.display='none';
        pauseIcon.style.display='block';
      } else {
        audio.pause();
        playing = false;
        playIcon.style.display='block';
        pauseIcon.style.display='none';
      }
    });
  }
})();
</script>
</body>
</html>
"""

html_out = (
    HTML_TEMPLATE.replace("{{BIRTHDAY_NAME}}", html.escape(BIRTHDAY_NAME))
    .replace("{{PERSONAL_MESSAGE}}", html.escape(PERSONAL_MESSAGE))
    .replace("{{SURPRISE_MESSAGE}}", html.escape(SURPRISE_MESSAGE))
    .replace("{{MUSIC_DISPLAY}}", "flex" if audio_data_uri else "none")
    .replace("{{AUDIO_SRC}}", audio_src)
    .replace("{{HAS_AUDIO}}", has_audio)
    .replace("{{NAME_JS}}", _escape_js(BIRTHDAY_NAME))
    .replace("{{CAKE_SRC}}", cake_data_uri)
)

st.components.v1.html(html_out, height=1000, scrolling=False)
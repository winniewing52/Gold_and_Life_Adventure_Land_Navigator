# ⚔️ Gold & Life — Adventure Land Navigator
 
A Python-based strategy game where you navigate a crew of adventurers across dungeons, castles, and forests to collect gold while battling guardians.
 
## 🗺️ Overview
 
You play as a **navigator** guiding adventurers to raid land sites, each containing a stash of gold guarded by monsters. Your goal is to make optimal decisions — choosing which sites to raid and how many adventurers to send — to maximise your rewards.
 
Each land site (`Land`) has three properties:
- `name` — identifier for the site
- `gold` — the reward available
- `guardians` — enemies defending the site
 
## 🎮 Game Modes
 
### Mode 1 — Solo Expedition
Raid land sites across multiple days with a fixed crew. For each site with `g` guardians and `r` gold, sending `c` adventurers yields:
 
```
reward = min(c/g * r, r)
```
 
Adventurers sent to a site are lost in battle. Once a site is raided, it has no gold or guardians remaining.
 
### Mode 2 — The Fair Fight
Compete against other navigator teams in a turn-based qualifying game. Each team selects one site per day to maximise their daily score:
 
```
score = 2.5 × remaining_adventurers + gold_gained
```
 
All team leaders play optimally. The highest scorer wins.

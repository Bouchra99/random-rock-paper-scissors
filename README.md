## Random Rock-Paper-Scissors ⛰📄✂️

A coworker once sent me a reel of a streamer playing a quirky, chaotic game.  
It looked like *a lot* of fun — so I decided to recreate it in Python using Pygame.  

While talking about it, my coworker shared an interesting observation:  
> *"In this game, if you destroy your enemy, you end up getting destroyed too."*  

That felt oddly philosophical — and also hilarious.  
So here it is: a fast-paced, autonomous twist on the classic rock-paper-scissors.

Enjoy. 🎮

---

### 🎯 Game Overview
- **Rock** beats **Scissors**  
- **Scissors** beat **Paper**  
- **Paper** beats **Rock**  
- But here, *victory can still lead to your own destruction*.  

Each player **starts with a team of three**:
- 1 Rock
- 1 Paper
- 1 Scissors  

Once the match starts:
- All pieces **move and battle automatically**
- You **don’t control anything** — just watch the chaos unfold
- Score points for each victory; survivors get massive end-of-game bonuses

Random pickups appear to stir things up:
- 🧬 **Clone** → duplicate one of your objects
- ❄ **Freeze** → temporarily stop all other players

---

### 🖥️ How to Play
1. Run the game.
```bash
uv run main.py
```
2. Watch the match play out automatically.
3. See who scores the most points when the dust settles.

---

### 📦 Requirements
- [Pygame](https://www.pygame.org/)

Install dependencies with **uv**:
```bash
uv add pygame

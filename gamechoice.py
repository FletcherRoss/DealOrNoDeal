import streamlit as st
import random

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(page_title="Briefcase Game", page_icon="💼", layout="wide")

# ─────────────────────────────────────────────────────────────────────────────
# STYLING
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500&display=swap');

*, body, html { font-family: 'DM Sans', sans-serif; }
.main { background: #0a0a0f; }
.block-container { padding: 1.5rem 2rem 3rem; max-width: 1100px; }

h1, h2, h3 { font-family: 'Playfair Display', serif !important; }

/* ── Title ── */
.game-title {
    font-family: 'Playfair Display', serif;
    font-size: 3.8rem;
    font-weight: 900;
    color: #f0e6c8;
    letter-spacing: -1px;
    line-height: 1;
    text-shadow: 0 0 60px rgba(212,175,55,0.3);
}
.game-subtitle {
    color: #7a6e58;
    font-size: 0.9rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-top: 4px;
    margin-bottom: 2rem;
}

/* ── Game cards ── */
.game-card {
    background: linear-gradient(135deg, #13131f 0%, #0e0e18 100%);
    border: 1px solid #2a2540;
    border-radius: 16px;
    padding: 1.4rem 1.6rem;
    cursor: pointer;
    transition: all 0.2s;
    height: 100%;
}
.game-card:hover { border-color: #d4af37; transform: translateY(-2px); }
.game-card-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.15rem;
    color: #f0e6c8;
    margin-bottom: 0.4rem;
}
.game-card-cats {
    font-size: 0.75rem;
    color: #5a5468;
    line-height: 1.6;
}
.game-card-emoji { font-size: 2rem; margin-bottom: 0.6rem; }

/* ── Section labels ── */
.section-label {
    font-size: 0.7rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #d4af37;
    margin-bottom: 0.5rem;
}
.round-banner {
    background: linear-gradient(90deg, #1a1628 0%, #120f1e 100%);
    border: 1px solid #2a2540;
    border-left: 3px solid #d4af37;
    border-radius: 10px;
    padding: 1rem 1.4rem;
    margin-bottom: 1.2rem;
}
.round-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    color: #f0e6c8;
}
.round-category {
    font-size: 0.78rem;
    color: #d4af37;
    letter-spacing: 2px;
    text-transform: uppercase;
}
.current-player {
    font-family: 'Playfair Display', serif;
    font-size: 1.1rem;
    color: #f0e6c8;
    background: #1a1628;
    border: 1px solid #3a3050;
    border-radius: 10px;
    padding: 0.7rem 1rem;
    margin-bottom: 1rem;
    display: inline-block;
}

/* ── Briefcases ── */
.briefcase-grid {
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
    margin: 1rem 0;
}
.briefcase {
    width: 90px;
    height: 100px;
    background: linear-gradient(145deg, #1e1830, #150f28);
    border: 2px solid #3a3050;
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    color: #d4af37;
    transition: all 0.18s;
    position: relative;
    box-shadow: 0 4px 20px rgba(0,0,0,0.4);
}
.briefcase:hover { border-color: #d4af37; transform: scale(1.07); box-shadow: 0 6px 30px rgba(212,175,55,0.25); }
.briefcase-num {
    font-size: 0.65rem;
    color: #5a5070;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-top: 4px;
}
.briefcase.opened {
    background: #0d0b15;
    border-color: #2a2030;
    opacity: 0.4;
    cursor: not-allowed;
    transform: none !important;
}
.briefcase.opened:hover { border-color: #2a2030; box-shadow: none; }

/* ── Player holdings ── */
.player-card {
    background: #13131f;
    border: 1px solid #2a2540;
    border-radius: 12px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.8rem;
}
.player-card-name {
    font-family: 'Playfair Display', serif;
    font-size: 1rem;
    color: #f0e6c8;
    margin-bottom: 0.5rem;
}
.player-holding {
    display: inline-block;
    background: #1e1830;
    border: 1px solid #3a3050;
    border-radius: 6px;
    padding: 3px 10px;
    font-size: 0.78rem;
    color: #c8b870;
    margin: 2px 4px 2px 0;
}
.player-holding.current-pick {
    border-color: #d4af37;
    background: #2a2030;
    color: #f0e6c8;
}

/* ── Reveal ── */
.reveal-card {
    background: linear-gradient(135deg, #13131f, #0e0e18);
    border: 1px solid #d4af37;
    border-radius: 16px;
    padding: 1.5rem 2rem;
    margin-bottom: 1rem;
}
.reveal-player {
    font-family: 'Playfair Display', serif;
    font-size: 1.6rem;
    color: #f0e6c8;
    margin-bottom: 0.8rem;
}
.reveal-item {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 6px 0;
    font-size: 0.88rem;
    color: #b0a880;
}
.reveal-cat {
    color: #d4af37;
    font-size: 0.7rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    width: 100px;
    flex-shrink: 0;
}
.reveal-value { color: #f0e6c8; font-size: 0.95rem; }

/* ── Swap panel ── */
.swap-box {
    background: #0e0e18;
    border: 1px solid #2a2540;
    border-radius: 10px;
    padding: 1rem 1.2rem;
    margin-top: 0.8rem;
    font-size: 0.85rem;
    color: #9080b0;
}
.swap-option {
    display: inline-block;
    background: #1a1628;
    border: 1px solid #3a3050;
    border-radius: 6px;
    padding: 3px 10px;
    font-size: 0.78rem;
    color: #a090c0;
    margin: 3px;
}

/* ── Dividers ── */
.gold-divider {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, #d4af37, transparent);
    margin: 1.5rem 0;
}

/* ── Buttons override ── */
.stButton > button {
    background: linear-gradient(135deg, #2a2040, #1a1628) !important;
    color: #d4af37 !important;
    border: 1px solid #3a3050 !important;
    border-radius: 8px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.85rem !important;
    letter-spacing: 1px !important;
    padding: 0.4rem 1.2rem !important;
    transition: all 0.15s !important;
}
.stButton > button:hover {
    border-color: #d4af37 !important;
    background: linear-gradient(135deg, #3a2f58, #2a2040) !important;
    color: #f0e6c8 !important;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# GAME DATA
# ─────────────────────────────────────────────────────────────────────────────
GAMES = {
    "🍕 Ultimate Party Night": {
        "emoji": "🎉",
        "description": "Plan the perfect party — pick your food, drinks, music, and more!",
        "categories": {
            "Food": ["Pizza", "Tacos", "Burgers", "Sushi", "BBQ", "Pasta", "Wings", "Ramen", "Nachos", "Charcuterie"],
            "Drink": ["Craft Beer", "Cocktails", "Wine", "Seltzers", "Mocktails", "Margaritas", "Mimosas", "Punch Bowl", "Whiskey Sour", "Espresso Martini"],
            "Music": ["Hip-Hop", "80s Pop", "Country", "EDM", "R&B", "Latin", "Rock", "Jazz", "Indie", "Top 40"],
            "Activity": ["Karaoke", "Board Games", "Dance Off", "Trivia", "Cornhole", "Movie Marathon", "Poker", "Escape Room Kit", "Paint Night", "Jackbox Games"],
            "Venue": ["Backyard", "Rooftop", "Beach", "Living Room", "Rented Hall", "Park", "Lake House", "Bowling Alley", "Restaurant Buyout", "Boat"],
            "Theme": ["Tropical", "Decades Party", "Black & White", "Costume", "Casino Night", "Sports Theme", "Glow Party", "Masquerade", "Luau", "Ugly Sweater"],
        }
    },
    "🌍 Dream Vacation": {
        "emoji": "✈️",
        "description": "Build your ultimate travel itinerary — destination, stay, food, and thrills!",
        "categories": {
            "Destination": ["Paris", "Tokyo", "Bali", "New York", "Rome", "Santorini", "Machu Picchu", "Safari Kenya", "Iceland", "Maldives"],
            "Accommodation": ["5-Star Hotel", "Airbnb Villa", "Overwater Bungalow", "Boutique Inn", "Hostel", "Glamping", "Castle Stay", "Treehouse", "Yacht", "Mountain Cabin"],
            "Transport": ["First Class Flight", "Road Trip", "Train Journey", "Private Jet", "Cruise Ship", "Motorcycle Tour", "Campervan", "Bicycle Tour", "Helicopter", "Sailboat"],
            "Activity": ["Skydiving", "Cooking Class", "Museum Hopping", "Hiking", "Scuba Diving", "Wine Tasting", "City Walking Tour", "Surfing", "Zip Lining", "Hot Air Balloon"],
            "Cuisine": ["Street Food", "Fine Dining", "Seafood", "Local Markets", "Rooftop Restaurant", "Farm-to-Table", "Night Market", "Food Tour", "Michelin Star", "Beach Shack"],
            "Companion": ["Solo Trip", "Partner", "Best Friend", "Family", "Group of Friends", "Colleague", "Parent", "Pet-Friendly", "Honeymoon", "Anniversary Trip"],
        }
    },
    "🏆 Fantasy Sports Draft": {
        "emoji": "🏈",
        "description": "Draft your fantasy squad — pick positions, players, and your game plan!",
        "categories": {
            "QB": ["Patrick Mahomes", "Josh Allen", "Lamar Jackson", "Joe Burrow", "Jalen Hurts", "Dak Prescott", "Justin Herbert", "Tua Tagovailoa", "Jordan Love", "Brock Purdy"],
            "RB": ["Christian McCaffrey", "Derrick Henry", "Saquon Barkley", "Josh Jacobs", "Bijan Robinson", "Jonathan Taylor", "De'Von Achane", "Breece Hall", "Jahmyr Gibbs", "Tony Pollard"],
            "WR": ["Ja'Marr Chase", "Justin Jefferson", "CeeDee Lamb", "Tyreek Hill", "Davante Adams", "Stefon Diggs", "Amon-Ra St. Brown", "Puka Nacua", "Garrett Wilson", "DK Metcalf"],
            "TE": ["Travis Kelce", "Sam LaPorta", "Mark Andrews", "TJ Hockenson", "Dallas Goedert", "George Kittle", "Trey McBride", "Cole Kmet", "Jake Ferguson", "Evan Engram"],
            "Defense": ["San Francisco 49ers", "Baltimore Ravens", "Dallas Cowboys", "Pittsburgh Steelers", "New England Patriots", "Denver Broncos", "Buffalo Bills", "Cleveland Browns", "Kansas City Chiefs", "Philadelphia Eagles"],
            "Kicker": ["Justin Tucker", "Evan McPherson", "Tyler Bass", "Jake Elliott", "Harrison Butker", "Brandon Aubrey", "Jason Myers", "Matt Gay", "Cairo Santos", "Greg Zuerlein"],
        }
    },
    "🎬 Movie Marathon": {
        "emoji": "🍿",
        "description": "Curate the perfect movie night — genre, snacks, setting, and more!",
        "categories": {
            "Genre": ["Action Thriller", "Romantic Comedy", "Horror", "Sci-Fi", "Animation", "Documentary", "Crime Drama", "Fantasy", "Comedy", "Superhero"],
            "Era": ["Classic 50s-60s", "New Hollywood 70s", "Blockbuster 80s", "Indie 90s", "Early 2000s", "2010s Golden Age", "Modern 2020s", "Silent Film", "Foreign Film", "Made-for-TV"],
            "Snack": ["Popcorn", "Pizza Rolls", "Candy Mix", "Nachos", "Charcuterie Board", "Ice Cream", "Pretzels & Dip", "Sliders", "Chips & Guac", "Brownie Sundae"],
            "Setting": ["Home Theater", "Drive-In", "Rooftop Cinema", "Blanket Fort", "Cinema Paradiso", "Outdoor Projection", "Cinema Pub", "IMAX", "Dorm Room", "Beach Bonfire"],
            "Mood": ["Cry Your Eyes Out", "Edge of Your Seat", "Laugh Till it Hurts", "Mind Blown", "Feel Good", "Total Fear", "Inspired", "Nostalgic", "Date Night Vibes", "Chaotic Fun"],
            "Company": ["Solo Night In", "Date Night", "Family Night", "Squad Goals", "Stranger Becomes Friend", "Book Club", "First Date", "Old Friends Reunion", "Rainy Day Buddy", "Roommates"],
        }
    },
    "🍽️ Dream Dinner Party": {
        "emoji": "🥂",
        "description": "Host the most memorable dinner — menu, guests, ambiance, and surprises!",
        "categories": {
            "Starter": ["Burrata & Tomato", "French Onion Soup", "Shrimp Cocktail", "Bruschetta", "Oysters", "Caprese Salad", "Lobster Bisque", "Charcuterie Board", "Stuffed Mushrooms", "Caesar Salad"],
            "Main Course": ["Wagyu Filet", "Lobster Thermidor", "Lamb Rack", "Truffle Pasta", "Sea Bass", "Duck Confit", "Beef Wellington", "Paella", "Stuffed Chicken", "Osso Buco"],
            "Dessert": ["Crème Brûlée", "Chocolate Lava Cake", "Tiramisu", "Cheesecake", "Pavlova", "Macarons", "Banana Foster", "Tarte Tatin", "Panna Cotta", "Ice Cream Bar"],
            "Wine": ["Bordeaux Red", "Champagne", "Burgundy White", "Rosé", "Barolo", "Pinot Noir", "Sauvignon Blanc", "Prosecco", "Chianti", "Riesling"],
            "Ambiance": ["Candlelit", "Garden Terrace", "Modern Loft", "Rustic Farmhouse", "Rooftop at Sunset", "Beach Bonfire", "Private Club", "Art Gallery", "Wine Cellar", "Penthouse"],
            "Guest": ["Celebrity Chef", "Childhood Best Friend", "Famous Author", "Travel Buddy", "Your Hero", "Mystery Guest", "Long Lost Friend", "Mentor", "Soulmate", "Comedian"],
        }
    },
}

PLAYER_COLORS = ["#d4af37", "#c084fc", "#34d399", "#f87171", "#60a5fa"]
PLAYER_BG = ["#2a2010", "#2a1040", "#0a2a20", "#2a1010", "#0a1a2a"]

# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE INIT
# ─────────────────────────────────────────────────────────────────────────────
def init_state():
    defaults = {
        "screen": "setup",          # setup | game | results
        "selected_game": None,
        "num_players": 2,
        "player_names": [],
        "categories": [],           # ordered list of category names
        "category_pools": {},       # category -> remaining options
        "round_idx": 0,             # 0–5 (which category)
        "turn_idx": 0,              # which player's turn within a round
        "phase": "pick",            # pick | swap
        "player_picks": {},         # {player_idx: {category: value}}
        "briefcase_contents": {},   # {1-6: value} for current round
        "opened_cases": [],         # which cases opened this round
        "swap_done": [],            # players who acted this swap phase
        "message": "",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def reset_game():
    keys = ["screen","selected_game","num_players","player_names","categories",
            "category_pools","round_idx","turn_idx","phase","player_picks",
            "briefcase_contents","opened_cases","swap_done","message"]
    for k in keys:
        if k in st.session_state:
            del st.session_state[k]
    init_state()

def start_game(game_key, num_players, player_names):
    game = GAMES[game_key]
    cats = list(game["categories"].keys())
    random.shuffle(cats)
    pools = {cat: game["categories"][cat].copy() for cat in cats}

    st.session_state.selected_game = game_key
    st.session_state.num_players = num_players
    st.session_state.player_names = player_names
    st.session_state.categories = cats
    st.session_state.category_pools = pools
    st.session_state.player_picks = {i: {} for i in range(num_players)}
    st.session_state.round_idx = 0
    st.session_state.turn_idx = 0
    st.session_state.phase = "pick"
    st.session_state.opened_cases = []
    st.session_state.swap_done = []
    st.session_state.message = ""
    st.session_state.screen = "game"
    deal_briefcases()

def deal_briefcases():
    cat = st.session_state.categories[st.session_state.round_idx]
    pool = st.session_state.category_pools[cat].copy()
    random.shuffle(pool)
    contents = {}
    for i in range(1, 7):
        contents[i] = pool[i - 1]
    st.session_state.briefcase_contents = contents
    st.session_state.opened_cases = []
    st.session_state.swap_done = []
    st.session_state.turn_idx = 0
    st.session_state.phase = "pick"

def current_category():
    return st.session_state.categories[st.session_state.round_idx]

def current_player_name():
    idx = st.session_state.turn_idx
    return st.session_state.player_names[idx]

def pick_case(case_num):
    idx = st.session_state.turn_idx
    cat = current_category()
    value = st.session_state.briefcase_contents[case_num]
    st.session_state.player_picks[idx][cat] = value
    st.session_state.opened_cases.append(case_num)
    st.session_state.message = f"✨ {st.session_state.player_names[idx]} picked **{value}**!"

    # advance to next player or transition to swap phase
    n = st.session_state.num_players
    if st.session_state.turn_idx + 1 < n:
        st.session_state.turn_idx += 1
    else:
        # all players picked → move to swap phase if unopened cases remain
        remaining = [c for c in range(1, 7) if c not in st.session_state.opened_cases]
        if remaining:
            st.session_state.phase = "swap"
            st.session_state.turn_idx = 0
            st.session_state.swap_done = []
        else:
            advance_round()

def swap_case(case_num):
    idx = st.session_state.turn_idx
    cat = current_category()
    new_value = st.session_state.briefcase_contents[case_num]
    old_value = st.session_state.player_picks[idx].get(cat, "")
    st.session_state.player_picks[idx][cat] = new_value
    st.session_state.opened_cases.append(case_num)
    st.session_state.message = f"🔄 {st.session_state.player_names[idx]} swapped **{old_value}** → **{new_value}**!"
    advance_swap_turn()

def stay():
    idx = st.session_state.turn_idx
    st.session_state.message = f"✅ {st.session_state.player_names[idx]} chose to **stay**!"
    advance_swap_turn()

def advance_swap_turn():
    idx = st.session_state.turn_idx
    st.session_state.swap_done.append(idx)
    n = st.session_state.num_players
    remaining_cases = [c for c in range(1, 7) if c not in st.session_state.opened_cases]

    # find next player who hasn't acted yet
    next_idx = None
    for i in range(1, n + 1):
        candidate = (idx + i) % n
        if candidate not in st.session_state.swap_done:
            next_idx = candidate
            break

    # end swap phase if: no more cases, or everyone has acted
    if not remaining_cases or next_idx is None:
        advance_round()
    else:
        st.session_state.turn_idx = next_idx

def advance_round():
    st.session_state.round_idx += 1
    if st.session_state.round_idx >= 6:
        st.session_state.screen = "results"
    else:
        deal_briefcases()

# ─────────────────────────────────────────────────────────────────────────────
# SCREEN: SETUP
# ─────────────────────────────────────────────────────────────────────────────
if st.session_state.screen == "setup":
    st.markdown('<div class="game-title">💼 The Briefcase</div>', unsafe_allow_html=True)
    st.markdown('<div class="game-subtitle">A group selection experience</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-label">Choose Your Game</div>', unsafe_allow_html=True)

    # Game selection
    game_cols = st.columns(5)
    selected_game_key = st.session_state.get("_pending_game", None)

    for i, (gk, gv) in enumerate(GAMES.items()):
        with game_cols[i]:
            cats_preview = " · ".join(list(gv["categories"].keys())[:3]) + "..."
            border = "#d4af37" if selected_game_key == gk else "#2a2540"
            st.markdown(f"""
            <div class="game-card" style="border-color:{border}">
                <div class="game-card-emoji">{gv['emoji']}</div>
                <div class="game-card-title">{gk}</div>
                <div class="game-card-cats">{cats_preview}</div>
            </div>""", unsafe_allow_html=True)
            if st.button("Select", key=f"sel_{i}"):
                st.session_state["_pending_game"] = gk
                st.rerun()

    st.markdown('<hr class="gold-divider">', unsafe_allow_html=True)

    if selected_game_key:
        gv = GAMES[selected_game_key]
        st.markdown(f'<div class="section-label">Selected: {selected_game_key}</div>', unsafe_allow_html=True)
        cats = list(gv["categories"].keys())
        cat_str = " &nbsp;·&nbsp; ".join([f"<span style='color:#f0e6c8'>{c}</span>" for c in cats])
        st.markdown(f'<div style="color:#7a6e58; font-size:0.85rem; margin-bottom:1rem;">Categories: {cat_str}</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-label">Players</div>', unsafe_allow_html=True)
    num_players = st.slider("Number of Players", 2, 4, 2, label_visibility="collapsed")

    name_cols = st.columns(num_players)
    player_names = []
    for i in range(num_players):
        with name_cols[i]:
            default = f"Player {i+1}"
            name = st.text_input(f"Player {i+1} Name", value=default, key=f"name_{i}", label_visibility="collapsed",
                                  placeholder=f"Player {i+1}")
            player_names.append(name if name.strip() else default)

    st.markdown("<br>", unsafe_allow_html=True)
    if selected_game_key:
        if st.button("🎲  Start Game", use_container_width=False):
            start_game(selected_game_key, num_players, player_names)
            st.rerun()
    else:
        st.markdown('<div style="color:#5a5468; font-size:0.85rem;">← Select a game above to begin</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# SCREEN: GAME
# ─────────────────────────────────────────────────────────────────────────────
elif st.session_state.screen == "game":
    n = st.session_state.num_players
    names = st.session_state.player_names
    cat = current_category()
    round_num = st.session_state.round_idx + 1
    phase = st.session_state.phase
    turn_idx = st.session_state.turn_idx

    # Header
    col_h1, col_h2 = st.columns([5, 1])
    with col_h1:
        st.markdown(f'<div class="game-title" style="font-size:2.4rem;">{st.session_state.selected_game}</div>', unsafe_allow_html=True)
    with col_h2:
        if st.button("↩ Restart"):
            reset_game()
            st.rerun()

    # Round banner
    st.markdown(f"""
    <div class="round-banner">
        <div class="round-category">Round {round_num} of 6</div>
        <div class="round-title">📂 Category: {cat}</div>
        <div style="color:#5a5468; font-size:0.8rem; margin-top:4px;">
            {'🎴 Pick Phase — Each player selects a briefcase' if phase == 'pick' else '🔄 Swap Phase — Each player may swap or stay'}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Message
    if st.session_state.message:
        st.markdown(f'<div style="background:#1a2a1a;border:1px solid #2a5a2a;border-radius:8px;padding:0.7rem 1rem;color:#80d080;font-size:0.88rem;margin-bottom:1rem;">{st.session_state.message}</div>', unsafe_allow_html=True)

    main_col, side_col = st.columns([3, 2])

    with main_col:
        # Current player indicator
        color = PLAYER_COLORS[turn_idx % len(PLAYER_COLORS)]
        st.markdown(f"""
        <div style="margin-bottom:1rem;">
            <div class="section-label">Current Turn</div>
            <div class="current-player">
                <span style="color:{color}; margin-right:8px;">●</span>{names[turn_idx]}'s turn
                {'— pick a briefcase' if phase == 'pick' else '— swap or stay?'}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Briefcases
        st.markdown('<div class="section-label">Briefcases</div>', unsafe_allow_html=True)
        case_cols = st.columns(6)
        for case_num in range(1, 7):
            with case_cols[case_num - 1]:
                opened = case_num in st.session_state.opened_cases
                if opened:
                    st.markdown(f"""
                    <div class="briefcase opened">
                        💼
                        <div class="briefcase-num">#{case_num}</div>
                    </div>""", unsafe_allow_html=True)
                else:
                    if st.button(f"💼\n#{case_num}", key=f"case_{case_num}_{round_num}_{phase}"):
                        if phase == "pick":
                            pick_case(case_num)
                        else:
                            swap_case(case_num)
                        st.rerun()

        # Stay button (swap phase only)
        if phase == "swap":
            st.markdown("<br>", unsafe_allow_html=True)
            remaining = [c for c in range(1, 7) if c not in st.session_state.opened_cases]
            st.markdown(f'<div class="swap-box">Remaining unopened cases: {" ".join([f"#{c}" for c in remaining])}<br>Pick one to swap your current pick, or stay with what you have.</div>', unsafe_allow_html=True)
            if st.button("✅  Stay with my pick"):
                stay()
                st.rerun()

    with side_col:
        st.markdown('<div class="section-label">Player Holdings</div>', unsafe_allow_html=True)
        for i in range(n):
            picks = st.session_state.player_picks[i]
            color = PLAYER_COLORS[i % len(PLAYER_COLORS)]
            bg = PLAYER_BG[i % len(PLAYER_BG)]
            is_current = (i == turn_idx)
            border = color if is_current else "#2a2540"

            holdings_html = ""
            for c in st.session_state.categories[:round_num]:
                val = picks.get(c, "—")
                cls = "current-pick" if c == cat and val != "—" else ""
                holdings_html += f'<span class="player-holding {cls}"><em style="color:#5a5468;font-style:normal;font-size:0.68rem;">{c}:</em> {val}</span>'

            st.markdown(f"""
            <div class="player-card" style="border-color:{border};">
                <div class="player-card-name">
                    <span style="color:{color};">●</span> {names[i]}
                    {'<span style="color:#d4af37;font-size:0.7rem;margin-left:6px;">← CURRENT</span>' if is_current else ''}
                </div>
                <div>{holdings_html if holdings_html else '<span style="color:#3a3050;font-size:0.8rem;">Nothing yet</span>'}</div>
            </div>
            """, unsafe_allow_html=True)

        # Round progress
        st.markdown('<div class="section-label" style="margin-top:1rem;">Round Progress</div>', unsafe_allow_html=True)
        for i, c in enumerate(st.session_state.categories):
            done = i < st.session_state.round_idx
            active = i == st.session_state.round_idx
            color_dot = "#d4af37" if active else ("#34d399" if done else "#2a2540")
            label_color = "#f0e6c8" if active else ("#80c890" if done else "#3a3050")
            st.markdown(f'<div style="font-size:0.8rem;color:{label_color};margin:3px 0;"><span style="color:{color_dot};">{"▶" if active else ("✓" if done else "○")}</span> {c}</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# SCREEN: RESULTS
# ─────────────────────────────────────────────────────────────────────────────
elif st.session_state.screen == "results":
    st.markdown('<div class="game-title">🏆 Final Results</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="game-subtitle">{st.session_state.selected_game}</div>', unsafe_allow_html=True)
    st.markdown('<hr class="gold-divider">', unsafe_allow_html=True)

    names = st.session_state.player_names
    cats = st.session_state.categories
    n = st.session_state.num_players

    res_cols = st.columns(min(n, 2))
    for i in range(n):
        with res_cols[i % 2]:
            st.write(st.session_state.player_picks)
            color = PLAYER_COLORS[i % len(PLAYER_COLORS)]
            picks = st.session_state.player_picks[i]
            items_html = ""
            for cat in cats:
                val = picks.get(cat, "—")
                items_html += f"""
                <div class="reveal-item">
                    <span class="reveal-cat">{cat}</span>
                    <span style="color:#3a3050;">│</span>
                    <span class="reveal-value">{val}</span>
                </div>"""
            st.markdown(f"""
            <div class="reveal-card" style="border-color:{color}40;">
                <div class="reveal-player"><span style="color:{color};">●</span> {names[i]}</div>
                {items_html}
            </div>""", unsafe_allow_html=True)

    st.markdown('<hr class="gold-divider">', unsafe_allow_html=True)
    col_a, col_b = st.columns([1, 5])
    with col_a:
        if st.button("🎲 Play Again"):
            reset_game()
            st.rerun()

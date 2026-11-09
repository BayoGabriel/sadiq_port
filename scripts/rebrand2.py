"""Second pass: finish rebranding — remaining index.js strings, the two hero
chunks (CurtainHero/TunnelHero hold the hero copy), and the work arrays."""
import re, sys

fails = []

def patch(path, pairs):
    src = open(path, encoding="utf-8").read()
    for old, new, count in pairs:
        n = src.count(old)
        if n == 0 or (count is not None and n != count):
            fails.append(f"[{path}] {'exp '+str(count) if count else 'miss'} got {n}x: {old[:70]!r}")
            continue
        src = src.replace(old, new)
    open(path, "w", encoding="utf-8").write(src)

# ---------------- index bundle: leftovers ----------------
JS = "js/index-CjxIzqK1.js"
src = open(JS, encoding="utf-8").read()

for old, new in [
    ("/logo-oyin-real.png", "/logo-sadiq.svg"),
    ("Oyin logo", "Sadiq logo"),
    ("a product design by Sadiq Abdulazeez, product designer in Lagos.",
     "a product design project by Sadiq Abdulazeez, product designer in Abuja."),
    ("`${e.name} brand identity`", "`${e.name} product design`"),
]:
    n = src.count(old)
    if n == 0:
        fails.append(f"[{JS}] miss: {old[:70]!r}")
    else:
        src = src.replace(old, new)

def esc(s):
    return s.replace("\\", "\\\\").replace("`", "\\`")

def build_project(p):
    h = p["helper"]
    meta = ",".join(f"{{label:`{l}`,value:`{v}`}}" for l, v in p["meta"])
    secs = []
    for sid, label, title, body, rows in p["sections"]:
        b = ",".join(f"`{esc(t)}`" for t in body)
        r = ",".join("[" + ",".join(f"{h}(`{k}`)" for k in row) + "]" for row in rows)
        secs.append(f"{{id:`{sid}`,label:`{label}`,title:`{esc(title)}`,body:[{b}],rows:[{r}]}}")
    return (f"{{slug:`{p['slug']}`,name:`{p['name']}`,intro:`{esc(p['intro'])}`,meta:[{meta}],"
            f"hero:{h}(`{p['hero']}`),teaser:{h}(`{p['teaser']}`),sections:[{','.join(secs)}]}}")

projects = [
 dict(slug="boldswitch", helper="x", name="Boldswitch",
  intro="A borderless banking app that gives Nigerians virtual USD cards, US bank accounts and faster cross-border payments, in one place.",
  meta=[("Industry","Fintech / Consumer payments"),("Scope","Product Design"),("Year","2024"),("Services","UX Flows · UI Design · Design System · Developer Handoff")],
  hero="hero", teaser="card",
  sections=[
   ("overview","Overview","Banking without borders.",
    ["Millions of Nigerians need access to dollars for everyday reasons: paying for subscriptions, receiving pay from US clients, or supporting family abroad. Traditional routes are slow, expensive or unpredictable.",
     "Boldswitch combines virtual USD cards, a personal US bank account, AI-assisted account entry, face-based payments and cross-border transfers in one app.",
     "The goal was to make a complex, regulated, multi-currency product feel simple enough for first-time users and trustworthy enough to hold their money."],
    [["dashboard"],["send","success"]]),
   ("challenge","The Challenge","Trust at every step.",
    ["People hesitate to put money into a new app, so every screen had to reduce anxiety rather than add to it.",
     "Multiple currencies, card types, account tiers and compliance steps had to feel like one coherent product.",
     "Long account numbers are easy to mistype, and a mistake with money is costly — all inside a 24-week window that demanded a tight MVP."],
    [["onboarding","tiers"]]),
   ("solution","The Solution","Designed around certainty.",
    ["The dashboard leads with the user's balance, followed by quick actions and recent activity — answering “how much do I have?” first, and confirming that transactions went through.",
     "After every payment, a clear success state shows the amount, recipient and details, so the moment of doubt never lasts.",
     "Snap & Pay lets users photograph an account number to auto-fill it, and FacePay enables quick payments with visible consent and security cues.",
     "Progressive, tiered onboarding gets new users started quickly, while a modular design system keeps the product consistent and ready to scale."],
    [["card"],["facepay","snap"],["system"]]),
   ("conclusion","Conclusion","Calm, even when money moves.",
    ["The MVP was designed, built and launched within 24 weeks.",
     "Since launch, Boldswitch has passed 50K+ downloads on Google Play, with a 4.1-star rating across 450+ verified reviews.",
     "The clearest lesson from reviews: in fintech, clarity at the moment of anxiety matters more than visual flair — verification, tiers and support are next in line for refinement."],
    [["screens","receipt"]]),
  ]),
 dict(slug="boldswitch-business", helper="S", name="Boldswitch Business",
  intro="A payments and money-management app that lets Nigerian merchants collect payments, track every naira in real time and run their business — no technical setup required.",
  meta=[("Industry","Fintech / Merchant payments"),("Scope","Product Design + Website"),("Year","2025"),("Services","UX Flows · UI Design · Design System · Marketing Website")],
  hero="hero", teaser="dashboard",
  sections=[
   ("overview","Overview","Getting paid, without doubt.",
    ["Most small and mid-sized businesses in Nigeria accept payment by bank transfer. The weak point is verification: customers say they have paid, merchants check alerts manually, and reconciliation happens later by hand.",
     "Boldswitch Business lets merchants accept transfers from any Nigerian bank, generate payment links and QR codes, and see confirmation in real time — with no monthly fees to get started.",
     "I designed both the merchant mobile app and the marketing website, so the product experience and its first impression feel like one brand."],
    [["dashboard"],["link","qr"]]),
   ("challenge","The Challenge","Certainty at the moment of sale.",
    ["A merchant handing over goods needs a confident, unambiguous “paid” signal — the interface must never leave doubt.",
     "Transfers, payment links, QR codes, embedded checkout and in-person options all had to feel like one coherent system.",
     "Verification had to be as light as compliance allows, and settlement status readable by people who do not think in accounting terms."],
    [["onboarding","status"]]),
   ("solution","The Solution","One “get paid” action, many channels.",
    ["Payment links, QR codes, checkout widgets and in-person options are presented as variations of a single action — because merchants think “I need to get paid”, not “I need a payment technology”.",
     "Each sale can generate its own payment account, so matching a payment to a sale is automatic and per-transaction status stays clear: awaiting payment, paid, settled.",
     "The dashboard is built around money in motion — incoming first, settlement status visible, and exports built in for bookkeeping.",
     "Role-based access and multi-business support keep owners, cashiers and accountants in the right view."],
    [["collect"],["team","web"],["history"]]),
   ("conclusion","Conclusion","Built around the merchant's first question.",
    ["Boldswitch Business shipped on Android and iOS with a coherent merchant experience and a supporting website — an early-stage launch with encouraging first signals.",
     "Starting from the merchant's most urgent question — “has the customer paid?” — gave the product a clear design centre."],
    [["screens","store"]]),
  ]),
 dict(slug="lodapoint", helper="C", name="Lodapoint",
  intro="A three-sided mobility and logistics platform connecting people who need rides, businesses that need goods moved, and the drivers and transporters who do the moving.",
  meta=[("Industry","Mobility / Logistics"),("Scope","Product Design × 4 apps"),("Year","2023 — Present"),("Services","UX Flows · UI Design · Design System · Web Apps")],
  hero="hero", teaser="rider",
  sections=[
   ("overview","Overview","One platform, three audiences.",
    ["In many Nigerian cities, booking a ride or finding a reliable truck still depends on word of mouth, phone calls and uncertainty about price, availability and trust.",
     "Lodapoint is a single ecosystem: customers request a ride or ship goods, drivers find and accept trips, and transporters manage cargo jobs and fleets — with live tracking connecting all three.",
     "The platform ships as three role-specific mobile apps plus companion web apps, all sharing one design language."],
    [["rider"],["driver","transporter"]]),
   ("challenge","The Challenge","Three experiences, one brand.",
    ["Each audience has a distinct mental model and daily routine — riders want speed, drivers want steady work, and transporters need business-grade control.",
     "Moving a person and moving cargo carry different information needs, from passenger count to load type and vehicle size.",
     "Field users work in motion on varied networks and devices, so every screen had to be glanceable and quick to act on."],
    [["request","vehicle"]]),
   ("solution","The Solution","Request, accept, track — one lifecycle.",
    ["Separate apps for separate roles keep navigation short and let each interface be tuned to its job, while a shared design system keeps the platform coherent.",
     "Across all three apps the core flow follows the same arc: a request is created, a driver or transporter accepts it, and the journey is tracked to completion.",
     "Vehicle choice is a guided step — tricycles, cars, trucks — with capacity cues that prevent mismatched bookings and set accurate expectations.",
     "The driver app centres on opportunity and schedule, the transporter app on booking, tracking and fleet control — and the web apps bring the same patterns to a desk."],
    [["track"],["schedule","fleet"],["web"]]),
   ("conclusion","Conclusion","Live and moving.",
    ["All three mobile apps are live on Google Play and actively maintained, with early-stage downloads across rider, driver and transporter audiences.",
     "The clearest lesson: a marketplace is really several products stitched together — the craft is making them feel like one system."],
    [["screens","store"]]),
  ]),
 dict(slug="bravoo", helper="D", name="Bravoo",
  intro="Banking designed for migrants and global citizens in the UK — a live marketing website and a mobile app MVP in pre-launch.",
  meta=[("Industry","Fintech / UK banking"),("Scope","Website + Mobile App"),("Year","2025"),("Services","UX Design · UI Design · MVP Scoping")],
  hero="hero", teaser="web",
  sections=[
   ("overview","Overview","The bank for Global Citizens.",
    ["People who move to the UK often struggle to access everyday banking — they may lack local credit history, familiar documents or a UK address, while still needing to support family abroad.",
     "Bravoo positions itself around one clear promise: banking designed for global citizens, not retrofitted for them.",
     "I designed both the live marketing website and the mobile app MVP, which is currently unreleased."],
    [["web"],["home","send"]]),
   ("challenge","The Challenge","Trust from zero.",
    ["A new brand asking newcomers to hold their money has to earn confidence fast.",
     "Verification must be thorough without feeling like another locked door, and wording must stay plain across languages and cultures.",
     "Currencies, fees and timing must be unmistakable at every step — within a disciplined MVP scope."],
    [["onboarding","verify"]]),
   ("solution","The Solution","Calm, clear, borderless.",
    ["The website leads with a single inclusive message — for an audience that feels overlooked by banks, the first screen has to say “this is for you” before it explains anything else.",
     "The app was scoped tightly around the few flows that matter most: getting in, seeing money, moving money.",
     "Calm visual language, generous spacing and clear status messages keep sensitive moments — verification, transfers — from feeling stressful.",
     "Web and app share one visual language, so moving from the site to the app feels like the same brand."],
    [["transfer"],["card","support"],["system"]]),
   ("conclusion","Conclusion","Ready for launch.",
    ["The marketing website is live and communicates a clear positioning; the mobile app MVP is designed and ready for the next stage of the product's journey.",
     "What I would measure after launch: onboarding completion, time to first transaction, verification drop-off and transfer success rate."],
    [["screens","site"]]),
  ]),
]

w_new = ("x=b(`boldswitch`),S=b(`boldswitch-business`),C=b(`lodapoint`),D=b(`bravoo`),w=["
         + ",".join(build_project(p) for p in projects)
         + "],T=e=>w.find(t=>t.slug===e),E=e=>w[(w.findIndex(t=>t.slug===e)+1)%w.length],j=[],M=e=>j.find(t=>t.slug===e)")
src2 = re.sub(r"x=b\(`vitalcare-plus`\).*?M=e=>j\.find\(t=>t\.slug===e\)",
              lambda m: w_new, src, count=1, flags=re.S)
if src2 == src:
    fails.append(f"[{JS}] miss: w/j array block")
src = src2
open(JS, "w", encoding="utf-8").write(src)

# ---------------- hero chunks ----------------
curtain_pairs = [
    ("Z=`Rufai Oyinkansola`", "Z=`Sadiq Abdulazeez`", 1),
    ("children:`Lagos`", "children:`Abuja`", 1),
    ("children:`A brand designer crafting`", "children:`A lead product designer crafting`", 1),
    ("children:`intentional brand experiences.`", "children:`intentional digital experiences.`", 1),
]
tunnel_pairs = [
    ("children:`Rufai Oyinkansola`", "children:`Sadiq Abdulazeez`", 2),
    ("lang:`yo`", "lang:`en`", 2),
    (", brand designer in Lagos`", ", product designer in Abuja`", 1),
    ("children:`brand designer, Lagos`", "children:`product designer, Abuja`", 1),
    ("{text:`Oyin`,weight:600}", "{text:`Sadiq`,weight:600}", 1),
    ("mailto:hello@oyin.design", "mailto:abubakarsadiqabdulazeez388@gmail.com", 1),
]
for base in ("js", "assets"):
    patch(f"{base}/CurtainHero-ChtinHHQ.js", curtain_pairs)
    patch(f"{base}/TunnelHero-C941nQWH.js", tunnel_pairs)

# ---------------- leftover scan ----------------
bad = ["Oyin", "oyin", "Rufai", "Oyinkansola", "behance.net/oyinkanrufai", "designbyoyin",
       "oyinkansolarufai", "ifeoluwase", "vitalcare", "itours", "Vibe Oasis", "vibe-oasis",
       "Asyn", "asyn", "ayanae", "Ayana", "bebedi", "Bebedi", "quaesana", "Quaesana",
       "hello@oyin", "oyin.design", "Lagos"]
import glob
for f in ["js/index-CjxIzqK1.js", "js/CurtainHero-ChtinHHQ.js", "js/TunnelHero-C941nQWH.js",
          "assets/CurtainHero-ChtinHHQ.js", "assets/TunnelHero-C941nQWH.js", "index.html"]:
    src = open(f, encoding="utf-8").read()
    for w in bad:
        if w == "Lagos":
            src = src.replace("Africa/Lagos", "")  # timezone stays
        if w in src:
            fails.append(f"[leftover {f}] {w}")

print("\n".join(fails) if fails else "ALL OK — fully rebranded")
sys.exit(1 if fails else 0)

"""
Rebrands the bundled site from Rufai Oyinkansola (Oyin) to Sadiq Abdulazeez.
Edits js/index-CjxIzqK1.js (content strings only — no logic) and index.html.
Every replacement asserts an expected occurrence count so a silent miss fails loudly.
"""
import re, sys

JS = "js/index-CjxIzqK1.js"
src = open(JS, encoding="utf-8").read()

fails = []

def rep(old, new, count=None):
    """Replace `old` with `new`; if count given, require exactly that many occurrences."""
    global src
    n = src.count(old)
    if n == 0 or (count is not None and n != count):
        fails.append(f"[{'exp '+str(count) if count else 'miss'}] got {n}x: {old[:80]!r}")
        return
    src = src.replace(old, new)

# ---------- contact & identity ----------
rep("`hello@oyin.design`", "`abubakarsadiqabdulazeez388@gmail.com`", 1)
rep("`+234 816 502 0995`", "`+234 705 187 7448`", 1)
rep("https://wa.me/2348165020995", "https://wa.me/2347051877448", 1)
rep("Fl=[{label:`Behance`,href:`https://www.behance.net/oyinkanrufai`},{label:`Instagram`,href:`https://www.instagram.com/designbyoyin`},{label:`LinkedIn`,href:`https://www.linkedin.com/in/oyinkansolarufai`}]",
    "Fl=[{label:`LinkedIn`,href:`https://www.linkedin.com/in/abdulazeez-sadiq`},{label:`Website`,href:`https://www.desynexia.com`}]", 1)
rep("sameAs:[`https://www.behance.net/oyinkanrufai`,`https://www.instagram.com/designbyoyin`,`https://www.linkedin.com/in/oyinkansolarufai`]",
    "sameAs:[`https://www.linkedin.com/in/abdulazeez-sadiq`,`https://www.desynexia.com`]", 1)
rep("wu=`https://www.oyin.design`", "wu=`https://www.desynexia.com`", 1)
rep("/about/oyin.jpg", "/about/sadiq.jpg")
rep("/logo-oyin-real.png", "/logo-sadiq.svg", 2)
rep("Oyin logo", "Sadiq logo", 2)
rep("Oyin, back to top", "Sadiq, back to top", 1)
rep("Email Oyin", "Email Sadiq", 1)
rep("` Oyin `", "` Sadiq `", 1)                        # footer © line
rep("children:[`Oyin`,(0,$.jsx)(`span`,{className:`ld-baseline`})]",
    "children:[`Sadiq`,(0,$.jsx)(`span`,{className:`ld-baseline`})]", 1)   # loader spec word
rep("children:[`Oyinkansola`,", "children:[`Abdulazeez`,", 1)              # expandable name
rep("alternateName:`Oyin`", "alternateName:`Sadiq`", 1)
rep("jobTitle:`Brand Designer`", "jobTitle:`Lead Product Designer`", 1)

# ---------- name & location ----------
rep("Rufai Oyinkansola, Lagos", "Sadiq Abdulazeez, Abuja")
rep("Rufai Oyinkansola — Brand Designer in Lagos", "Sadiq Abdulazeez — Product Designer in Abuja", 1)
rep("Rufai Oyinkansola (Oyin) is a brand identity designer in Lagos, Nigeria, crafting intentional brand experiences through brand strategy, visual identity, art direction and brand guidelines.",
    "Sadiq Abdulazeez is a lead product designer and strategist in Abuja, Nigeria, crafting intentional digital products across fintech, enterprise SaaS, mobility and marketplaces.", 1)
rep("Rufai Oyinkansola, brand designer", "Sadiq Abdulazeez, product designer")
rep("Rufai Oyinkansola", "Sadiq Abdulazeez")             # all remaining standalone
rep("Brand designer — Lagos", "Product designer — Abuja", 1)
rep("Brand designer, Lagos", "Product designer, Abuja", 1)
rep("`Lagos, `", "`Abuja, `", 1)                       # footer clock label
rep("addressLocality:`Lagos`", "addressLocality:`Abuja`", 1)
rep("based in Lagos", "based in Abuja", 1)
rep("a brand identity designer based in Abuja. I build thoughtful brands for businesses that want to be understood and taken seriously.",
    "a lead product designer based in Abuja. I design thoughtful digital products for teams that want clarity, momentum, and work that actually ships.", 1)

# ---------- seo / work meta ----------
rep("Work — Sadiq Abdulazeez, Brand Designer", "Work — Sadiq Abdulazeez, Product Designer", 1)
rep("Brand identities by Sadiq Abdulazeez, a brand designer in Lagos:", "Digital products by Sadiq Abdulazeez, a product designer in Abuja:", 1)
rep("Brand identity work by Sadiq Abdulazeez", "Product design work by Sadiq Abdulazeez", 1)
rep("— Brand Identity Case Study | Sadiq Abdulazeez", "— Product Design Case Study | Sadiq Abdulazeez", 1)
rep("a brand identity by Sadiq Abdulazeez, brand designer in Lagos.",
    "a product design project by Sadiq Abdulazeez, product designer in Abuja.", 1)
rep("brand identity by Sadiq Abdulazeez", "product design by Sadiq Abdulazeez")
rep("— Brand Identity | Sadiq Abdulazeez", "— Product Design | Sadiq Abdulazeez", 1)
rep("`${e.name} brand identity`", "`${e.name} product design`", 1)
rep("knowsAbout:[`Brand identity`,`Brand strategy`,`Visual identity`,`Art direction`,`Brand guidelines`]",
    "knowsAbout:[`Product design`,`Product strategy`,`UX research`,`Design systems`,`Prototyping`]", 1)
rep("[`Brand identity`,`Brand strategy`,`Visual identity`,`Art direction`,`Brand guidelines`],sameAs:Tu.sameAs",
    "[`Product design`,`Product strategy`,`UX research`,`Design systems`,`Prototyping`],sameAs:Tu.sameAs")

# ---------- hero & taglines ----------
rep("A brand designer crafting intentional brand experiences.",
    "A lead product designer crafting intentional digital experiences.", 1)
rep("Brands and identities, designed for people who are full of ideas.",
    "Digital products, designed for people who are full of ideas.")
rep("`Brands and identities,`", "`Digital products,`")
rep("`designed for people`", "`designed for people`")  # unchanged, keep for safety
rep("`who are full of ideas.`", "`who are full of ideas.`")

# ---------- the programme paragraph ----------
rep("children:[`I create `,o(`product`),` that give businesses a clear way to show up and be remembered. From the thinking behind the `,o(`brand`),` to the `,o(`system`),` that brings it to life, I work through the `,o(`proto`),` to make sure everything feels connected and true to the business.`]",
    "children:[`I design `,o(`product`),` that give businesses a clearer way to serve the people they are built for. From the `,o(`brand`),` behind the product to the `,o(`system`),` that brings it to life, I work through the `,o(`proto`),` to make sure everything feels connected and true to the user.`]", 1)

# ---------- process steps (zl = short, Bl = long) ----------
rep("{title:`Listen`,body:`I get to know the business, its audience, and what isn’t quite working yet.`}",
    "{title:`Discover`,body:`I get to know the product, its users, the business goals, and what isn’t quite working yet.`}", 1)
rep("{title:`Shape`,body:`Research and insight become a clear direction, shared early so everyone is aligned.`}",
    "{title:`Define`,body:`Research and insight become a clear product direction, shared early so everyone is aligned.`}", 1)
rep("{title:`Make`,body:`The identity comes to life: logo, type, colour, imagery, and the details that make it one system.`}",
    "{title:`Design`,body:`The experience comes to life: flows, interfaces, systems, and the details that make it one product.`}", 1)
rep("{title:`Refine`,body:`Feedback comes in, details get sharper, and the brand is tested across real applications.`}",
    "{title:`Refine`,body:`Feedback comes in, details get sharper, and the product is tested against real use and edge cases.`}", 1)
rep("{title:`Launch`,body:`A complete brand, with the files and guidelines that keep any team consistent as it grows.`}",
    "{title:`Ship`,body:`A complete, build-ready product, with the specs and systems that keep any team consistent as it grows.`}", 1)
rep("{title:`Listen`,body:`We start with a conversation. I get to know the business, what you’re trying to build, who you’re trying to reach, and what isn’t quite working yet.`}",
    "{title:`Discover`,body:`We start with a conversation. I get to know the product, what you’re trying to build, who you’re trying to reach, and what isn’t quite working yet.`}", 1)
rep("{title:`Shape`,body:`We bring the thinking together and start looking for a direction. Positioning, ideas, references, and visual territories begin to take shape.`}",
    "{title:`Define`,body:`We bring the thinking together and find a direction. User needs, flows, edge cases, and product priorities begin to take shape.`}", 1)
rep("{title:`Make`,body:`This is where the identity comes to life. I explore the logo, typography, colour, imagery, and the visual details that make the system feel like one thing.`}",
    "{title:`Design`,body:`This is where the product comes to life. I explore the flows, interfaces, components, and the details that make the experience feel like one thing.`}", 1)
rep("{title:`Refine`,body:`We step back, look at what we’ve made, and make it better. I refine the details, test the identity across different applications, and prepare everything for handoff.`}",
    "{title:`Refine`,body:`We step back, look at what we’ve made, and make it better. I refine the details, test the product against real scenarios, and prepare everything for handoff.`}", 1)
rep("{title:`Launch`,body:`You get a complete identity that’s ready to use, along with the files and guidelines needed to keep the brand consistent as it grows.`}",
    "{title:`Ship`,body:`You get a build-ready product with the specs, components and guidelines needed to keep the experience consistent as it grows.`}", 1)

# ---------- footer credit ----------
rep("href:`https://ifeoluwase.dev`", "href:`https://www.desynexia.com`", 1)
rep("children:`iea`", "children:`desynexia`", 1)

# ---------- preview decks (ml words + hl cards) ----------
ml_new = (
    "ml=["
    "{id:`product`,word:`products`,image:`/work/boldswitch-card.jpg`,caption:`Boldswitch, fintech app`,slug:`boldswitch`,color:`#0b3d91`,accent:`#9fc3dc`},"
    "{id:`brand`,word:`strategy`,image:`/work/lodapoint-hero.jpg`,caption:`Lodapoint, mobility platform`,slug:`lodapoint`,color:`#14532d`,accent:`#b7dcc3`},"
    "{id:`system`,word:`design systems`,image:`/work/boldswitch-business-hero.jpg`,caption:`Boldswitch Business, merchant app`,slug:`boldswitch-business`,color:`#7c2d12`,accent:`#e8c8b0`},"
    "{id:`proto`,word:`flows`,image:`/work/bravoo-hero.jpg`,caption:`Bravoo, UK banking`,slug:`bravoo`,color:`#4c1d95`,accent:`#cfc0ea`}],hl=")
hl_new = (
    "[{image:`/work/boldswitch-hero.jpg`,caption:`Boldswitch, borderless banking`,slug:`boldswitch`,color:`#0b3d91`,accent:`#9fc3dc`},"
    "{image:`/work/lodapoint-driver.jpg`,caption:`Lodapoint Driver, gig app`,slug:`lodapoint`,color:`#14532d`,accent:`#b7dcc3`},"
    "{image:`/work/bravoo-web.jpg`,caption:`Bravoo, marketing site`,slug:`bravoo`,color:`#4c1d95`,accent:`#cfc0ea`},"
    "{image:`/work/boldswitch-business-dash.jpg`,caption:`Boldswitch Business dashboard`,slug:`boldswitch-business`,color:`#7c2d12`,accent:`#e8c8b0`}],gl=")
src2 = re.sub(r"ml=\[.*?\],hl=", lambda m: ml_new, src, count=1, flags=re.S)
if src2 == src: fails.append("[miss] ml array")
src = src2
src2 = re.sub(r"hl=\[.*?\],gl=", lambda m: "hl=" + hl_new, src, count=1, flags=re.S)
if src2 == src: fails.append("[miss] hl array")
src = src2

# ---------- work arrays: 4 full case studies, no "coming soon" ----------
def img(fn, slug): return f"{fn}(`{{}}`)".format(slug)

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
 dict(slug="bravoo", helper="T", name="Bravoo",
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

w_new = "x=b(`boldswitch`),S=b(`boldswitch-business`),C=b(`lodapoint`),T=b(`bravoo`),w=[" + ",".join(build_project(p) for p in projects) + "],j=[],Au="
src2 = re.sub(r"x=b\(`vitalcare-plus`\),S=b\(`itours-travels`\),C=b\(`vibe-oasis`\),w=\[.*?\],j=\[.*?\],Au=",
              lambda m: w_new, src, count=1, flags=re.S)
if src2 == src: fails.append("[miss] w/j arrays")
src = src2

open(JS, "w", encoding="utf-8").write(src)

# ---------- index.html ----------
H = "index.html"
h = open(H, encoding="utf-8").read()
subs = [
 ("Rufai Oyinkansola — Brand Designer in Lagos", "Sadiq Abdulazeez — Product Designer in Abuja"),
 ("Rufai Oyinkansola (Oyin) is a brand identity designer in Lagos, Nigeria, crafting intentional brand experiences through brand strategy, visual identity, art direction and brand guidelines.",
  "Sadiq Abdulazeez is a lead product designer and strategist in Abuja, Nigeria, crafting intentional digital products across fintech, enterprise SaaS, mobility and marketplaces."),
 ('"name":"Rufai Oyinkansola","alternateName":"Oyin","jobTitle":"Brand Designer","email":"mailto:hello@oyin.design","url":"https://www.oyin.design/"',
  '"name":"Sadiq Abdulazeez","alternateName":"Sadiq","jobTitle":"Lead Product Designer","email":"mailto:abubakarsadiqabdulazeez388@gmail.com","url":"https://www.desynexia.com/"'),
 ('"name":"Rufai Oyinkansola"', '"name":"Sadiq Abdulazeez"'),
 ("https://www.oyin.design/about/oyin.jpg", "https://www.desynexia.com/about/sadiq.jpg"),
 ('"addressLocality":"Lagos"', '"addressLocality":"Abuja"'),
 ('"knowsAbout":["Brand identity","Brand strategy","Visual identity","Art direction","Brand guidelines"]',
  '"knowsAbout":["Product design","Product strategy","UX research","Design systems","Prototyping"]'),
 ('"sameAs":["https://www.behance.net/oyinkanrufai","https://www.instagram.com/designbyoyin","https://www.linkedin.com/in/oyinkansolarufai"]',
  '"sameAs":["https://www.linkedin.com/in/abdulazeez-sadiq","https://www.desynexia.com"]'),
 ("https://www.oyin.design/", "https://www.desynexia.com/"),
 ('"author":{"@id":"https://www.desynexia.com/#person"}', '"author":{"@id":"https://www.desynexia.com/#person"}'),
 ("Rufai Oyinkansola", "Sadiq Abdulazeez"),
]
for old, new in subs:
    if old in h:
        h = h.replace(old, new)
    elif new not in h:
        fails.append(f"[html miss] {old[:80]!r}")
open(H, "w", encoding="utf-8").write(h)

# ---------- report ----------
leftover = [w for w in ("Oyin", "oyin", "Rufai", "Lagos", "behance.net/oyinkanrufai", "designbyoyin", "oyinkansolarufai") if w in src]
if leftover: fails.append(f"[leftover in js] {leftover}")
leftover_h = [w for w in ("Oyin", "oyin", "Rufai", "oyinkanrufai", "designbyoyin") if w in h]
if leftover_h: fails.append(f"[leftover in html] {leftover_h}")

print("\n".join(fails) if fails else "ALL OK — no Oyin references remain")
sys.exit(1 if fails else 0)

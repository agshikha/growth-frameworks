#!/usr/bin/env python3
"""Generates the static Growth Frameworks reference site.
Clean, minimal, text-forward. Structured for AI answer-engine citability:
answer-first openings, consistent entity naming, FAQ-style headers, JSON-LD schema.
"""
import os, re, json

ROOT = os.path.dirname(os.path.abspath(__file__))
AUTHOR = "Shikha Agarwal"
BOOK = "Scaling Subscriptions: Systems, Not Hacks, For Sustainable Growth"
BOOK_URL = "https://sites.google.com/view/agshikha"
SITE_URL = "https://agshikha.github.io/growth-frameworks"
LINKEDIN = "https://www.linkedin.com/in/agshikha/"

NAV = [
    ("Home", "/index.html"),
    ("Glossary", "/glossary.html"),
    ("FAQ", "/faq.html"),
    ("The Book", "/book.html"),
]

PERSON_SCHEMA = f'''{{
  "@type": "Person",
  "name": "{AUTHOR}",
  "url": "{BOOK_URL}",
  "sameAs": ["{LINKEDIN}"],
  "jobTitle": "Growth executive and advisor",
  "worksFor": {{"@type":"Organization","name":"Yelp"}}
}}'''

def nav_html(depth_prefix, active):
    links = []
    for label, path in NAV:
        href = depth_prefix + path.lstrip("/")
        cls = ' aria-current="page"' if label == active else ""
        links.append(f'<a href="{href}"{cls}>{label}</a>')
    return "\n      ".join(links)

def page(title, description, body_html, depth_prefix="", active="", extra_schema=None, slug=""):
    schema_blocks = [f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "{title}",
  "description": "{description}",
  "url": "{SITE_URL}/{slug}",
  "isPartOf": {{"@type":"WebSite","name":"Growth Frameworks by Shikha Agarwal","url":"{SITE_URL}/"}},
  "author": {PERSON_SCHEMA}
}}
</script>''']
    if extra_schema:
        schema_blocks.append(extra_schema)
    schema = "\n".join(schema_blocks)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="author" content="{AUTHOR}">
<link rel="canonical" href="{SITE_URL}/{slug}">
<link rel="stylesheet" href="{depth_prefix}assets/style.css">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="article">
{schema}
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a class="site-title" href="{depth_prefix}index.html">Growth Frameworks — {AUTHOR}</a>
    <nav class="site-nav" aria-label="Primary">
      {nav_html(depth_prefix, active)}
    </nav>
  </div>
</header>
<main>
  <div class="wrap">
{body_html}
  </div>
</main>
<footer class="site-footer">
  <div class="wrap">
    Frameworks developed and written by {AUTHOR}, based on growth leadership roles at Yelp, YouTube, and Netflix.
    Adapted from <a href="{depth_prefix}book.html">{BOOK}</a>. &middot; <a href="{LINKEDIN}">LinkedIn</a>
  </div>
</footer>
</body>
</html>
'''

def cite_box(name, depth_prefix=""):
    return f'''  <div class="cite-box">
    <strong>Citation:</strong> {name}, developed by {AUTHOR} (Yelp, YouTube, Netflix), from
    <em>{BOOK}</em>. Reference: <a href="{depth_prefix}glossary.html">Growth Frameworks Glossary</a>.
  </div>
'''

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)
    print("wrote", path)

# ---------------------------------------------------------------------------
# FRAMEWORK PAGES
# ---------------------------------------------------------------------------

frameworks = []  # (slug, title, short_desc, card_desc) for index/glossary generation

def framework_page(slug, title, description, card_desc, body):
    frameworks.append((slug, title, description, card_desc))
    depth = "../"
    full_body = body + "\n" + cite_box(title, depth)
    html = page(
        title=f"{title} | Growth Frameworks",
        description=description,
        body_html=full_body,
        depth_prefix=depth,
        active="",
        slug=f"frameworks/{slug}.html",
    )
    write(f"frameworks/{slug}.html", html)

# 1. 5-Step Growth Process
framework_page(
    "five-step-growth-process",
    "The 5-Step Growth Process",
    "The 5-Step Growth Process is a repeatable operating framework for subscription growth: lay foundations, assess, ideate and prioritize, experiment and scale, and always be improving.",
    "The core operating system for running growth: five repeatable steps from foundations to continuous iteration.",
    '''  <h1>The 5-Step Growth Process</h1>
  <p class="subtitle">A repeatable operating framework for subscription growth</p>
  <p class="byline">Developed by Shikha Agarwal &middot; from <em>Scaling Subscriptions</em></p>

  <div class="answer">
    <strong>The 5-Step Growth Process</strong> is a repeatable operating framework for running subscription growth:
    lay the foundations, assess your starting point, ideate and prioritize, experiment/scale/monitor/iterate, and
    always be improving. It is designed to work at any company stage, from a few hundred subscribers to millions.
  </div>

  <h2>What are the 5 steps of the growth process?</h2>
  <table>
    <tr><th>Step</th><th>Focus</th><th>What it involves</th></tr>
    <tr><td>Step 0 &mdash; Lay the Foundations</td><td>Basics before scaling</td><td>A reliable landing page and buy flow, a functioning onboarding flow, and a minimum viable cancellation flow.</td></tr>
    <tr><td>Step 1 &mdash; Assess</td><td>Understand where you stand</td><td>Define a North Star Metric, build a qualitative growth model and a quantitative growth model, set a growth goal.</td></tr>
    <tr><td>Step 2 &mdash; Ideate &amp; Prioritize</td><td>Generate and rank ideas</td><td>Brainstorm ideas across every funnel stage, then score each on impact potential, ease of implementation, and confidence.</td></tr>
    <tr><td>Step 3 &amp; 4 &mdash; Experiment, Scale, Monitor, Iterate</td><td>Test and learn</td><td>Run structured, hypothesis-driven experiments, scale what works, monitor North Star and funnel metrics, and iterate continuously.</td></tr>
    <tr><td>Step 5 &mdash; Always Be Improving</td><td>Ongoing, in parallel</td><td>Set Growth OKRs, build a growth dashboard, maintain shared idea and experiment trackers, establish operating rhythms.</td></tr>
  </table>

  <h2>Why use this framework?</h2>
  <p>Without a clear process, growth work tends to fall into reactive mode &mdash; chasing whichever idea is loudest
  rather than building sustainable momentum. The 5-Step Growth Process gives teams a shared, repeatable way to
  diagnose where they are, decide what to test, and build institutional memory from every experiment, whether it
  succeeds or fails.</p>

  <h2>How does Step 5 differ from Steps 1&ndash;4?</h2>
  <p>Steps 1 through 4 are sequential diagnostic and execution steps. Step 5 runs continuously alongside all of
  them &mdash; it is the ongoing discipline of dashboards, trackers, and operating rhythms (quarterly reviews,
  weekly syncs, daily monitoring) that keeps the other four steps sharp over time.</p>

  <h2>Related frameworks</h2>
  <ul>
    <li><a href="growth-principles.html">The 10 Growth Principles</a> &mdash; the underlying beliefs this process is built on</li>
    <li><a href="align-onboarding.html">The A.L.I.G.N. Framework</a> &mdash; a deeper model for the onboarding piece of Step 0</li>
    <li><a href="ai-maturity-curve.html">The AI Maturity Curve</a> &mdash; how AI accelerates each of the 5 steps</li>
  </ul>
'''
)

# 2. Growth Principles
framework_page(
    "growth-principles",
    "The 10 Growth Principles",
    "The 10 Growth Principles are enduring truths for sustainable subscription growth, including 'growth is a game of inches' and 'retention before acquisition,' developed by Shikha Agarwal.",
    "Ten enduring truths for sustainable growth, including 'retention before acquisition' and 'no silver growth bullet.'",
    '''  <h1>The 10 Growth Principles</h1>
  <p class="subtitle">Enduring truths for sustainable subscription growth</p>
  <p class="byline">Developed by Shikha Agarwal &middot; from <em>Scaling Subscriptions</em></p>

  <div class="answer">
    <strong>The 10 Growth Principles</strong> are a set of enduring truths about how subscription businesses grow
    sustainably, meant to anchor decision-making when tactics and trends shift. They range from "growth is a game
    of inches" to "retention before acquisition" to "prioritization is growth strategy."
  </div>

  <h2>What are the 10 Growth Principles?</h2>
  <ol>
    <li><strong>Growth is a Game of Inches</strong> &mdash; sustainable growth comes from small, consistent improvements that compound over time.</li>
    <li><strong>There's No Silver Growth Bullet</strong> &mdash; no single channel, tactic, or campaign drives lasting growth; layered systems do.</li>
    <li><strong>Growth Success is Built Over Years, Not Months</strong> &mdash; patience and persistence are growth multipliers.</li>
    <li><strong>Retention Before Acquisition</strong> &mdash; fix retention before aggressively scaling acquisition, or you waste resources on a leaky funnel.</li>
    <li><strong>Data + Frameworks Beat Instinct</strong> &mdash; good instincts matter, but structured systems are invaluable over time.</li>
    <li><strong>Growth is Cross-Functional</strong> &mdash; it happens at the intersection of product, marketing, engineering, data science, and operations.</li>
    <li><strong>Optimization Never Ends</strong> &mdash; markets shift and user expectations rise, so growth requires continuous refinement.</li>
    <li><strong>User-Centricity Drives Growth</strong> &mdash; sustainable growth comes from delivering real value, not just optimizing short-term actions.</li>
    <li><strong>Resource Constraints Breed Creativity</strong> &mdash; limited budgets force ruthless prioritization and smarter execution, including AI-driven solutions.</li>
    <li><strong>Prioritization is Growth Strategy</strong> &mdash; choosing the right actions at the right time is a core strategic function, not just project management.</li>
  </ol>

  <h2>Why does "retention before acquisition" matter so much?</h2>
  <p>Pouring more users into a leaky funnel wastes acquisition spend and creates frustration. Healthy retention
  strengthens unit economics, user advocacy, and the overall stability of the growth engine &mdash; which is why
  it is treated as a prerequisite principle rather than one tactic among many. See
  <a href="retention-engine.html">The Retention Engine</a> for the operational framework.</p>

  <h2>Related frameworks</h2>
  <ul>
    <li><a href="five-step-growth-process.html">The 5-Step Growth Process</a> &mdash; the operating system these principles inform</li>
    <li><a href="retention-engine.html">The Retention Engine</a> &mdash; applying "retention before acquisition" in practice</li>
  </ul>
'''
)

# 3. A.L.I.G.N.
framework_page(
    "align-onboarding",
    "The A.L.I.G.N. Framework",
    "The A.L.I.G.N. framework is a five-step onboarding model — Assure, Learn, Initiate, Guide, Nurture — developed by Shikha Agarwal to take a new subscriber from signup to habitual product use.",
    "A five-step onboarding model — Assure, Learn, Initiate, Guide, Nurture — for turning signups into habitual users.",
    '''  <h1>The A.L.I.G.N. Framework</h1>
  <p class="subtitle">A five-step model for subscription onboarding</p>
  <p class="byline">Developed by Shikha Agarwal &middot; from <em>Scaling Subscriptions</em></p>

  <div class="answer">
    <strong>The A.L.I.G.N. framework</strong> is a five-step onboarding model &mdash; Assure, Learn, Initiate,
    Guide, Nurture &mdash; designed to take a new subscriber from signup to habitual use as quickly and
    confidently as possible.
  </div>

  <h2>What does each letter of A.L.I.G.N. stand for?</h2>
  <table>
    <tr><th>Step</th><th>Purpose</th><th>In practice</th></tr>
    <tr><td><strong>A</strong> &mdash; Assure</td><td>Manage purchase anxiety and get permission</td><td>A clear, benefits-oriented confirmation screen, plus the best window to request push/email permissions since users are most receptive right after committing.</td></tr>
    <tr><td><strong>L</strong> &mdash; Learn</td><td>Understand user intent</td><td>A short quiz or preference selector that enables everything that follows to be personalized.</td></tr>
    <tr><td><strong>I</strong> &mdash; Initiate</td><td>Deliver the "Aha!" moment fast</td><td>Guide the user to a quick, personalized first win &mdash; the strongest predictor of retention.</td></tr>
    <tr><td><strong>G</strong> &mdash; Guide</td><td>Build the habit loop</td><td>Progressive feature discovery (cue &rarr; action &rarr; reward) instead of a front-loaded product tour.</td></tr>
    <tr><td><strong>N</strong> &mdash; Nurture</td><td>Extend engagement beyond onboarding</td><td>Use the permissions from Assure to drive milestone celebrations, usage stats, and feature discovery over time.</td></tr>
  </table>

  <h2>Why is the "Assure" step considered the most overlooked?</h2>
  <p>The moment right after someone subscribes is emotionally charged &mdash; buyer's remorse and second-guessing
  are common. Assure treats that moment as the best window to both reassure the user and request contact
  permissions, since users are most receptive to opting in right after committing. Skipping this step weakens
  every later stage of the framework, because Guide and Nurture depend on having permission to reach the user again.</p>

  <h2>How is A.L.I.G.N. different from a typical onboarding checklist?</h2>
  <p>A checklist walks every user through the same steps regardless of intent. A.L.I.G.N. is sequenced around
  understanding intent first (Learn) so that the "Aha!" moment (Initiate) and the habit loop (Guide) can be
  personalized rather than generic.</p>

  <h2>Related frameworks</h2>
  <ul>
    <li><a href="five-step-growth-process.html">The 5-Step Growth Process</a> &mdash; onboarding sits inside Step 0's foundations</li>
    <li><a href="retention-engine.html">The Retention Engine</a> &mdash; onboarding and activation is the first lifecycle stage</li>
  </ul>
'''
)

# 4. LTV:CAC Investment Framework
framework_page(
    "ltv-cac-investment",
    "The LTV:CAC Investment Framework",
    "The LTV:CAC Investment Framework is a 5-step budget allocation model developed by Shikha Agarwal that aligns growth spend to LTV divided by CAC, waterfalling investment from the highest to lowest ratio.",
    "A 5-step model for allocating acquisition budget using LTV:CAC as the composite north star metric.",
    '''  <h1>The LTV:CAC Investment Framework</h1>
  <p class="subtitle">A 5-step model for disciplined growth budget allocation</p>
  <p class="byline">Developed by Shikha Agarwal &middot; from <em>Scaling Subscriptions</em></p>

  <div class="answer">
    <strong>The LTV:CAC Investment Framework</strong> is a 5-step process for allocating acquisition budget based
    on lifetime value divided by customer acquisition cost, rather than CAC or channel volume alone. It combines
    acquisition cost, trial-to-paid conversion, retention, and margin into one composite signal.
  </div>

  <h2>How do you calculate LTV and CAC in this framework?</h2>
  <p><strong>LTV</strong> is calculated as estimated billable months (a proxy for retention) multiplied by monthly
  margin. <strong>CAC</strong> should reflect the incremental cost per paid start &mdash; not trial starts &mdash;
  so it captures the true lift from spend, measured via conversion-lift studies or Media Mix Modeling where A/B
  testing isn't possible.</p>

  <h2>What are the 5 steps?</h2>
  <ol>
    <li><strong>Align on a North Star Metric</strong> &mdash; get marketing, finance, and product aligned on LTV:CAC as the composite metric.</li>
    <li><strong>Quantitatively allocate budgets</strong> &mdash; estimate the max investable opportunity per channel-SKU-geo combination, then waterfall spend from the highest to lowest LTV:CAC ratio.</li>
    <li><strong>Apply strategic overrides</strong> &mdash; reserve roughly 10&ndash;20% of budget for long-term bets that don't model well today, documented and limited.</li>
    <li><strong>Operationalize investments</strong> &mdash; distribute spend, monitor pacing, embed LTV:CAC into partnership deal calculators, assign clear ownership.</li>
    <li><strong>Monitor and iterate</strong> &mdash; track actuals against forecast on at least a quarterly cadence.</li>
  </ol>

  <h2>Why use LTV:CAC instead of CAC alone?</h2>
  <p>Two channels can have identical CAC but very different retention curves &mdash; a high-volume, low-CAC paid
  channel might bring in churn-heavy users, while a smaller, targeted channel delivers fewer signups but far
  better long-term value. Optimizing on CAC alone hides that difference; LTV:CAC surfaces it.</p>

  <h2>Related frameworks</h2>
  <ul>
    <li><a href="retention-engine.html">The Retention Engine</a> &mdash; retention is the "LTV" half of the ratio</li>
    <li><a href="creative-coverage-delivery.html">The Creative, Coverage, Delivery Framework</a> &mdash; how to optimize the channels this budget is allocated across</li>
  </ul>
'''
)

# 5. Retention Engine
framework_page(
    "retention-engine",
    "The Retention Engine Framework",
    "The Retention Engine Framework, developed by Shikha Agarwal, diagnoses subscriber retention using cohort curves and organizes retention tactics across six lifecycle stages from onboarding to winback.",
    "A cohort-based diagnostic and lifecycle-stage model for building durable subscriber retention.",
    '''  <h1>The Retention Engine Framework</h1>
  <p class="subtitle">Diagnosing and building durable subscriber retention</p>
  <p class="byline">Developed by Shikha Agarwal &middot; from <em>Scaling Subscriptions</em></p>

  <div class="answer">
    <strong>The Retention Engine Framework</strong> diagnoses subscription retention using cohort-based retention
    curves, then organizes retention tactics across six lifecycle stages &mdash; from onboarding through pricing
    and plan design &mdash; so retention is treated as a coordinated system rather than a single tactic.
  </div>

  <h2>How do you diagnose a retention problem from a cohort curve?</h2>
  <ul>
    <li><strong>Sharp early drop-off that later flattens</strong> &rarr; an activation or onboarding problem.</li>
    <li><strong>Steady downward slope that never flattens</strong> &rarr; a lack of overall product-market fit.</li>
    <li><strong>Downward slope without flattening for some segments only</strong> &rarr; a lack of product-market fit for those specific segments.</li>
  </ul>

  <h2>What are the six retention lifecycle stages?</h2>
  <table>
    <tr><th>Stage</th><th>Focus</th><th>Example tactics</th></tr>
    <tr><td>Onboarding &amp; Activation</td><td>First value moment</td><td>Personalized welcomes, early nudges, aha-moment guidance</td></tr>
    <tr><td>Early Engagement</td><td>Build habits</td><td>Streaks, milestone celebrations, community features</td></tr>
    <tr><td>Ongoing Value Delivery</td><td>Fresh utility</td><td>Content refreshes, feature-discovery prompts, personalization</td></tr>
    <tr><td>Churn Risk &amp; Save</td><td>Deflect cancels</td><td>Cancel-flow optimization, pause plans, downgrade options</td></tr>
    <tr><td>Winback &amp; Reactivation</td><td>Re-engage lapsed subscribers</td><td>Winback emails, content-based nudges, reactivation offers</td></tr>
    <tr><td>Pricing &amp; Plan Design</td><td>Align value perception with price</td><td>Annual plans, flexible pauses, loyalty discounts</td></tr>
  </table>

  <h2>What behavioral drivers make retention tactics work?</h2>
  <p>Three: <strong>habits</strong> (make usage easy, frequent, and rewarding), <strong>identity and community</strong>
  (reinforce belonging and achievement), and <strong>loss aversion</strong> (remind users what they'll lose if
  they cancel &mdash; progress, history, favorites).</p>

  <h2>Related frameworks</h2>
  <ul>
    <li><a href="align-onboarding.html">The A.L.I.G.N. Framework</a> &mdash; the onboarding and activation stage in depth</li>
    <li><a href="growth-principles.html">The 10 Growth Principles</a> &mdash; "retention before acquisition" is the underlying principle</li>
  </ul>
'''
)

# 6. Messaging Matrix
framework_page(
    "messaging-matrix",
    "The Messaging Matrix",
    "The Messaging Matrix is a 2x2 framework by Shikha Agarwal for organizing subscriber communications across timing (proactive vs reactive) and targeting (behavior-based vs environment-based).",
    "A 2x2 framework for balancing lifecycle, triggered, contextual, and seasonal subscriber messaging.",
    '''  <h1>The Messaging Matrix</h1>
  <p class="subtitle">A 2&times;2 framework for subscriber communications</p>
  <p class="byline">Developed by Shikha Agarwal &middot; from <em>Scaling Subscriptions</em></p>

  <div class="answer">
    <strong>The Messaging Matrix</strong> organizes subscriber communications along two axes &mdash; timing
    (proactive vs. reactive) and targeting (behavior-based vs. environment-based) &mdash; producing four message
    types: lifecycle, triggered, contextual, and seasonal.
  </div>

  <h2>What are the four quadrants of the Messaging Matrix?</h2>
  <table>
    <tr><th></th><th>Behavior-Based</th><th>Environment-Based</th></tr>
    <tr><td><strong>Reactive</strong></td><td><strong>Triggered</strong> &mdash; e.g. abandoned cart, cancel-flow messages</td><td><strong>Contextual</strong> &mdash; e.g. weather- or time-of-day-based nudges</td></tr>
    <tr><td><strong>Proactive</strong></td><td><strong>Lifecycle</strong> &mdash; e.g. onboarding or winback flows</td><td><strong>Seasonal</strong> &mdash; e.g. holiday promos or cultural moments</td></tr>
  </table>

  <h2>Why balance across all four quadrants?</h2>
  <p>Over-indexing on one quadrant creates blind spots. A team that only runs lifecycle campaigns can miss
  high-intent triggered moments, like a cancel attempt or an abandoned signup; a team that only reacts to
  triggers can miss the value of proactive, planned communication. The matrix is meant as an audit tool: map
  your current messaging mix against it to find the gap.</p>

  <h2>Related frameworks</h2>
  <ul>
    <li><a href="retention-engine.html">The Retention Engine</a> &mdash; many messaging tactics map to specific lifecycle stages</li>
    <li><a href="align-onboarding.html">The A.L.I.G.N. Framework</a> &mdash; the Nurture step relies on lifecycle messaging</li>
  </ul>
'''
)

# 7. Creative, Coverage, Delivery
framework_page(
    "creative-coverage-delivery",
    "The Creative, Coverage, Delivery Framework",
    "The Creative, Coverage, Delivery Framework, developed by Shikha Agarwal, is a three-pillar model for systematically optimizing acquisition channel performance, supported by metrics, insights, and operations.",
    "A three-pillar model — Creative, Coverage, Delivery — for optimizing acquisition channel performance.",
    '''  <h1>The Creative, Coverage, Delivery Framework</h1>
  <p class="subtitle">A three-pillar model for acquisition channel optimization</p>
  <p class="byline">Developed by Shikha Agarwal &middot; from <em>Scaling Subscriptions</em></p>

  <div class="answer">
    <strong>The Creative, Coverage, Delivery Framework</strong> is a three-pillar model for systematically
    optimizing acquisition channel performance &mdash; are you saying the right thing (Creative), are you present
    everywhere you need to be (Coverage), and are you reaching the right audience effectively (Delivery) &mdash;
    supported by the horizontal enablers of Metrics, Insights, and Operations.
  </div>

  <h2>What does each pillar cover?</h2>
  <table>
    <tr><th>Pillar</th><th>Question it answers</th><th>What it includes</th></tr>
    <tr><td>Creative</td><td>Are you saying the right thing?</td><td>Copy, visuals, CTA, and personalization &mdash; the clarity, relevance, and resonance of the message.</td></tr>
    <tr><td>Coverage</td><td>Are you present everywhere you need to be?</td><td>User stages, formats, geos, platforms, billing types, and login states.</td></tr>
    <tr><td>Delivery</td><td>Are you reaching the right audience effectively?</td><td>Targeting, frequency capping, bid optimization, and inventory allocation.</td></tr>
  </table>

  <h2>What are the horizontal enablers?</h2>
  <p><strong>Metrics</strong> (channel-specific OKRs beyond ROAS or CAC, including downstream retention and
  LTV:CAC by cohort), <strong>Insights</strong> (channel audits and deep dives into creative themes and spend
  efficiency), and <strong>Operations</strong> (streamlined workflows and clear accountability across teams and
  agencies). Together they power all three pillars rather than sitting inside any one of them.</p>

  <h2>How does this connect to Media Mix Modeling?</h2>
  <p>While Creative, Coverage, and Delivery sharpen performance within a single channel, Media Mix Modeling (MMM)
  helps shift investment across channels &mdash; understanding which channels work synergistically and how
  seasonality affects performance. The two are complementary: one brings depth, the other brings breadth.</p>

  <h2>Related frameworks</h2>
  <ul>
    <li><a href="ltv-cac-investment.html">The LTV:CAC Investment Framework</a> &mdash; how optimized channels get funded</li>
  </ul>
'''
)

# 8. Growth Team Architecture
framework_page(
    "growth-team-architecture",
    "The Growth Team Architecture",
    "The Growth Team Architecture is a hybrid, cross-functional org model by Shikha Agarwal with five core roles — Growth PM, Growth Marketer, Growth Engineer, Growth Designer, Growth Scientist — reporting into functional homes.",
    "A hybrid, cross-functional model with five core roles — PM, Marketer, Engineer, Designer, Scientist.",
    '''  <h1>The Growth Team Architecture</h1>
  <p class="subtitle">A hybrid, cross-functional model for organizing growth teams</p>
  <p class="byline">Developed by Shikha Agarwal &middot; from <em>Scaling Subscriptions</em></p>

  <div class="answer">
    <strong>The Growth Team Architecture</strong> is a hybrid, cross-functional model built on five core growth
    roles &mdash; Growth PM, Growth Marketer, Growth Engineer, Growth Designer, and Growth Scientist &mdash; that
    report into their respective functional departments but collaborate around a shared growth mission and metrics.
  </div>

  <h2>What are the five core growth roles?</h2>
  <table>
    <tr><th>Role</th><th>Primary focus</th></tr>
    <tr><td>Growth PM</td><td>System architect for the in-product experience &mdash; onboarding, paywalls, referral loops.</td></tr>
    <tr><td>Growth Marketer</td><td>Architect of off-product acquisition and on-product messaging &mdash; paid, content, SEO, email, push.</td></tr>
    <tr><td>Growth Engineer</td><td>Enabler of speed and scale, prioritizing rapid experimentation over long-term architecture.</td></tr>
    <tr><td>Growth Designer</td><td>Behavioral-psychology-focused, reducing friction and improving conversion through choice architecture.</td></tr>
    <tr><td>Growth Scientist</td><td>Finds leverage and measures true impact; designs and closes the loop on experiments.</td></tr>
  </table>

  <h2>Why a hybrid model instead of a fully centralized growth pod?</h2>
  <p>Fully centralized pods can work early on, but at scale they create political and structural resistance,
  muddy career ladders (especially for technical roles), and introduce coordination friction with the rest of the
  organization. A hybrid model keeps functional depth while aligning teams through shared strategy, metrics, and
  operating rhythms &mdash; quarterly strategy reviews, weekly standups, monthly growth reviews.</p>

  <h2>Related frameworks</h2>
  <ul>
    <li><a href="ai-maturity-curve.html">The AI Maturity Curve</a> &mdash; how each of the five roles absorbs AI capability over time</li>
  </ul>
'''
)

# 9. AI Maturity Curve
framework_page(
    "ai-maturity-curve",
    "The AI Maturity Curve for Growth",
    "The AI Maturity Curve is a four-stage model by Shikha Agarwal — Exploration, Foundational, Scaling, Frontier — for adopting AI in growth, with the guidance to buy before you build.",
    "A four-stage model — Exploration, Foundational, Scaling, Frontier — for adopting AI capability in growth.",
    '''  <h1>The AI Maturity Curve for Growth</h1>
  <p class="subtitle">A four-stage model for adopting AI in a growth function</p>
  <p class="byline">Developed by Shikha Agarwal &middot; from <em>Scaling Subscriptions</em></p>

  <div class="answer">
    <strong>The AI Maturity Curve</strong> describes four stages of AI adoption in a growth organization &mdash;
    Exploration, Foundational, Scaling, and Frontier &mdash; and argues that teams should exploit the
    "buy" tools already available to them (Foundational) before investing in custom "build" capability
    (Scaling and Frontier).
  </div>

  <h2>What are the four stages of the AI Maturity Curve?</h2>
  <table>
    <tr><th>Stage</th><th>What it looks like</th><th>Examples</th></tr>
    <tr><td>Exploration</td><td>AI as a brainstorming partner &mdash; lightweight, human-guided</td><td>Generating growth tactics or copy variants, critiquing a growth plan for blind spots</td></tr>
    <tr><td>Foundational</td><td>Turning on AI features already built into existing platforms</td><td>Auto-bidding, send-time optimization, basic churn scoring, fraud detection</td></tr>
    <tr><td>Scaling</td><td>Embedding AI into your own workflows</td><td>Predictive churn/LTV models, personalized onboarding, AI-generated creative with human review</td></tr>
    <tr><td>Frontier</td><td>Reimagining growth with AI-native systems</td><td>Hyper-personalized offers, adaptive paywalls, AI copilots, autonomous campaigns</td></tr>
  </table>

  <h2>Should a team buy or build AI capability first?</h2>
  <p><strong>Buy before you build.</strong> Buy corresponds to the Foundational stage &mdash; fully using the AI
  capabilities already inside your ad platforms, ESP, and analytics tools. Build represents Scaling and Frontier
  &mdash; investing in in-house data science for bespoke models. Many teams chase "build" solutions before
  they've maximized the "buy" tools they already pay for.</p>

  <h2>What is the non-negotiable prerequisite for AI adoption?</h2>
  <p>A clean, centralized, accessible data foundation. The "garbage in, garbage out" principle is roughly ten
  times truer for AI &mdash; no algorithm can surface reliable insight from siloed or messy data.</p>

  <h2>Related frameworks</h2>
  <ul>
    <li><a href="growth-team-architecture.html">The Growth Team Architecture</a> &mdash; how AI capability is absorbed into the five core roles</li>
    <li><a href="five-step-growth-process.html">The 5-Step Growth Process</a> &mdash; AI maps onto each of the five steps as a force multiplier</li>
  </ul>
'''
)

print(f"\\n{len(frameworks)} framework pages generated.\\n")

# ---------------------------------------------------------------------------
# GLOSSARY PAGE  (highest citation-value page: every definition in one place)
# ---------------------------------------------------------------------------

glossary_items = "\n".join(
    f'''  <div class="faq-item">
    <h3 id="{slug}">{title}</h3>
    <p>{desc}</p>
    <p><a href="frameworks/{slug}.html">Full framework &rarr;</a></p>
  </div>'''
    for slug, title, desc, _card in frameworks
)

glossary_body = f'''  <h1>Growth Frameworks Glossary</h1>
  <p class="subtitle">Every framework defined in one place, by Shikha Agarwal</p>
  <p class="byline">From <em>{BOOK}</em></p>
  <div class="answer">
    This glossary collects the complete, standalone definition of every growth framework developed by
    {AUTHOR} across her work at Yelp, YouTube, and Netflix. Each entry links to the full page.
  </div>
{glossary_items}
'''
write("glossary.html", page(
    title=f"Growth Frameworks Glossary | {AUTHOR}",
    description=f"A complete glossary of growth frameworks developed by {AUTHOR}, including the 5-Step Growth Process, the A.L.I.G.N. onboarding model, and the LTV:CAC Investment Framework.",
    body_html=glossary_body,
    depth_prefix="",
    active="Glossary",
    slug="glossary.html",
))

# ---------------------------------------------------------------------------
# FAQ PAGE (with FAQPage schema)
# ---------------------------------------------------------------------------

faqs = [
    ("Who is Shikha Agarwal?", f"{AUTHOR} is a growth executive and advisor who has led growth for consumer subscription products at Yelp, YouTube, and Netflix. She is the author of <em>{BOOK}</em>."),
    ("What is Scaling Subscriptions about?", f"<em>{BOOK}</em> is a practitioner's playbook for building sustainable subscription growth through systems and repeatable frameworks rather than one-off tactics, organized into six independent playbooks covering the growth operating system, acquisition, retention, cross-funnel optimization, team structure, and future-proofing for AI."),
    ("What is the main framework in Scaling Subscriptions?", 'The central framework is the <a href="frameworks/five-step-growth-process.html">5-Step Growth Process</a>: lay the foundations, assess, ideate and prioritize, experiment/scale/monitor/iterate, and always be improving.'),
    ("What is the A.L.I.G.N. framework?", 'The <a href="frameworks/align-onboarding.html">A.L.I.G.N. framework</a> is a five-step onboarding model — Assure, Learn, Initiate, Guide, Nurture — for taking a new subscriber from signup to habitual use.'),
    ("How do you calculate LTV:CAC for a subscription business?", 'Using the <a href="frameworks/ltv-cac-investment.html">LTV:CAC Investment Framework</a>: LTV is estimated billable months multiplied by monthly margin, and CAC is the incremental cost per paid start (not trial starts).'),
    ("Why does retention matter more than acquisition in subscription growth?", 'Per the <a href="frameworks/growth-principles.html">10 Growth Principles</a>, pouring more users into a leaky funnel wastes acquisition spend. Fixing retention first strengthens unit economics and makes every later acquisition dollar more effective &mdash; see <a href="frameworks/retention-engine.html">The Retention Engine</a>.'),
    ("Should a growth team buy or build AI capability first?", 'Per the <a href="frameworks/ai-maturity-curve.html">AI Maturity Curve</a>, buy before you build: fully exploit AI features already inside existing ad, email, and analytics platforms before investing in custom-built models.'),
]

faq_schema_items = ",\n".join(
    f'''    {{
      "@type": "Question",
      "name": {json.dumps(q)},
      "acceptedAnswer": {{"@type": "Answer", "text": {json.dumps(re.sub('<[^<]+?>', '', a))}}}
    }}''' for q, a in faqs
)
faq_schema = f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
{faq_schema_items}
  ]
}}
</script>'''

faq_items_html = "\n".join(
    f'''  <div class="faq-item">
    <h3>{q}</h3>
    <p>{a}</p>
  </div>''' for q, a in faqs
)

faq_body = f'''  <h1>Frequently Asked Questions</h1>
  <p class="subtitle">Growth frameworks, the book, and {AUTHOR}</p>
{faq_items_html}
'''
write("faq.html", page(
    title=f"FAQ | Growth Frameworks by {AUTHOR}",
    description=f"Frequently asked questions about {AUTHOR}'s growth frameworks and the book Scaling Subscriptions.",
    body_html=faq_body,
    depth_prefix="",
    active="FAQ",
    extra_schema=faq_schema,
    slug="faq.html",
))

# ---------------------------------------------------------------------------
# BOOK PAGE
# ---------------------------------------------------------------------------

book_body = f'''  <h1>{BOOK}</h1>
  <p class="subtitle">By {AUTHOR}</p>

  <div class="answer">
    <strong>{BOOK}</strong> is a practitioner's playbook for building sustainable subscription growth through
    systems and repeatable frameworks, not hacks. It is organized as six independent playbooks covering the
    growth operating system, acquisition, retention, cross-funnel optimization, team structure, and adapting for
    B2B, free/ad-supported models, and AI.
  </div>

  <h2>Who is this book for?</h2>
  <p>Founders, marketers, and operators building subscription growth engines &mdash; particularly early-stage
  teams with limited resources, tech nonprofits, and growth practitioners at the start of their journey who want
  to build growth systems correctly from the start.</p>

  <h2>What are the six playbooks?</h2>
  <ol>
    <li>The Growth Operating System &mdash; principles, the 5-Step Growth Process, and the growth toolkit</li>
    <li>The Acquisition Engine &mdash; finding, testing, and optimizing channels; investment frameworks</li>
    <li>The Retention Machine &mdash; the Retention Engine, onboarding, cancel flows, winback</li>
    <li>The Cross-Funnel Optimization Toolkit &mdash; the Messaging Matrix, incentives, personalized offers</li>
    <li>The Team &amp; Capabilities Blueprint &mdash; growth org design and growth science</li>
    <li>The Future-Proofing Guide &mdash; B2C vs. B2B, paid vs. free models, and using AI to accelerate growth</li>
  </ol>

  <h2>Where can I get the book?</h2>
  <p>A complimentary digital edition is available at <a href="{BOOK_URL}">{BOOK_URL}</a>.</p>

  <h2>Explore the frameworks</h2>
  <p>Every major framework from the book is documented in full on this site &mdash; start with the
  <a href="glossary.html">Growth Frameworks Glossary</a>.</p>
'''
write("book.html", page(
    title=f"The Book | {BOOK}",
    description=f"{BOOK}, by {AUTHOR} — a practitioner's playbook for sustainable subscription growth.",
    body_html=book_body,
    depth_prefix="",
    active="The Book",
    slug="book.html",
))

# ---------------------------------------------------------------------------
# INDEX PAGE
# ---------------------------------------------------------------------------

cards = "\n".join(
    f'''    <a class="card" href="frameworks/{slug}.html">
      <div class="card-title">{title}</div>
      <div class="card-desc">{card_desc}</div>
    </a>''' for slug, title, _desc, card_desc in frameworks
)

index_body = f'''  <h1>Growth Frameworks</h1>
  <p class="subtitle">A reference library of subscription growth frameworks, by {AUTHOR}</p>

  <div class="answer">
    This site documents the growth frameworks developed by {AUTHOR} across leadership roles at Yelp, YouTube,
    and Netflix, and published in <a href="book.html">{BOOK}</a>. Start with the
    <a href="glossary.html">glossary</a> for a complete list of definitions, or browse individual frameworks below.
  </div>

  <h2>Frameworks</h2>
  <div class="card-grid">
{cards}
  </div>

  <h2>More</h2>
  <ul>
    <li><a href="glossary.html">Growth Frameworks Glossary</a> &mdash; every definition in one place</li>
    <li><a href="faq.html">FAQ</a></li>
    <li><a href="book.html">About the book</a></li>
  </ul>
'''
write("index.html", page(
    title=f"Growth Frameworks | {AUTHOR}",
    description=f"A reference library of subscription growth frameworks developed by {AUTHOR}, author of {BOOK}.",
    body_html=index_body,
    depth_prefix="",
    active="Home",
    slug="index.html",
))

# ---------------------------------------------------------------------------
# SITEMAP.XML  (kept in sync automatically with the page list above)
# ---------------------------------------------------------------------------

import datetime
today = datetime.date.today().isoformat()

static_pages = ["index.html", "glossary.html", "faq.html", "book.html"]
framework_pages = [f"frameworks/{slug}.html" for slug, *_ in frameworks]
all_pages = static_pages + framework_pages

url_entries = "\n".join(
    f'''  <url>
    <loc>{SITE_URL}/{p}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{"1.0" if p == "index.html" else ("0.9" if p == "glossary.html" else "0.7")}</priority>
  </url>''' for p in all_pages
)

sitemap = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{url_entries}
</urlset>
'''
write("sitemap.xml", sitemap)

# robots.txt -- explicitly allow AI/answer-engine crawlers, point at the sitemap
robots = f'''User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
'''
write("robots.txt", robots)

print("\\nSite build complete.")

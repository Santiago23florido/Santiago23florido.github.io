# -*- coding: utf-8 -*-
"""Genera las cuatro paginas del sitio a partir de una cabecera y un pie comunes."""
import io, os

ROOT = os.path.dirname(os.path.abspath(__file__))

HEAD = """<!doctype html>
<html lang="en" data-theme="">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<meta name="author" content="Santiago Florido Gómez" />
<link rel="canonical" href="https://santiago23florido.github.io{canon}" />
<meta property="og:type" content="website" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:url" content="https://santiago23florido.github.io{canon}" />
<meta name="twitter:card" content="summary" />
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>&#129470;</text></svg>" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/style.css" />
<script>
  try {{ var t = localStorage.getItem("theme"); if (t) document.documentElement.setAttribute("data-theme", t); }} catch (e) {{}}
</script>
</head>
<body>

<nav>
  <div class="wrap">
    <a class="brand" href="/">Santiago Florido Gómez</a>
    <a class="navlink{a_research}" href="/research/">Research</a>
    <a class="navlink{a_projects}" href="/projects/">Projects</a>
    <a class="navlink{a_experience}" href="/experience/">Experience</a>
    <a class="navlink" href="#contact">Contact</a>
    <button id="theme" type="button" aria-label="Switch between light and dark theme" title="Light / dark">&#9680;</button>
  </div>
</nav>
"""

FOOT = """
<section id="contact">
  <div class="wrap contact">
    <h2>Contact</h2>
    <p>
      I am looking for a <b>PhD in robot learning, neuromotor interfaces or dexterous
      manipulation</b>, and I am always glad to talk about any of this work — including
      reproducing or extending it.
    </p>
    <div class="links" style="margin-top:18px">
      <a href="mailto:santiago.florido@ensta-paris.fr">santiago.florido@ensta-paris.fr</a>
      <a href="https://github.com/Santiago23florido">github.com/Santiago23florido</a>
      <a href="https://www.linkedin.com/in/santiago-florido-gómez-722193232/">LinkedIn</a>
    </div>
  </div>
</section>

<div class="wrap">
  <footer>
    <span>Santiago Florido Gómez — Palaiseau, France</span>
    <span>Built with plain HTML and CSS. <a href="https://github.com/Santiago23florido/Santiago23florido.github.io">Source</a></span>
  </footer>
</div>

<script>
  (function () {
    var btn = document.getElementById("theme");
    if (!btn) return;
    function current() {
      var set = document.documentElement.getAttribute("data-theme");
      if (set === "dark" || set === "light") return set;
      return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
    }
    btn.addEventListener("click", function () {
      var next = current() === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch (e) {}
    });
  })();
</script>

</body>
</html>
"""

def page(path, canon, title, desc, body, active=""):
    head = HEAD.format(
        title=title, desc=desc, canon=canon,
        a_research=" active" if active == "research" else "",
        a_projects=" active" if active == "projects" else "",
        a_experience=" active" if active == "experience" else "",
    )
    full = head + body + FOOT
    out = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    io.open(out, "w", encoding="utf-8").write(full)
    print("escrito", path, len(full), "bytes")


# ===================================================================
# PORTADA
# ===================================================================
INDEX = """
<header class="hero">
  <div class="wrap">
    <h1>Santiago Florido Gómez</h1>
    <p class="role">
      MSc student, Cyber-Physical Systems — Institut Polytechnique de Paris<br />
      Engineering degree, AI track — ENSTA Paris
    </p>
    <p class="lede">
      I work on getting learned behaviour to <strong>survive a change of body</strong>: moving a
      skill from one humanoid to a very different one, and translating human motor intention
      into commands a robotic hand can act on.
    </p>
    <div class="links">
      <a href="https://github.com/Santiago23florido">GitHub</a>
      <a href="https://www.linkedin.com/in/santiago-florido-gómez-722193232/">LinkedIn</a>
      <a href="mailto:santiago.florido@ensta-paris.fr">Email</a>
    </div>
  </div>
</header>

<section class="about">
  <div class="wrap">
    <h2>About</h2>
    <p>
      I trained as a mechatronics engineer in Colombia, where I worked on the modelling and
      digital control of physical systems, and then moved to Paris to study computer science
      and artificial intelligence at ENSTA Paris, alongside a master's in Cyber-Physical
      Systems at Institut Polytechnique de Paris. In between I spent a summer at Inria on the
      question of when a neural network should grow rather than keep training.
    </p>
    <p>
      What I do now sits between reinforcement learning in simulation and the decoding of
      biological signals. Both halves ask the same question from opposite ends: what has to be
      true about a skill, or about an intention, for it to still mean something once the body
      carrying it out is not the one it came from. On one side that means moving a locomotion
      policy between humanoids of very different scale; on the other, reading individual motor
      units out of a muscle signal while the limb is moving, so that a hand can be driven from
      what a person intended rather than from what a sensor happened to measure.
    </p>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Where to go</h2>
    <div class="cards">
      <a class="card" href="/research/">
        <h3>Research</h3>
        <p>What I work on and why, and the papers that have come out of it.</p>
        <span class="enter">Enter &rarr;</span>
      </a>
      <a class="card" href="/projects/">
        <h3>Projects</h3>
        <p>The code, the results it actually produced, and the limits of each one.</p>
        <span class="enter">Enter &rarr;</span>
      </a>
      <a class="card" href="/experience/">
        <h3>Experience</h3>
        <p>Positions, education, technical skills and languages.</p>
        <span class="enter">Enter &rarr;</span>
      </a>
    </div>
  </div>
</section>
"""

# ===================================================================
# RESEARCH
# ===================================================================
RESEARCH = """
<header class="pagehead">
  <div class="wrap">
    <a class="back" href="/">&larr; Santiago Florido Gómez</a>
    <h1>Research</h1>
    <p>What I work on, and the papers that have come out of it.</p>
  </div>
</header>

<section>
  <div class="wrap">
    <h2>Interests</h2>
    <div class="interests">
      <div class="interest">
        <h3>Cross-embodiment transfer</h3>
        <p>Moving a learned locomotion skill between humanoids of very different scale, in
        simulation. The interesting part is not the policy but the interface: what a skill has
        to be expressed in so that a body it was never trained on can execute it.</p>
      </div>
      <div class="interest">
        <h3>Neuromotor interfaces</h3>
        <p>Decoding individual motor units from high-density surface EMG while the limb is
        moving — which is exactly when existing methods lose track of them, and exactly when an
        interface has to stay usable.</p>
      </div>
      <div class="interest">
        <h3>Dexterous manipulation</h3>
        <p>Musculoskeletal and robotic hands, teleoperation, and the context a muscle signal
        cannot carry on its own: two different intentions can produce almost the same
        activation, and what separates them lies in the situation.</p>
      </div>
      <div class="interest">
        <h3>Safe and efficient learning</h3>
        <p>Constrained MDPs where a safety budget is stated in units someone can argue with,
        physics-structured dynamics models, and networks that add capacity only once they can
        certify they need it.</p>
      </div>
    </div>
  </div>
</section>

<section id="publications">
  <div class="wrap">
    <h2>Publications</h2>

    <div class="pub">
      <div class="year">2026</div>
      <div>
        <h3>CAGE-NAS: Certified Functional Descent for Efficient Model Growth</h3>
        <p class="authors"><em>Santiago Florido Gómez</em>, Stéphane Rivaud</p>
        <p class="venue"><b>AXIOM workshop at NeurIPS 2026</b> — accepted</p>
        <p style="font-size:14.5px;color:var(--text-soft);margin:0 0 8px">
          Uses functional-gradient approximations in the tangent space of the network to certify
          when a model should grow rather than keep training parametrically.
        </p>
        <p class="meta"><a href="https://github.com/Santiago23florido/functional-gradient-growth">Code</a></p>
      </div>
    </div>

    <div class="pub">
      <div class="year">2025</div>
      <div>
        <h3>Low-order dynamic modeling and control of a neonatal incubator</h3>
        <p class="authors"><em>Santiago Florido Gómez</em>, José David Gómez Bedoya, Tatiana Manrique, Róbinson A. Torres</p>
        <p class="venue"><b>2025 IEEE 7th Colombian Conference on Automatic Control (CCAC)</b></p>
        <p style="font-size:14.5px;color:var(--text-soft);margin:0 0 8px">
          A thermodynamic model of a commercial incubator reduced to a control-friendly low-order
          form by system identification, with discrete-time PID and incremental RST controllers
          that outperform the stock controller.
        </p>
        <p class="meta">
          <a href="https://ieeexplore.ieee.org/document/11259151">IEEE Xplore</a>
          <a href="https://github.com/Santiago23florido/Neonatal-Incubator-Dynamic-Model-and-Control">Code</a>
        </p>
      </div>
    </div>

    <p class="backtop"><a href="/projects/">The projects behind this work &rarr;</a></p>
  </div>
</section>
"""

# ===================================================================
# PROJECTS
# ===================================================================
PROJECTS = """
<header class="pagehead">
  <div class="wrap">
    <a class="back" href="/">&larr; Santiago Florido Gómez</a>
    <h1>Projects</h1>
    <p>Each one states the result it actually produced and the limits of the evidence behind
    it — what is simulation, what data is synthetic, and what has not been built yet.</p>
  </div>
</header>

<section>
  <div class="wrap">

    <article class="project">
      <h3><a href="https://github.com/Santiago23florido/lHumanoid-Soccer-Isaac-Lab">Cross-Embodiment Humanoid Skill Transfer</a></h3>
      <p class="sub">Isaac Lab · 2026–present</p>
      <p>
        A locomotion skill learned on a <b>Unitree G1</b> runs <b>zero-shot</b> on a <b>NAO</b> that
        never trained on it — nine times lighter and 2.3 times shorter. The skill crosses as a
        <i>contract</i> rather than as joint angles: the short future of a 27-number state describing
        what the body does, made dimensionless with its own leg length, mass and gravity.
      </p>
      <p>
        Each skill's generator is trained once by flow matching on the source robot's rollouts;
        each body's estimator and tracker are trained once on procedurally generated plans and never
        see a transferred skill. So <b>N skills on M bodies cost N + M trainings instead of N × M</b>.
      </p>
      <div class="result">
        <p><b>192 of 192 episodes complete without a fall</b> per body and skill, at 1.00–1.14× the
        teacher's speed. On the NAO the zero-shot tracker stays closer to the teacher's gait
        (0.141–0.185 deviation) than a tracker trained on the skill itself (0.346–0.674) or
        joint-angle imitation (0.195–0.307). A task held out of every generator and tracker
        still runs: 288/288 on the NAO with cross-fitted plans.</p>
        <p class="caveat">All results are in simulation — no physical robot has walked with this.
        One source body and one target body, not arbitrary morphologies.</p>
      </div>
      <div class="tags">
        <span>Isaac Lab</span><span>Isaac Sim</span><span>PyTorch</span>
        <span>PPO (rsl_rl)</span><span>Flow Matching</span><span>Dimensional Analysis</span>
      </div>
    </article>

    <article class="project">
      <h3><a href="https://github.com/Santiago23florido/Musculoskeletal-Hand-Simulation">Musculoskeletal Hand Control from Motor Units</a></h3>
      <p class="sub">MuJoCo / MyoSuite · 2026–present</p>
      <p>
        Decoding <b>individual motor units</b> from high-density surface EMG in order to drive a
        simulated musculoskeletal hand (MyoSuite's MyoHand). The open problem: decomposition methods
        lose track of motor units exactly when the limb moves quickly — which is precisely when an
        interface has to remain usable.
      </p>
      <p>
        Building on the published adaptive method of Mendez Guerra, Barsakcioglu and Farina (2024),
        I added a <b>closed-loop context head</b> that decides which detected peaks are true
        discharges and feeds those decisions back into the adaptation.
      </p>
      <div class="result">
        <p>On a <b>held-out subject, evaluated once with every component frozen</b>: it recovers
        <b>87.4%</b> of discharges where the original method recovers <b>76.9%</b>
        (+10.5, 95% cluster-bootstrap [7.6, 14.0]), and <b>78.6% against 60.5%</b> during the
        fastest ramps. Units tracked at ≥90% agreement rise from 48.6% to 68.1%, with precision
        and recall improving together.</p>
        <p class="caveat">Ongoing research. The recordings are simulated HD-sEMG, which is why the
        true discharges are known and every decoded spike can be scored. The hand is not yet driven
        by the decoded motor units — that is the next stage of the project.</p>
      </div>
      <div class="tags">
        <span>MuJoCo</span><span>MyoSuite</span><span>PyTorch</span>
        <span>HD-sEMG</span><span>Attention</span><span>Signal Processing</span>
      </div>
    </article>

    <article class="project">
      <h3><a href="https://github.com/Santiago23florido/safe-autonomous-catheter-navigation">Safe Autonomous Catheter Navigation</a></h3>
      <p class="sub">Isaac Lab · 2026–present</p>
      <p>
        A physics-based endovascular navigation research environment: an <b>81-body, 80-DOF flexible
        catheter</b> advanced through vascular geometry with contact-force sensing. Wall-contact force
        is treated as a <b>constraint rather than another weighted term in the reward</b>, so the budget
        is stated in units a clinician can argue with instead of being hidden inside a tuned penalty
        weight. The cost is emitted on a channel structurally separate from the reward.
      </p>
      <div class="result">
        <p class="caveat">Phase 1 — environment construction. There is no reinforcement learning yet:
        <code>_get_rewards()</code> returns zeros by construction, and a test enforces that separation.</p>
      </div>
      <div class="tags">
        <span>Isaac Lab</span><span>Isaac Sim</span><span>Python</span>
        <span>PyTorch</span><span>Safe RL / CMDPs</span>
      </div>
    </article>

    <article class="project">
      <h3><a href="https://github.com/Santiago23florido/functional-gradient-growth">CAGE-NAS — Certified Functional Descent</a></h3>
      <p class="sub">Inria Saclay, équipe TAU · 2026</p>
      <p>
        Uses functional-gradient approximations in the <b>tangent space of the network</b> to certify
        when to keep training parametrically and when to perform a function-preserving expansion,
        so capacity grows only once the current representation can no longer certify a functional
        descent step.
      </p>
      <div class="result">
        <p>Grown architectures land <b>above the 99.8th percentile of 76,646 exhaustively enumerated
        alternatives</b>, with 0.9575 ± 0.0038 test accuracy over four seeds on the principal
        synthetic benchmark.</p>
      </div>
      <div class="tags">
        <span>PyTorch</span><span>Neural Architecture Growth</span>
        <span>Functional Gradients</span><span>Optimization</span>
      </div>
    </article>

    <details class="more">
      <summary>Earlier projects</summary>
      <ul>
        <li><b><a href="https://github.com/Santiago23florido/Deep-Drive-APEX">Deep-Drive-APEX</a></b> —
          Autonomous navigation on a real robotic vehicle with ROS 2: LiDAR obstacle detection,
          path planning and trajectory execution, with a Gazebo real-to-sim framework for validation.</li>
        <li><b><a href="https://github.com/Santiago23florido/gromo">gromo</a></b> —
          Contributions to the growing-networks module for PyTorch (Inria, équipe TAU).</li>
        <li><b><a href="https://github.com/Santiago23florido/Neonatal-incubator-with-response-to-apnea-episodes">Neonatal incubator with apnea response</a></b> —
          End-to-end central-apnea detection from EMG-derived respiratory signals using CNN–LSTM
          temporal models, with closed-loop corrective stimulation.</li>
        <li><b><a href="https://github.com/Santiago23florido/Neonatal-Incubator-Dynamic-Model-and-Control">Neonatal incubator: model &amp; control</a></b> —
          Thermodynamic modelling, system identification and digital PID / incremental RST control.
          Published at IEEE CCAC 2025.</li>
        <li><b><a href="https://github.com/Santiago23florido/Incremental-RST-control-for-DC-motor-with-encoder-design">Incremental RST control of a DC motor</a></b> —
          System identification and digital control on real hardware, with encoder design.</li>
        <li><b><a href="https://github.com/Santiago23florido/Robust-Image-Matching-with-Local-Features">Robust image matching</a></b> and
          <b><a href="https://github.com/Santiago23florido/Vision_LocalFeatures_BayesianClassification_KMeans">local features, Bayesian classification &amp; K-means</a></b> —
          Classical computer-vision pipelines.</li>
        <li><b><a href="https://github.com/Santiago23florido/Scara-web-controlled-robotic-arm">SCARA web-controlled robotic arm</a></b> —
          Kinematics, embedded control and a web interface for a physical SCARA arm.</li>
      </ul>
    </details>

    <p class="backtop"><a href="/research/">&larr; Why I work on this</a></p>
  </div>
</section>
"""

# ===================================================================
# EXPERIENCE
# ===================================================================
EXPERIENCE = """
<header class="pagehead">
  <div class="wrap">
    <a class="back" href="/">&larr; Santiago Florido Gómez</a>
    <h1>Experience</h1>
    <p>Positions, education, technical skills and languages.</p>
  </div>
</header>

<section>
  <div class="wrap">
    <h2>Positions</h2>

    <div class="entry">
      <div class="top">
        <span class="what">Research Intern (PRe) — Neural architecture growth</span>
        <span class="when">May – Aug 2026</span>
      </div>
      <div class="where">équipe TAU / LISN, Inria Saclay — Université Paris-Saclay</div>
      <p>
        Certified functional descent for frugal learning: using functional-gradient information in
        the tangent space of a network to decide when it should grow rather than keep training.
        Led to a first-author paper accepted at the AXIOM workshop, NeurIPS 2026.
      </p>
    </div>

    <div class="entry">
      <div class="top">
        <span class="what">Data &amp; Machine Learning Analyst</span>
        <span class="when">Dec 2024 – Sep 2025</span>
      </div>
      <div class="where">Celerix — Medellín, Colombia</div>
      <p>
        Demand-forecasting and pricing models, automated ETL pipelines, embedding-based NLP
        components, and Power BI / Tableau dashboards for operational decision-making.
      </p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Education</h2>

    <div class="entry">
      <div class="top">
        <span class="what">M2 — Cyber-Physical Systems</span>
        <span class="when">2026 – 2027</span>
      </div>
      <div class="where">Institut Polytechnique de Paris</div>
    </div>

    <div class="entry">
      <div class="top">
        <span class="what">Diplôme d'Ingénieur — Computer Science, AI specialization</span>
        <span class="when">2025 – present</span>
      </div>
      <div class="where">ENSTA Paris — Institut Polytechnique de Paris</div>
    </div>

    <div class="entry">
      <div class="top">
        <span class="what">B.Sc. Mechatronics Engineering</span>
        <span class="when">2021 – 2026</span>
      </div>
      <div class="where">Universidad EIA — Envigado, Colombia</div>
      <p>
        Graduated with the highest cumulative average of the undergraduate class (4.64 / 5.00).
        Honorary Mention for outstanding academic performance; University Honor Roll.
      </p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Technical skills</h2>
    <div class="skills">
      <div class="skillgroup">
        <h3>Robot learning &amp; simulation</h3>
        <ul>
          <li>Isaac Lab, Isaac Sim, PhysX</li>
          <li>MuJoCo, MyoSuite</li>
          <li>PPO (rsl_rl), constrained MDPs</li>
          <li>Flow matching, imitation</li>
          <li>ROS 2, Gazebo, Nav2</li>
        </ul>
      </div>
      <div class="skillgroup">
        <h3>Machine learning</h3>
        <ul>
          <li>PyTorch, TensorFlow, scikit-learn</li>
          <li>CNNs, LSTMs, attention</li>
          <li>Statistical learning</li>
          <li>Neural architecture growth</li>
          <li>NLP &amp; semantic embeddings</li>
        </ul>
      </div>
      <div class="skillgroup">
        <h3>Signals &amp; control</h3>
        <ul>
          <li>HD-sEMG decomposition</li>
          <li>EMG / ECG signal processing</li>
          <li>System identification</li>
          <li>PID / RST digital control</li>
          <li>MATLAB, Simulink</li>
        </ul>
      </div>
      <div class="skillgroup">
        <h3>Software &amp; systems</h3>
        <ul>
          <li>Python, C++, C, SQL, Git</li>
          <li>Docker, MPI, parallel computing</li>
          <li>NumPy, SciPy, Pandas</li>
          <li>Embedded: Arduino, ESP32</li>
          <li>Graph, string &amp; geometric algorithms</li>
        </ul>
      </div>
    </div>
    <p style="margin-top:22px;color:var(--text-soft);font-size:14.5px">
      <b>Languages:</b> Spanish (native) · English (C1) · French (B2)
    </p>
  </div>
</section>
"""

page("index.html", "/", "Santiago Florido Gómez",
     "Robot learning, cross-embodiment transfer and neuromotor interfaces. MSc student in Cyber-Physical Systems at Institut Polytechnique de Paris.",
     INDEX)
page("research/index.html", "/research/", "Research — Santiago Florido Gómez",
     "Cross-embodiment transfer, neuromotor interfaces, dexterous manipulation, and safe and efficient learning. Publications.",
     RESEARCH, active="research")
page("projects/index.html", "/projects/", "Projects — Santiago Florido Gómez",
     "Cross-embodiment humanoid skill transfer, motor-unit decoding for a musculoskeletal hand, safe catheter navigation, and certified network growth.",
     PROJECTS, active="projects")
page("experience/index.html", "/experience/", "Experience — Santiago Florido Gómez",
     "Positions, education, technical skills and languages.",
     EXPERIENCE, active="experience")

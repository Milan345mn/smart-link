import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette (Modern Tech / Dark Navy & Indigo)
    BG_DARK = RGBColor(15, 23, 42)      # Slate 900
    CARD_BG = RGBColor(30, 41, 59)      # Slate 800
    TEXT_MAIN = RGBColor(248, 250, 252) # White/Slate 50
    TEXT_MUTED = RGBColor(148, 163, 184)# Slate 400
    ACCENT_CYAN = RGBColor(6, 182, 212) # Cyan 500
    ACCENT_GREEN = RGBColor(16, 185, 129)# Emerald 500
    ACCENT_BLUE = RGBColor(59, 130, 246) # Blue 500

    def add_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.fill.background()
        return bg

    def add_header(slide, category, title):
        add_bg(slide)
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.4))
        tf_c = cat_box.text_frame
        tf_c.word_wrap = True
        p_c = tf_c.paragraphs[0]
        p_c.text = category.upper()
        p_c.font.size = Pt(11)
        p_c.font.bold = True
        p_c.font.color.rgb = ACCENT_CYAN
        p_c.font.name = "Segoe UI"

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.7))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(24)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_MAIN
        p_t.font.name = "Segoe UI"

    # ==========================================================
    # SLIDE 1: Title Slide
    # ==========================================================
    slide1 = prs.slides.add_slide(blank_layout)
    add_bg(slide1)

    tbox = slide1.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(11.0), Inches(2.2))
    tf = tbox.text_frame
    tf.word_wrap = True
    p1 = tf.paragraphs[0]
    p1.text = "Automated CI/CD Pipeline Implementation"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_MAIN
    p1.font.name = "Segoe UI"

    p2 = tf.add_paragraph()
    p2.text = "End-to-End DevOps Automation for a React Web Application with GitHub Actions"
    p2.font.size = Pt(18)
    p2.font.color.rgb = ACCENT_CYAN
    p2.font.name = "Segoe UI"
    p2.space_before = Pt(14)

    # Info Card
    card = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(4.5), Inches(11.0), Inches(1.8))
    card.fill.solid()
    card.fill.fore_color.rgb = CARD_BG
    card.line.color.rgb = ACCENT_BLUE

    itbox = slide1.shapes.add_textbox(Inches(1.5), Inches(4.7), Inches(10.4), Inches(1.4))
    itf = itbox.text_frame
    
    bullets = [
        ("Student & Developer: ", "Milan (@Milan345mn)"),
        ("Live Web Application: ", "https://milan345mn.github.io/smart-link/"),
        ("GitHub Repository: ", "https://github.com/Milan345mn/smart-link"),
        ("Core Technology: ", "React 18 • Vite • Vitest • GitHub Actions • GitHub Pages")
    ]
    for i, (label, val) in enumerate(bullets):
        p = itf.paragraphs[0] if i == 0 else itf.add_paragraph()
        run1 = p.add_run()
        run1.text = label
        run1.font.bold = True
        run1.font.size = Pt(13)
        run1.font.color.rgb = TEXT_MUTED
        run1.font.name = "Segoe UI"
        run2 = p.add_run()
        run2.text = val
        run2.font.bold = True
        run2.font.size = Pt(13)
        run2.font.color.rgb = ACCENT_GREEN if "https" in val else TEXT_MAIN
        run2.font.name = "Segoe UI"
        p.space_after = Pt(4)

    # ==========================================================
    # SLIDE 2: Project Objectives & Context
    # ==========================================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "1. Executive Summary", "Project Context & DevOps Objectives")

    cards_data_s2 = [
        ("The Challenge", "Select an existing public open-source project on GitHub, run it locally, and implement an industrial-grade CI/CD pipeline without human intervention.", ACCENT_CYAN),
        ("The Solution", "Chose 'react-calculator' (React 18 + Vite). Added Vitest unit testing, configured production base routing, and built an 8-stage GitHub Actions pipeline.", ACCENT_BLUE),
        ("The Result", "100% automated lifecycle: code push triggers test execution, builds production bundles, and publishes live to GitHub Pages in under 30 seconds.", ACCENT_GREEN)
    ]
    for idx, (title, desc, col) in enumerate(cards_data_s2):
        x = Inches(0.8 + idx * 3.9)
        c = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(3.6), Inches(4.8))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = col
        c.line.width = Pt(1.5)

        tb = slide2.shapes.add_textbox(x + Inches(0.25), Inches(2.1), Inches(3.1), Inches(4.2))
        tf_c = tb.text_frame
        tf_c.word_wrap = True
        p_t = tf_c.paragraphs[0]
        p_t.text = title
        p_t.font.bold = True
        p_t.font.size = Pt(18)
        p_t.font.color.rgb = col
        p_t.font.name = "Segoe UI"

        p_d = tf_c.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(14)
        p_d.font.color.rgb = TEXT_MAIN
        p_d.font.name = "Segoe UI"
        p_d.space_before = Pt(14)

    # ==========================================================
    # SLIDE 3: System Architecture & Stack
    # ==========================================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "2. System Architecture", "Technology Stack & Application Components")

    stack = [
        ("Frontend Application", "React 18.3 & Vite 6", "Single Page Application (SPA) with clean component architecture and reactive state hooks."),
        ("Testing Engine", "Vitest v5.0.5", "Native Vite testing framework executing in-memory unit tests in ~820ms."),
        ("Automation Platform", "GitHub Actions", "Hosted Ubuntu Linux runner executing automated CI jobs on push and PR triggers."),
        ("Deployment Target", "GitHub Pages (OIDC)", "Global CDN hosting static production assets with automatic SSL/HTTPS.")
    ]
    for idx, (layer, tech, detail) in enumerate(stack):
        y = Inches(1.8 + idx * 1.25)
        bar = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(11.7), Inches(1.05))
        bar.fill.solid()
        bar.fill.fore_color.rgb = CARD_BG
        bar.line.color.rgb = ACCENT_BLUE

        tb = slide3.shapes.add_textbox(Inches(1.1), y + Inches(0.12), Inches(11.1), Inches(0.8))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        r1 = p.add_run()
        r1.text = f"[{layer}]  "
        r1.font.bold = True
        r1.font.size = Pt(14)
        r1.font.color.rgb = ACCENT_CYAN
        r1.font.name = "Segoe UI"
        r2 = p.add_run()
        r2.text = f"{tech} — "
        r2.font.bold = True
        r2.font.size = Pt(14)
        r2.font.color.rgb = TEXT_MAIN
        r2.font.name = "Segoe UI"
        r3 = p.add_run()
        r3.text = detail
        r3.font.size = Pt(13)
        r3.font.color.rgb = TEXT_MUTED
        r3.font.name = "Segoe UI"

    # ==========================================================
    # SLIDE 4: The 8-Stage CI/CD Pipeline
    # ==========================================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_header(slide4, "3. Pipeline Design", "The 8 Stages of the GitHub Actions Workflow")

    stages = [
        ("1. Trigger", "Push to main/master, PRs, and manual workflow_dispatch."),
        ("2. Checkout", "actions/checkout@v4 clones full source tree."),
        ("3. Environment Setup", "actions/setup-node@v4 installs Node 20 LTS with npm cache."),
        ("4. Clean Install", "npm ci provides 100% deterministic dependency install."),
        ("5. Automated Testing", "npm test runs Vitest suite as a strict quality gate."),
        ("6. Production Build", "npm run build bundles minified JS/CSS into dist/."),
        ("7. Artifact Upload", "actions/upload-artifact@v4 saves build outputs for audit."),
        ("8. Cloud Deployment", "actions/deploy-pages@v4 pushes to GitHub Pages via OIDC.")
    ]
    for idx, (st_name, st_desc) in enumerate(stages):
        row = idx // 2
        col = idx % 2
        x = Inches(0.8 + col * 5.9)
        y = Inches(1.7 + row * 1.3)

        box = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.6), Inches(1.1))
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = ACCENT_CYAN if idx in [0, 4, 7] else ACCENT_BLUE

        tb = slide4.shapes.add_textbox(x + Inches(0.2), y + Inches(0.1), Inches(5.2), Inches(0.9))
        tf = tb.text_frame
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        p1.text = st_name
        p1.font.bold = True
        p1.font.size = Pt(14)
        p1.font.color.rgb = ACCENT_GREEN if idx in [4, 7] else ACCENT_CYAN
        p1.font.name = "Segoe UI"

        p2 = tf.add_paragraph()
        p2.text = st_desc
        p2.font.size = Pt(12)
        p2.font.color.rgb = TEXT_MUTED
        p2.font.name = "Segoe UI"
        p2.space_before = Pt(3)

    # ==========================================================
    # SLIDE 5: Automated Testing Quality Gate
    # ==========================================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_header(slide5, "4. Quality Assurance", "Automated Testing Suite (Vitest Quality Gate)")

    # Left Stats Card
    scard = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.8))
    scard.fill.solid()
    scard.fill.fore_color.rgb = CARD_BG
    scard.line.color.rgb = ACCENT_GREEN

    stb = slide5.shapes.add_textbox(Inches(1.0), Inches(2.1), Inches(3.2), Inches(4.2))
    stf = stb.text_frame
    stf.word_wrap = True
    sp1 = stf.paragraphs[0]
    sp1.text = "100% PASS RATE"
    sp1.font.bold = True
    sp1.font.size = Pt(22)
    sp1.font.color.rgb = ACCENT_GREEN
    sp1.font.name = "Segoe UI"

    sp2 = stf.add_paragraph()
    sp2.text = "• Total Tests: 9\n• Tests Passed: 9\n• Tests Failed: 0\n• Execution Time: 820ms\n• Framework: Vitest v5.0.5\n• Quality Gate: Strict Exit 0"
    sp2.font.size = Pt(14)
    sp2.font.color.rgb = TEXT_MAIN
    sp2.font.name = "Segoe UI"
    sp2.space_before = Pt(18)

    # Right Tests Table
    tests_summary = [
        ("Arithmetic Operations", "Tests 5+3=8, 15-7=8, 6*7=42, 20/4=5", "PASS"),
        ("Operator Precedence", "Tests BODMAS compliance: 2+3*4 = 14 and (2+3)*4 = 20", "PASS"),
        ("Floating Point Logic", "Tests 1.5 + 2.5 = 4 and 0.1 + 0.2 precision handling", "PASS"),
        ("Division by Zero", "Tests 10/0 returns 'Error' without crashing application", "PASS"),
        ("Syntax Error Guards", "Tests unclosed parentheses and double operators (5++)", "PASS"),
        ("Code Injection Defense", "Rejects malicious inputs (alert, process.exit, eval)", "PASS")
    ]
    for idx, (tname, tdesc, tstatus) in enumerate(tests_summary):
        y = Inches(1.8 + idx * 0.8)
        tbox = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.6), y, Inches(7.9), Inches(0.7))
        tbox.fill.solid()
        tbox.fill.fore_color.rgb = CARD_BG
        tbox.line.color.rgb = ACCENT_BLUE

        tb = slide5.shapes.add_textbox(Inches(4.8), y + Inches(0.08), Inches(7.5), Inches(0.55))
        tf = tb.text_frame
        p = tf.paragraphs[0]
        r1 = p.add_run()
        r1.text = f"{tname}: "
        r1.font.bold = True
        r1.font.size = Pt(13)
        r1.font.color.rgb = ACCENT_CYAN
        r1.font.name = "Segoe UI"
        r2 = p.add_run()
        r2.text = f"{tdesc}  "
        r2.font.size = Pt(12)
        r2.font.color.rgb = TEXT_MUTED
        r2.font.name = "Segoe UI"
        r3 = p.add_run()
        r3.text = f"[{tstatus}]"
        r3.font.bold = True
        r3.font.size = Pt(13)
        r3.font.color.rgb = ACCENT_GREEN
        r3.font.name = "Segoe UI"

    # ==========================================================
    # SLIDE 6: Continuous Deployment Verification
    # ==========================================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_header(slide6, "5. Verification", "Live Pipeline Execution & CD Demonstration")

    runs = [
        ("Run #1: Initial CI/CD & Deployment", "Commit 3552a05", "Duration: 35s", "Status: SUCCESS", "Pushed repository source code, Vitest test suite, and workflow file. Automated jobs installed dependencies, passed 9 unit tests, bundled assets, and initialized live GitHub Pages website."),
        ("Run #2: Continuous Deployment Verification", "Commit 60324d0", "Duration: 29s", "Status: SUCCESS", "Made code change to Frame.jsx header title ('React Calculator (CI/CD Verified)'). Pushed change to main branch. Pipeline automatically triggered, validated tests, and updated live website in 29 seconds.")
    ]
    for idx, (title, commit, dur, status, desc) in enumerate(runs):
        y = Inches(1.8 + idx * 2.5)
        card = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(11.7), Inches(2.2))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = ACCENT_GREEN
        card.line.width = Pt(1.5)

        tb = slide6.shapes.add_textbox(Inches(1.1), y + Inches(0.18), Inches(11.1), Inches(1.8))
        tf = tb.text_frame
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        r1 = p1.add_run()
        r1.text = f"{title}   "
        r1.font.bold = True
        r1.font.size = Pt(16)
        r1.font.color.rgb = TEXT_MAIN
        r1.font.name = "Segoe UI"
        r2 = p1.add_run()
        r2.text = f"[{commit} • {dur} • {status}]"
        r2.font.bold = True
        r2.font.size = Pt(14)
        r2.font.color.rgb = ACCENT_GREEN
        r2.font.name = "Segoe UI"

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(13)
        p2.font.color.rgb = TEXT_MUTED
        p2.font.name = "Segoe UI"
        p2.space_before = Pt(8)

    # ==========================================================
    # SLIDE 7: Key DevOps Lessons & Overcoming Challenges
    # ==========================================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_header(slide7, "6. Key Lessons", "DevOps Challenges Encountered & Senior Solutions")

    challenges = [
        ("Relative Path Routing for CDN", "Vite defaults to root-relative asset URLs ('/assets/...'). On GitHub Pages subpaths, this causes 404 white screens. Fixed by configuring base: './' in vite.config.js for 100% path portability."),
        ("Zero-Test Codebase Remediation", "The upstream GitHub project had no automated tests. Implemented Vitest, exported evaluateExpression, and authored 9 comprehensive unit tests to establish a true CI quality gate."),
        ("Secure Least-Privilege Permissions", "Avoided broad write permissions or long-lived static Personal Access Tokens. Scoped workflow strictly to contents: read, pages: write, and id-token: write using native GitHub OIDC."),
        ("Non-Destructive Local Workspace Safety", "Preserved user's existing work in E:\\ev by isolating the cloned project in E:\\ev\\react-calculator, adhering to senior DevOps safety principles.")
    ]
    for idx, (ch_title, ch_desc) in enumerate(challenges):
        row = idx // 2
        col = idx % 2
        x = Inches(0.8 + col * 5.9)
        y = Inches(1.8 + row * 2.5)

        c = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.6), Inches(2.2))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = ACCENT_BLUE

        tb = slide7.shapes.add_textbox(x + Inches(0.2), y + Inches(0.15), Inches(5.2), Inches(1.9))
        tf = tb.text_frame
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        p1.text = ch_title
        p1.font.bold = True
        p1.font.size = Pt(15)
        p1.font.color.rgb = ACCENT_CYAN
        p1.font.name = "Segoe UI"

        p2 = tf.add_paragraph()
        p2.text = ch_desc
        p2.font.size = Pt(12)
        p2.font.color.rgb = TEXT_MUTED
        p2.font.name = "Segoe UI"
        p2.space_before = Pt(6)

    # ==========================================================
    # SLIDE 8: Deliverables & Conclusion
    # ==========================================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_header(slide8, "7. Submission Summary", "Assignment Deliverables & Live Demonstration")

    docs = [
        ("PROJECT_DOCUMENTATION.md", "Architecture, component flow, dependency breakdown, and local instructions."),
        ("CI_CD_EXPLANATION.md", "Line-by-line workflow YAML breakdown, trigger events, and security architecture."),
        ("SETUP_AND_EXECUTION.md", "Step-by-step installation, test execution, build, and Git commands."),
        ("TESTING_REPORT.md", "Complete Vitest report, inputs/outputs matrix, and CI gate verification."),
        ("DEPLOYMENT_GUIDE.md", "GitHub Pages setup, live URL verification, and continuous deployment guide.")
    ]
    for idx, (doc_name, doc_desc) in enumerate(docs):
        y = Inches(1.8 + idx * 0.95)
        bar = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(11.7), Inches(0.82))
        bar.fill.solid()
        bar.fill.fore_color.rgb = CARD_BG
        bar.line.color.rgb = ACCENT_GREEN

        tb = slide8.shapes.add_textbox(Inches(1.1), y + Inches(0.12), Inches(11.1), Inches(0.6))
        tf = tb.text_frame
        p = tf.paragraphs[0]
        r1 = p.add_run()
        r1.text = f"📄 {doc_name}: "
        r1.font.bold = True
        r1.font.size = Pt(14)
        r1.font.color.rgb = ACCENT_CYAN
        r1.font.name = "Segoe UI"
        r2 = p.add_run()
        r2.text = doc_desc
        r2.font.size = Pt(13)
        r2.font.color.rgb = TEXT_MAIN
        r2.font.name = "Segoe UI"

    output_path = r"E:\ev\react-calculator\CICD_Pipeline_Project_Presentation.pptx"
    prs.save(output_path)
    print(f"Presentation saved successfully at: {output_path}")

if __name__ == "__main__":
    create_deck()

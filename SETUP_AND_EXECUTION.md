# 🛠️ Setup and Execution Guide: React Calculator

This guide walks you through setting up, running, testing, and pushing this React Calculator project to GitHub step by step.

---

## 1. Prerequisites Checklist

Before running or deploying the project, ensure you have the following installed on your local machine:

| Tool | Minimum Version | Recommended Version | Verification Command |
| :--- | :--- | :--- | :--- |
| **Git** | `v2.20+` | `v2.40+` | `git --version` |
| **Node.js** | `v18.0.0+` | `v20.x` or `v22.x` | `node --version` |
| **npm** | `v9.0.0+` | `v10.x` | `npm --version` |

---

## 2. Local Setup & Execution

### Step 1: Open the Project Directory
Open your terminal (PowerShell or Bash) and navigate to the project directory:
```powershell
cd E:\ev\react-calculator
```

### Step 2: Install Project Dependencies
Run npm to install all production and development dependencies:
```bash
npm install
```
*(This installs React, Vite, and Vitest according to `package.json`.)*

### Step 3: Run the Development Server
Launch the local development server with Hot Module Replacement (HMR):
```bash
npm run dev
```
Output:
```text
  VITE v6.4.1  ready in 640 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```
Open your web browser and navigate to `http://localhost:5173/` to interact with the calculator.

### Step 4: Run Automated Unit Tests
Verify all mathematical and functional logic:
```bash
npm test
```
Vitest will run and report:
```text
 ✓ src/components/Frame.test.js (9 tests)
 Test Files  1 passed (1)
      Tests  9 passed (9)
```

### Step 5: Test the Production Build
Generate optimized production bundles:
```bash
npm run build
```
Vite will compile files into the `dist/` directory.

### Step 6: Preview Production Build Locally
Verify the production build works as expected prior to cloud deployment:
```bash
npm run preview
```
Navigate to `http://localhost:4173/` to preview the production bundle.

---

## 3. Pushing to Your GitHub Account

Because this project was originally cloned from upstream (`swapnilgupta/react-calculator`), you need to push it to **your own** GitHub account so your GitHub Actions pipeline can run.

### Step 1: Create a New Repository on GitHub
1. Log into your GitHub account: [https://github.com](https://github.com).
2. Click the **+** (plus icon) in the top right corner $\to$ Select **New repository**.
3. Name your repository (e.g. `react-calculator` or `react-calculator-cicd`).
4. Keep it **Public** (required for free GitHub Pages deployment).
5. **Do NOT** initialize with a README, .gitignore, or license (we already have them).
6. Click **Create repository**.
7. Copy your repository's HTTPS URL:
   `https://github.com/<YOUR_GITHUB_USERNAME>/react-calculator.git`

### Step 2: Configure Git User Info (If Not Set)
If you haven't configured your Git credentials on your machine, run:
```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

### Step 3: Update Git Remote URL
Point your local repository to your newly created GitHub repository:
```bash
# Check current remote (points to original upstream author)
git remote -v

# Change remote origin to YOUR repository
git remote set-url origin https://github.com/<YOUR_GITHUB_USERNAME>/react-calculator.git

# Verify the updated remote URL
git remote -v
```

### Step 4: Ensure Primary Branch is `main` (or `master`)
```bash
git branch -M main
```

### Step 5: Stage, Commit, and Push Your Files
```bash
# Stage all updated files, tests, documentation, and the CI/CD workflow
git add .

# Commit with a descriptive message
git commit -m "feat: implement automated CI/CD pipeline with Vitest and GitHub Actions"

# Push to your GitHub repository
git push -u origin main
```

---

## 4. Troubleshooting Common Issues

### Issue 1: Port 5173 is already in use
* **Cause**: Another service or previous Vite process is running.
* **Fix**: Run `npm run dev -- --port 5174` or kill the existing process.

### Issue 2: Git push authentication failed
* **Cause**: GitHub no longer accepts account passwords via HTTPS; it requires a Personal Access Token (PAT) or GitHub CLI authentication.
* **Fix**: Generate a token at **GitHub $\to$ Settings $\to$ Developer Settings $\to$ Personal Access Tokens (Classic)** with `repo` and `workflow` scopes, and use it as your password when prompted.

### Issue 3: Tests fail locally
* **Cause**: Node.js version incompatibility or missing packages.
* **Fix**: Ensure Node.js is $\ge 18$. Run `npm ci` to reset `node_modules` cleanly.

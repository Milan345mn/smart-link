# 🔄 CI/CD Pipeline Architecture & In-Depth YAML Explanation

## 1. What is CI/CD?
* **Continuous Integration (CI)** is the automated practice of integrating code changes from multiple developers into a single software project. As soon as code is pushed, an automated system checks out the repository, installs dependencies, runs automated unit tests, and verifies that the production build succeeds without errors.
* **Continuous Deployment (CD)** is the automated delivery pipeline that takes tested build artifacts and automatically releases them to a hosting environment (such as GitHub Pages) without human intervention.

---

## 2. CI/CD Architecture Flow
The following diagram illustrates the complete lifecycle of a code change in this repository:

```text
[Developer / Local Machine]
           │
           │  git push (main or master)
           ▼
[GitHub Repository Event Trigger]
           │
 ┌─────────┴──────────────────────────────┐
 │ JOB 1: Build & Test (Runner: ubuntu-latest)
 │                                        │
 │ 1. actions/checkout@v4                 │
 │ 2. actions/setup-node@v4 (Node 20)     │
 │ 3. npm ci (Deterministic dependency install)
 │ 4. npm test (Vitest: 9 unit tests)     │
 │ 5. npm run build (Vite production bundle)
 │ 6. actions/upload-artifact@v4          │
 │ 7. actions/upload-pages-artifact@v3    │
 └─────────┬──────────────────────────────┘
           │
           │ (On Push to main/master ONLY, PRs stop here)
           ▼
 ┌────────────────────────────────────────┐
 │ JOB 2: Deploy to GitHub Pages          │
 │                                        │
 │ 1. Environment: github-pages           │
 │ 2. actions/deploy-pages@v4             │
 └─────────┬──────────────────────────────┘
           │
           ▼
[Live Production Website on GitHub Pages]
```

---

## 3. Line-by-Line Explanation of `.github/workflows/ci-cd.yml`

Below is an exhaustive explanation of every directive in the pipeline configuration file:

### Lines 1–11: Pipeline Name & Trigger Configuration
```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]
  workflow_dispatch:
```
* **`name: CI/CD Pipeline`**: The descriptive title that appears in GitHub's **Actions** tab.
* **`on:`**: Defines the triggers that cause this workflow to start running.
  * **`push: branches: [ main, master ]`**: Automatically starts the pipeline whenever new commits are pushed to the primary branches (`main` or `master`).
  * **`pull_request: branches: [ main, master ]`**: Runs the CI checks whenever someone opens a pull request targeting the primary branch. This prevents broken code from being merged.
  * **`workflow_dispatch:`**: Adds a "Run workflow" button in the GitHub Actions web interface, enabling manual on-demand execution.

---

### Lines 13–23: Permissions & Concurrency Control
```yaml
permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: 'pages'
  cancel-in-progress: false
```
* **`permissions:`**: Implements the security principle of **least privilege**:
  * `contents: read`: Allows the workflow to read and download the repository source code.
  * `pages: write`: Grants permission to upload and publish content to GitHub Pages.
  * `id-token: write`: Authorizes OpenID Connect (OIDC) token generation for secure authentication without hardcoding static personal access tokens.
* **`concurrency:`**: Ensures only one deployment task runs at a time for the `pages` group, preventing race conditions if multiple pushes happen in rapid succession.

---

### Lines 25–46: Job 1 — Build & Test (Continuous Integration)
```yaml
jobs:
  build-and-test:
    name: Build & Test
    runs-on: ubuntu-latest
```
* **`jobs:`**: Defines the distinct containerized workflows.
* **`build-and-test:`**: The identifier for the CI job.
* **`runs-on: ubuntu-latest`**: Runs the job inside a fresh, clean, hosted Linux (Ubuntu) virtual environment provided by GitHub.

```yaml
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
```
* Clones the repository code into the runner's workspace using the official, actively maintained v4 action.

```yaml
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'
```
* Installs Node.js version 20 LTS.
* `cache: 'npm'`: Automatically caches downloaded npm packages between workflow runs based on `package-lock.json`, speeding up pipeline runs by 50–70%.

```yaml
      - name: Install dependencies
        run: npm ci
```
* `npm ci` (Clean Install): Installs dependencies strictly matching `package-lock.json`. Unlike `npm install`, it never alters the lockfile, ensuring 100% reproducible builds across all environments.

```yaml
      - name: Run automated tests
        run: npm test
```
* Executes the Vitest automated test suite (`vitest run`).
* If any test fails, the step exits with code 1, stopping the pipeline immediately and preventing faulty code from building or deploying.

```yaml
      - name: Build production application
        run: npm run build
```
* Bundles all React components, CSS, and HTML into optimized, minified static files located in the `dist/` directory.

---

### Lines 48–65: Preserving Build Artifacts
```yaml
      - name: Upload production build artifact
        uses: actions/upload-artifact@v4
        with:
          name: react-calculator-dist
          path: dist
          retention-days: 14
```
* Uses `actions/upload-artifact@v4` to store the raw compiled `dist/` folder in GitHub. Team members can download and inspect the compiled assets directly from the Actions run summary.

```yaml
      - name: Upload GitHub Pages artifact
        if: github.ref == 'refs/heads/main' || github.ref == 'refs/heads/master'
        uses: actions/upload-pages-artifact@v3
        with:
          path: dist
```
* Packages the `dist/` folder into a format required by GitHub Pages deployment services.
* Guarded by `if:` to only package when on `main` or `master`.

---

### Lines 67–85: Job 2 — Deploy to GitHub Pages (Continuous Deployment)
```yaml
  deploy:
    name: Deploy to GitHub Pages
    needs: build-and-test
    if: (github.ref == 'refs/heads/main' || github.ref == 'refs/heads/master') && github.event_name != 'pull_request'
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
```
* **`needs: build-and-test`**: Declares a dependency on Job 1. Deployment will **never** execute if the build or unit tests fail.
* **`if: ... && github.event_name != 'pull_request'`**: Ensures pull requests are tested but never deployed to production.
* **`environment:`**: Targets GitHub's dedicated `github-pages` deployment tracking environment and links the final live URL directly in the GitHub UI.

```yaml
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```
* Publishes the packaged artifact to GitHub's global CDN with zero downtime.

---

## 4. Security & Best Practices Highlights
1. **Least-Privilege Scoping**: Workflow permissions are explicitly declared (`contents: read`, `pages: write`, `id-token: write`) rather than inheriting broad default write access.
2. **Zero Hardcoded Secrets**: Uses native GitHub OIDC authentication tokens (`id-token: write`) rather than long-lived Personal Access Tokens (PATs).
3. **Fail-Fast Safety Gate**: If any math logic fails in `npm test` or a bundling error occurs in `npm run build`, Job 2 never starts. Production remains safe and untouched.
4. **Reproducible Toolchain**: Standardized on Node.js 20 LTS with deterministic dependency resolution (`npm ci`).

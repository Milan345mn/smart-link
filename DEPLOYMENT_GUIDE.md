# 🚀 GitHub Pages Continuous Deployment Guide

This guide details how to configure GitHub Pages for automated deployment, verify live releases, and make iterative updates through Continuous Deployment.

---

## 1. Deployment Overview & Platform Selection

* **Deployment Platform**: **GitHub Pages**
* **Deployment Mechanism**: Official GitHub Actions (`actions/deploy-pages@v4`)
* **Cost**: 100% Free for public GitHub repositories
* **SSL / TLS**: Automatic HTTPS certificate provided by GitHub
* **CDN**: Globally distributed Fastly CDN cache

### Why GitHub Actions for GitHub Pages?
Previously, GitHub Pages required pushing pre-built files to a `gh-pages` branch. The modern approach (used in this project) uses native GitHub Actions:
1. The `dist/` build directory is packaged using `actions/upload-pages-artifact@v3`.
2. The deployment is executed via OpenID Connect (OIDC) through `actions/deploy-pages@v4`.
3. No orphan branches or messy git histories are created.

---

## 2. GitHub Pages One-Time Repository Configuration

To allow GitHub Actions to publish your site to GitHub Pages:

1. Open your repository on GitHub: `https://github.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPOSITORY>`.
2. Click the **Settings** tab (gear icon at the top).
3. In the left navigation sidebar under the **Code and automation** section, click **Pages**.
4. Under **Build and deployment**:
   * Change **Source** from *"Deploy from a branch"* to:
     ```
     GitHub Actions
     ```
   * *(Note: When selected, GitHub Pages automatically activates the `github-pages` environment for your repository).*

That is the only manual configuration needed!

---

## 3. Deployment URL Structure

Once deployed, your live web application will be accessible at:
```text
https://<YOUR_GITHUB_USERNAME>.github.io/<YOUR_REPOSITORY_NAME>/
```

For example, with your GitHub username `Milan345mn` and repository `smart-link`:
* **Live Web App URL**: `https://Milan345mn.github.io/smart-link/`

---

## 4. Verification Workflow: First Deployment

1. Push your repository to GitHub:
   ```bash
   git push -u origin main
   ```
2. On GitHub, navigate to the **Actions** tab.
3. You will see a running workflow titled **CI/CD Pipeline**.
4. Click on the workflow run to view the execution tree:
   * **Job 1 (Build & Test)**:
     * Checkouts repository.
     * Sets up Node.js 20.
     * Installs dependencies (`npm ci`).
     * Runs 9 automated unit tests (`npm test`).
     * Compiles production build (`npm run build`).
     * Packages the `dist/` directory as a Pages artifact.
   * **Job 2 (Deploy to GitHub Pages)**:
     * Deploys the static assets directly to GitHub Pages.
5. In the run summary, you will see a link to the deployed application under the **deploy** job or under the environment status pill.
6. Open the URL in your browser and confirm that all calculator buttons (numbers, decimals, operators, clear, equals) work smoothly.

---

## 5. Verification Workflow: Automated Code Update (CD Demonstration)

To demonstrate Continuous Deployment in action:

1. Open `src/components/Frame.jsx` locally.
2. Update the title banner on line 52:
   ```jsx
   <div className="calculator-title">React Calculator v2.0 (CI/CD Verified)</div>
   ```
3. Commit and push the update:
   ```bash
   git add src/components/Frame.jsx
   git commit -m "chore: bump title to v2.0 for CD verification"
   git push origin main
   ```
4. Observe the **Actions** tab:
   * GitHub Actions detects the push event automatically.
   * It runs the tests, rebuilds the code, and redeploys to GitHub Pages in ~60 seconds.
5. Refresh your live URL: The title update appears live on the web without any manual FTP or file uploads!

---

## 6. Known Limitations & Troubleshooting

### Assets 404 (Blank White Screen)
* **Cause**: Vite was built with absolute root paths (`/assets/...`).
* **Resolution**: In our project, `vite.config.js` is already configured with `base: './'`. This guarantees assets are referenced relatively, preventing 404 errors regardless of repository name.

### Deployment Permission Denied
* **Cause**: Repository permissions did not allow GitHub Actions to write to Pages.
* **Resolution**: Ensure the workflow specifies `permissions: pages: write, id-token: write` (already included in `.github/workflows/ci-cd.yml`).

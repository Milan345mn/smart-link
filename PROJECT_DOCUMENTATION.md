# 📱 Project Documentation: React Calculator

## 1. Project Overview & Purpose
**React Calculator** is a clean, modern, single-page web calculator built with React 18 and Vite. It provides an intuitive, responsive user interface for performing everyday mathematical calculations directly in a web browser. The primary purpose of this project in this DevOps workflow is to serve as a reliable, fully working, self-contained application for implementing, testing, and deploying a modern Continuous Integration & Continuous Deployment (CI/CD) pipeline using GitHub Actions.

* **Original Repository**: [swapnilgupta/react-calculator](https://github.com/swapnilgupta/react-calculator)
* **License / Access**: Public open-source
* **Application Type**: Client-Side Single Page Application (SPA)

---

## 2. Application Architecture
The application adheres to modern component-based React architecture:

```
[Browser Window: index.html]
        │
        ▼
   [src/main.jsx]  ── mounts React root into `<div id="app"></div>`
        │
        ▼
   [src/components/Frame.jsx]  ── State Manager & Expression Evaluator
        │
        ├── State: `question` (Current formula string)
        ├── State: `answer`   (Evaluated mathematical result)
        │
        ├── Evaluator: `evaluateExpression(expression)`
        │     - Validates against regex: `/^[\d+\-*/.() ]+$/`
        │     - Computes result safely using isolated constructor
        │     - Guards against divide-by-zero (`Infinity` -> `'Error'`)
        │
        ├── [src/components/Screen.jsx]  ── Display Container
        │     ├── [ScreenRow.jsx] (Input formula)
        │     └── [ScreenRow.jsx] (Evaluated answer)
        │
        └── [src/components/Button.jsx]  ── Keypad elements
              - Numbers: 0–9
              - Decimal: .
              - Operators: +, -, *, /
              - Action: Cls (Clear)
              - Action: = (Evaluate)
```

---

## 3. Folder & File Structure
```text
react-calculator/
├── .gitignore               # Git ignore rules for node_modules, build outputs, and logs
├── index.html               # Main HTML entry point mounting React root
├── package.json             # Project metadata, NPM scripts, and dependency definitions
├── package-lock.json        # Deterministic lockfile for exact package versions
├── vite.config.js           # Vite bundler configuration (React plugin, build targets)
├── README.md                # Upstream repository README
├── screenshot.png           # Visual UI preview
└── src/
    ├── main.jsx             # React DOM rendering entry point
    ├── components/
    │   ├── Button.jsx       # Reusable button component with PropTypes validation
    │   ├── Frame.jsx        # Top-level calculator component, state, and math engine
    │   ├── Screen.jsx       # Screen wrapper component holding two ScreenRows
    │   └── ScreenRow.jsx    # Readonly display input field for questions and results
    └── styles/
        └── main.css         # Modern dark-mode UI stylesheet with CSS transitions
```

---

## 4. Programming Languages & Frameworks
* **JavaScript (ECMAScript Modern / ES Modules)**: Powers all logic, components, and module imports/exports.
* **React 18.3.1**: Modern declarative UI library using functional components and hooks (`useState`).
* **HTML5**: Base DOM template in `index.html`.
* **CSS3**: Responsive flexbox layout, custom color palette (`#1a1a2e`, `#0f0f23`, `#5e81f4`), and button animations.
* **Vite 6.0.5**: Lightning-fast frontend build tool and development server.

---

## 5. Dependencies & Packages
From `package.json`:

### Production Dependencies (`dependencies`)
| Package | Version | Purpose |
| :--- | :--- | :--- |
| `react` | `^18.3.1` | Core React library providing state and component lifecycle primitives |
| `react-dom` | `^18.3.1` | React package responsible for rendering virtual DOM to the browser DOM |

### Development Dependencies (`devDependencies`)
| Package | Version | Purpose |
| :--- | :--- | :--- |
| `vite` | `^6.0.5` | Next-generation bundler and local development server |
| `@vitejs/plugin-react` | `^4.3.4` | Official Vite plugin for React Fast Refresh and JSX transformation |
| `prop-types` | `^15.8.1` | Runtime type-checking for React props |

---

## 6. Configuration Files
* **`vite.config.js`**:
  Configures the Vite bundler. It imports `@vitejs/plugin-react` and specifies the build output directory (`dist`).
* **`package.json`**:
  Defines project name, scripts (`dev`, `build`, `preview`), and module type (`"type": "module"`).
* **`.gitignore`**:
  Specifies untracked files: `node_modules/`, `dist/`, and debug log files.

---

## 7. How the Application Works
1. **Initial Mount**: When the browser loads `index.html`, Vite loads `/src/main.jsx`. React creates a root on `<div id="app"></div>` and renders `<Frame />`.
2. **User Interaction**:
   - Clicking a numeric button or operator invokes `handleClick()`, appending the character to `question`.
   - Clicking `Cls` resets both `question` and `answer` to empty strings.
   - Clicking `=` calls `evaluateExpression(question)`.
3. **Safe Evaluation Logic**:
   - First tests the expression string against regex `/^[\d+\-*/.() ]+$/` to ensure no malicious code can run.
   - Executes the calculation using a sandboxed `Function` call.
   - If finite, returns string result; if non-finite (e.g. division by 0) or invalid syntax, returns `'Error'`.
4. **Reactive Rendering**: The display automatically updates through React's virtual DOM diffing.

---

## 8. How to Install, Build, and Run Locally

### Prerequisites
* **Node.js**: v18+ (tested on Node.js v22.19.0)
* **npm**: v9+ (tested on npm 10.9.3)

### Installation
Run within the `react-calculator` directory:
```bash
npm install
```

### Run Locally in Development Mode
Starts a local development server with hot-module replacement (HMR):
```bash
npm run dev
```
Open your browser at the reported local URL (typically `http://localhost:5173`).

### Production Build
Compiles and bundles the application for production deployment into the `dist/` directory:
```bash
npm run build
```

### Production Preview
Locally preview the generated production build:
```bash
npm run preview
```

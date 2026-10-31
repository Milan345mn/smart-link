# 🧪 Automated Testing Report: React Calculator

## 1. Testing Strategy & Purpose

In a Continuous Integration (CI) pipeline, automated tests act as the **quality gate**. If newly committed code introduces a regression, calculation bug, or security vulnerability, the CI pipeline fails immediately. This prevents defective code from reaching the production deployment stage.

The original upstream repository had zero automated tests. To make this project production-grade and meet assignment requirements, we implemented an automated unit testing suite targeting the core mathematical calculation engine (`evaluateExpression`).

---

## 2. Testing Framework: Vitest

* **Framework**: Vitest (`v5.0.5`)
* **Runner Command**: `npx vitest run` / `npm test`
* **Why Vitest was selected**:
  1. **Native Vite Integration**: Reads `vite.config.js` directly without duplicating bundler configurations or Babel plugins.
  2. **High Speed**: Executes tests in-memory in milliseconds using modern ES modules.
  3. **Standard Syntax**: Uses standard `describe`, `it`, and `expect` assertions compatible with Jest.

---

## 3. Test Suite Specification (`src/components/Frame.test.js`)

| Test # | Test Name | Input Expression | Expected Output | Actual Output | Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **1** | Addition | `'5+3'`<br>`'10 + 25'` | `'8'`<br>`'35'` | `'8'`<br>`'35'` | ✅ **PASS** |
| **2** | Subtraction | `'15-7'`<br>`'5 - 12'` | `'8'`<br>`'-7'` | `'8'`<br>`'-7'` | ✅ **PASS** |
| **3** | Multiplication | `'6*7'`<br>`'0 * 100'` | `'42'`<br>`'0'` | `'42'`<br>`'0'` | ✅ **PASS** |
| **4** | Division | `'20/4'`<br>`'9 / 2'` | `'5'`<br>`'4.5'` | `'5'`<br>`'4.5'` | ✅ **PASS** |
| **5** | Operator Precedence (BODMAS / PEMDAS) | `'2+3*4'`<br>`'(2+3)*4'` | `'14'`<br>`'20'` | `'14'`<br>`'20'` | ✅ **PASS** |
| **6** | Decimal Floating Point Operations | `'1.5 + 2.5'`<br>`'0.1 + 0.2'` | `'4'`<br>`0.3...` | `'4'`<br>`0.30000000000000004` | ✅ **PASS** |
| **7** | Division by Zero Handling | `'10/0'` | `'Error'` | `'Error'` | ✅ **PASS** |
| **8** | Syntax Errors & Unbalanced Parentheses | `'5++'`<br>`'(5+2'` | `'Error'`<br>`'Error'` | `'Error'`<br>`'Error'` | ✅ **PASS** |
| **9** | Code Injection & Malicious Script Rejection | `'alert("hack")'`<br>`'process.exit()'`<br>`'window.location'` | `'Error'`<br>`'Error'`<br>`'Error'` | `'Error'`<br>`'Error'`<br>`'Error'` | ✅ **PASS** |

---

## 4. Execution Terminal Output

```text
> react-calculator@1.0.0 test
> vitest run

 RUN  v5.0.5 E:/ev/react-calculator

 ✓ src/components/Frame.test.js (9 tests) 13ms

 Test Files  1 passed (1)
      Tests  9 passed (9)
   Start at  14:52:13
   Duration  820ms (transform 61%, import 30%, worker 4%, tests 4%)
```

---

## 5. Summary & CI Gate Compliance

* **Total Test Suites**: 1 (`src/components/Frame.test.js`)
* **Total Unit Tests Executed**: 9
* **Passed**: 9 (100%)
* **Failed**: 0
* **Execution Time**: ~820 milliseconds
* **CI Gate Status**: **PASSED (Exit Code: 0)**

The automated test suite runs as **Step 4** in Job 1 of the CI/CD pipeline. Any failure in this suite prevents Job 2 (Deployment to GitHub Pages) from running, maintaining continuous delivery safety.

# PR Reviewer Agent 🤖🔍

An AI GitHub bot that reviews pull requests for issues related to security, readability, and style. It uses LLMs to analyze diffs and leave comments on PRs with suggested improvements — perfect for OSS maintainers and dev teams.

---

## 🛠️ Features

- 🧠 LLM-powered PR review based on diff context
- 📝 Analyzes code for:
  - Security flaws
  - Readability
  - Performance
  - Style violations
- 🤖 Posts comments directly on GitHub PRs
- 🗂️ Categorized feedback (security, readability, etc.)
- 🧪 Optional mode for auto-generating test suggestions

---

## ⚙️ Tech Stack

- GitHub REST API (via webhooks or polling)
- Python 3.10+
- LangChain + OpenAI or Claude
- FastAPI backend server
- Redis queue (optional for async review)
- GitHub App or Personal Access Token

---

## 🚀 Setup

1. Clone the repo:

```bash
git clone https://github.com/HiraWaheed/PR_Reviewer.git
cd PR_Reviewer
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
````

2. Configure `.env`

```env
GITHUB_TOKEN=your_pat_or_app_token
OPENAI_API_KEY=your_openai_key
REPO_NAME=your-user/your-repo
```

3. Run the server:

```bash
uvicorn app.main:app --reload
```

---

## 🔗 Webhook Setup (GitHub App)

* Set up a GitHub App with:

  * `pull_request` and `pull_request_review` events
  * Permissions: read/write on Pull Requests and Comments
* Set webhook URL to your server endpoint (e.g. `/webhook`)

---

## 🧠 Agent Flow

1. PR is opened or updated
2. Diff is fetched from GitHub
3. LLM is prompted with:

   * Changed files
   * Code context
4. Review comments are generated and posted via API

---

## 🖼️ Example Output

```text
🛡️ Security Issue:
In `auth.py`, you're using `eval()` on user input. This is dangerous. Consider `ast.literal_eval` or refactoring the logic.

📚 Readability:
Consider splitting this 30-line function into smaller units.

✅ Suggestion:
Add a test case for the new `is_token_valid` function.
```


## 🧠 Ideas for Extension

* Integrate OWASP rules for vulnerability spotting
* Auto-close or label risky PRs
* Slack/Discord alerts for flagged changes
* Compare PR with past similar diffs


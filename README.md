

# The Browser

The Browser builds upon the foundation of the [browser-use](https://github.com/browser-use/browser-use) and its web interface [web-ui](https://github.com/browser-use/web-ui), which is designed to make webpages accessible for AI agents.



## Prerequisites

### Operating Systems

Only macOS is supported.



### Browsers

Chrome and non-Chrome browsers should be installed first.



## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/imyizhang/the-browser.git
cd the-browser
```



### Step 2: Set Up a Python Virtual Environment

We recommend using **[uv](https://docs.astral.sh/uv/)** for managing a Python virtual environment:

```bash
uv venv --python 3.11
source .venv/bin/activate
```



### Step 3: Install Dependencies

Install Python packages:
```bash
uv pip install -r requirements.txt
```



Install Browsers in Patchright:

```bash
patchright install --with-deps
```
or you can install specific browsers:
```bash
patchright install chromium --with-deps
```



### Step 4: Configure Environment Variables 

Create a copy of the example environment file as `.env`, and open `.env` in your preferred text editor and add your API keys and modify other settings:

```bash
cp .env.example .env
```


### Step 5: Enjoy The Browser

Run The Browser:

```bash
python app.py --ip 127.0.0.1 --port 7788 --theme Ocean
```



Close all Chrome windows. 



Open a non-Chrome browser, such as Firefox or Edge, and navigate to http://127.0.0.1:7788. ***This is important because the persistent browser context will use the Chrome data when running the agent.***


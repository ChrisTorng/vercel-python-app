# Flask App on Vercel

[How to deploy a Python/Flask App to Vercel - DEV Community](https://dev.to/andrewbaisden/how-to-deploy-a-python-flask-app-to-vercel-2o5k)

```cmd
npm i -g vercel
mkdir vercel-python-app
cd vercel-python-app
python3 -m venv .venv
.venv/bin/activate
pip install Flask
set FLASK_APP=index.py
set FLASK_ENV=development
flask run
```

[Step-by-Step Guide to Deploying a Project to Vercel using GitHub Actions for Free - DEV Community](https://dev.to/tobidelly/step-by-step-guide-to-deploying-a-project-to-vercel-using-github-actions-for-free-l61)

- Publish to GitHub
- [Vercel](https://vercel.com/christorngs-projects) - Add New.. - Project
- vercel-python-app - Import Project
- Framework Preset: Other
- Deploy
- Continue to Dashboard
- 
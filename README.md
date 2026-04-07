# REPS - Fitness Tracker

Your personal fitness companion. Simple, focused, built for consistency.

## Deploy to GitHub Pages (Free Hosting)

### Step 1: Create a GitHub Repository
1. Go to [github.com/new](https://github.com/new)
2. Name it `reps` (or anything you want)
3. Set it to **Public**
4. Click **Create repository**

### Step 2: Upload Files
Upload ALL of these files to the repository root:
- `index.html`
- `manifest.json`
- `sw.js`
- `icon-192.png`
- `icon-512.png`

You can drag-and-drop them on the GitHub page or use git:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/reps.git
git push -u origin main
```

### Step 3: Enable GitHub Pages
1. Go to your repo → **Settings** → **Pages**
2. Under "Source", select **Deploy from a branch**
3. Select **main** branch, **/ (root)** folder
4. Click **Save**
5. Wait 1-2 minutes for deployment

Your app will be live at: `https://YOUR_USERNAME.github.io/reps/`

### Step 4: Add to Phone Home Screen

**iPhone/iPad:**
1. Open the URL in Safari (must be Safari)
2. Tap the **Share** button (square with arrow)
3. Scroll down and tap **Add to Home Screen**
4. Tap **Add**

**Android:**
1. Open the URL in Chrome
2. Tap the **three-dot menu**
3. Tap **Install App** or **Add to Home Screen**
4. Tap **Install**

The app will now appear on your home screen like a native app — full screen, no browser bar, with the REPS icon.

## Where is my data stored?

| Data | Storage | Limit |
|------|---------|-------|
| Workouts, history, stats, settings | `localStorage` | ~5 MB |
| Progress photos | `IndexedDB` | ~50-100 MB+ |

**All data stays on YOUR device.** Nothing is sent to any server. 

### Important notes about data:
- **Clearing browser data WILL delete your app data** — be careful
- Photos are compressed to 800px max and JPEG quality 70% to save space
- You can store roughly 100-200 progress photos before hitting limits
- If you uninstall the PWA, your data may be deleted (varies by OS)

### Want cloud backup?
This version is local-only. For cloud sync, you'd need to add a backend (Firebase, Supabase, etc.). The app architecture is ready for that upgrade when needed.

## Tech Stack
- Pure HTML/CSS/JS with React 18 (CDN)
- Babel for in-browser JSX transformation
- IndexedDB for photo storage
- Service Worker for offline support
- PWA manifest for installable experience
- Zero build tools, zero dependencies to install

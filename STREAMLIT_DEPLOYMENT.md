# 🚀 Streamlit Cloud Deployment Guide

## 📋 **Deploy Both Apps to Streamlit Cloud**

You can deploy **both Task 1 and Task 2** as separate live apps!

---

## 🌐 **DEPLOYMENT STEPS**

### **Step 1: Go to Streamlit Cloud**
1. Visit: **https://share.streamlit.io/**
2. Sign in with your **GitHub account**

### **Step 2: Deploy Task 1 (Asha AI)**

1. Click **"New app"**
2. Fill in:
   - **Repository**: `SahanaGPDEV/ironlady-lead-engine`
   - **Branch**: `main`
   - **Main file path**: `task1_asha_ai/app.py`
   - **App URL** (custom): `ironlady-asha-ai` (or your choice)

3. Click **"Advanced settings"**
4. Add **Secrets** (TOML format):
   ```toml
   GROQ_API_KEY = "your_actual_groq_api_key_here"
   ```

5. Click **"Deploy!"**
6. Wait 2-3 minutes for deployment
7. Your app will be live at: `https://ironlady-lead-engine-9dzmeeryvgmu6qya835fky.streamlit.app/`

---

### **Step 3: Deploy Task 2 (Project Ironclad)**

1. Click **"New app"** again
2. Fill in:
   - **Repository**: `SahanaGPDEV/ironlady-lead-engine`
   - **Branch**: `main`
   - **Main file path**: `task2_project_ironclad/dashboard.py`
   - **App URL** (custom): `ironlady-crm` (or your choice)

3. Click **"Advanced settings"**
4. Add **Secrets** (TOML format):
   ```toml
   GROQ_API_KEY = "your_actual_groq_api_key_here"
   ```

5. Click **"Deploy!"**
6. Wait 2-3 minutes for deployment
7. Your app will be live at: `https://ironlady-crm.streamlit.app`

---

## 🔗 **After Deployment**

You'll have **2 live apps**:
- 🌸 **Asha AI** (Customer-facing): `https://ironlady-lead-engine-9dzmeeryvgmu6qya835fky.streamlit.app/`
- 🛡️ **Project Ironclad** (Internal CRM): `https://ironlady-crm.streamlit.app`

---

## ⚠️ **IMPORTANT: Shared Data Issue**

**Problem**: Streamlit Cloud apps can't share the same `leads.csv` file because they're deployed separately.

**Solutions**:

### **Option 1: Demo Mode (Recommended for Submission)**
- Each app works independently
- Task 1 saves leads to its own CSV
- Task 2 loads its own CSV
- For demo videos, show the local version where they're integrated

### **Option 2: Use Google Sheets (Advanced)**
- Replace `leads.csv` with Google Sheets API
- Both apps read/write to the same sheet
- Requires additional setup

### **Option 3: Use a Database (Production)**
- Use Supabase, Firebase, or PostgreSQL
- Both apps connect to the same database
- Best for real production use

**For your submission, Option 1 is fine!** Just mention in your README that the deployed versions are for individual app demos, while the local version shows the full integration.

---

## 📝 **Update Your README**

After deployment, add this section to your README:

```markdown
## 🌐 Live Demos

### Task 1: Asha AI (Customer Advisor)
🔗 **Live App**: https://ironlady-lead-engine-9dzmeeryvgmu6qya835fky.streamlit.app/

### Task 2: Project Ironclad (Internal CRM)
🔗 **Live App**: https://ironlady-crm.streamlit.app

> **Note**: The deployed versions run independently. For the complete integrated workflow (where leads flow from Task 1 to Task 2), please run locally using the setup instructions below.
```

---

## 🔧 **Troubleshooting**

### **If deployment fails:**
1. Check the **Logs** in Streamlit Cloud
2. Verify `requirements.txt` exists in the correct folder
3. Ensure all imports are correct
4. Check that secrets are properly formatted (TOML)

### **If app crashes:**
- Check for missing dependencies
- Verify file paths are correct
- Look at error logs in Streamlit Cloud

### **To update deployed app:**
1. Push changes to GitHub: `git push`
2. Streamlit Cloud auto-redeploys (takes 1-2 min)

---

## 🎯 **Benefits of Deployment**

✅ **Live demos** - Share links instead of videos  
✅ **Professional** - Shows deployment skills  
✅ **Accessible** - Anyone can try your apps  
✅ **Impressive** - Evaluators can interact directly  

---

## 🏆 **Final Checklist**

- [ ] Deploy Task 1 to Streamlit Cloud
- [ ] Deploy Task 2 to Streamlit Cloud
- [ ] Test both live apps
- [ ] Update README with live links
- [ ] Push README update to GitHub
- [ ] Include live links in submission form

---

**Your apps will be live and accessible to everyone!** 🌟

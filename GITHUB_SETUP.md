# 🚀 GitHub Setup Guide

## 📋 **Step-by-Step Instructions**

### **Step 1: Initialize Git Repository**

Open a terminal in your project folder and run:

```bash
cd "c:/Users/sahana gp/ironlady_assignment"
git init
```

---

### **Step 2: Add All Files**

```bash
git add .
```

This will add all files **except** those in `.gitignore` (like `.env` files - which is good for security!)

---

### **Step 3: Create Initial Commit**

```bash
git commit -m "Initial commit: Iron Lady Lead Engine - Complete integrated system with AI"
```

---

### **Step 4: Create GitHub Repository**

1. Go to **https://github.com**
2. Click **"New repository"** (green button)
3. Repository name: `ironlady-lead-engine` (or your preferred name)
4. Description: `AI-Powered Lead Management System - Integrated customer advisor and internal CRM`
5. **Keep it PUBLIC** (required for submission)
6. **DO NOT** initialize with README (you already have one)
7. Click **"Create repository"**

---

### **Step 5: Connect Local to GitHub**

GitHub will show you commands. Use these:

```bash
git remote add origin https://github.com/YOUR_USERNAME/ironlady-lead-engine.git
git branch -M main
git push -u origin main
```

**Replace `YOUR_USERNAME`** with your actual GitHub username!

---

### **Step 6: Verify Upload**

1. Refresh your GitHub repository page
2. You should see all your files:
   - ✅ `README.md`
   - ✅ `task1_asha_ai/`
   - ✅ `task2_project_ironclad/`
   - ✅ `leads.csv`
   - ✅ `.gitignore`
   - ✅ `.env.example`
   - ✅ All other files

3. **IMPORTANT**: Check that `.env` is **NOT** visible (it should be ignored for security)

---

## 🔒 **Security Checklist**

Before pushing, verify:

- [ ] `.env` is in `.gitignore` ✅ (already done)
- [ ] `.env` files are NOT in the repository
- [ ] Only `.env.example` is included (without real API key)
- [ ] `leads.csv` can be included (it's demo data)

---

## 📝 **After Pushing to GitHub**

### **Update README with Links:**

1. Add your GitHub repository link
2. Add demo video links (after recording)
3. Commit and push changes:

```bash
git add README.md
git commit -m "Add demo video links"
git push
```

---

## 🎯 **Final Submission Steps**

1. ✅ **GitHub Repository**: Created and public
2. ✅ **README.md**: Complete with setup instructions
3. ✅ **Demo Videos**: Recorded and linked in README
4. ✅ **Code Quality**: Clean, documented, working
5. ✅ **Integration**: End-to-end flow verified

### **Submit via Google Form:**

Fill out the submission form with:
- Your GitHub repository URL
- Demo video links
- Brief description of your system

---

## 🆘 **Troubleshooting**

### **If Git is not installed:**
Download from: https://git-scm.com/downloads

### **If push fails:**
```bash
git config --global user.email "your.email@example.com"
git config --global user.name "Your Name"
```

Then try pushing again.

### **If you need to update after first push:**
```bash
git add .
git commit -m "Update: [describe your changes]"
git push
```

---

## 🏆 **You're Almost Done!**

After GitHub setup:
1. Record demo videos
2. Add video links to README
3. Submit the form
4. Celebrate! 🎉

**Your Iron Lady Lead Engine is submission-ready!**

import streamlit as st
import pandas as pd
import os
from datetime import datetime
from groq import Groq
from dotenv import load_dotenv
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components

# Load environment variables
load_dotenv()

# Configuration
start_dir = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.normpath(os.path.join(start_dir, "..", "leads.csv"))

st.set_page_config(
    page_title="Project Ironclad | Lead Command Center",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------------------------------------------
# PREMIUM STYLES
# -------------------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .main-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #881337 100%);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(0,0,0,0.3);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.12);
        text-align: center;
        border: 1px solid rgba(255,255,255,0.8);
        transition: all 0.3s ease;
        height: 140px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 48px rgba(0,0,0,0.2);
    }
    
    .metric-value {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #881337 0%, #be123c 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 8px;
    }
    
    .metric-label {
        color: #64748b;
        font-size: 0.875rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .lead-card {
        background: white;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 16px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.08);
        border-left: 4px solid #881337;
        transition: all 0.3s ease;
    }
    
    .lead-card:hover {
        box-shadow: 0 8px 32px rgba(0,0,0,0.16);
        transform: translateX(4px);
    }
    
    .status-badge {
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.75rem;
        display: inline-block;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .status-new { 
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        color: #1e40af;
    }
    .status-contacted { 
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        color: #92400e;
    }
    .status-nurturing {
        background: linear-gradient(135deg, #e0e7ff 0%, #c7d2fe 100%);
        color: #3730a3;
    }
    .status-converted { 
        background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%);
        color: #166534;
    }
    .status-lost { 
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
        color: #991b1b;
    }
    
    .ai-message-box {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        border-radius: 12px;
        padding: 20px;
        border-left: 4px solid #0ea5e9;
        margin: 16px 0;
        box-shadow: 0 4px 12px rgba(14,165,233,0.1);
    }
    
    .section-header {
        font-size: 1.5rem;
        font-weight: 700;
        color: white;
        margin: 24px 0 16px 0;
        padding-bottom: 8px;
        border-bottom: 3px solid rgba(255,255,255,0.3);
    }
    
    .stButton>button {
        border-radius: 10px;
        font-weight: 600;
        padding: 12px 24px;
        transition: all 0.3s ease;
        border: none;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 24px rgba(0,0,0,0.2);
    }
    
    div[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
    }
    
    div[data-testid="stSidebar"] * {
        color: white !important;
    }
    
    .stDataFrame {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------------------------
# DATA MANAGEMENT
# -------------------------------------------------------------------------------------
@st.cache_data(ttl=5)
def load_data():
    if not os.path.exists(CSV_FILE):
        # Create sample data for demo
        sample_data = {
            "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
            "Name": ["Demo User"],
            "Role": ["Professional"],
            "Challenge": ["Career Growth"],
            "Goal": ["Get promoted to leadership role"],
            "Program": ["Leadership Accelerator"],
            "Status": ["New"],
            "Notes": ["Sample lead for demonstration"],
            "Version": ["A"]
        }
        df = pd.DataFrame(sample_data)
        df.to_csv(CSV_FILE, index=False)
        return df
    
    try:
        df = pd.read_csv(CSV_FILE)
        required_cols = ["Timestamp", "Name", "Role", "Challenge", "Goal", "Program", "Status", "Notes", "Version"]
        for col in required_cols:
            if col not in df.columns:
                if col == "Notes": df[col] = ""
                elif col == "Status": df[col] = "New"
                elif col == "Version": df[col] = "N/A"
                else: df[col] = "N/A"
        
        df["Status"] = df["Status"].fillna("New")
        df["Notes"] = df["Notes"].fillna("")
        df["Version"] = df["Version"].fillna("N/A")
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

def save_data(df):
    try:
        df.to_csv(CSV_FILE, index=False)
        st.cache_data.clear()
        return True
    except Exception as e:
        st.error(f"Error saving data: {e}")
        return False

# -------------------------------------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🛡️ PROJECT IRONCLAD")
    st.markdown("*AI-Augmented Lead Command Center*")
    st.divider()

    # Authentication
    st.markdown("🔒 **ACCESS CONTROL**")
    pwd = st.text_input("Enter CRM Password", type="password")
    if pwd != "ironlady2025": # Simple demo password
        if pwd: st.error("❌ Incorrect Password")
        st.warning("Please enter password to access CRM dashboard.")
        st.info("💡 Hint: ironlady2025")
        st.stop()
    st.success("✅ Access Granted")
    st.divider()
    
    df = load_data()
    
    st.markdown("#### 🔍 FILTERS")
    if not df.empty:
        all_statuses = df["Status"].unique().tolist()
        status_filter = st.multiselect("Status", all_statuses, default=all_statuses, key="status_filter")
        
        all_programs = df["Program"].unique().tolist()
        program_filter = st.multiselect("Program", all_programs, default=all_programs, key="program_filter")
        
        filtered_df = df[
            (df["Status"].isin(status_filter)) & 
            (df["Program"].isin(program_filter))
        ]
    else:
        filtered_df = df
    
    st.divider()
    st.markdown("#### ➕ QUICK ACTIONS")
    
    with st.expander("✨ Add New Lead", expanded=False):
        with st.form("add_lead_form", clear_on_submit=True):
            new_name = st.text_input("Full Name*")
            new_role = st.selectbox("Current Role", ["Student", "Professional", "Manager", "Career Break", "Entrepreneur"])
            new_challenge = st.selectbox("Main Challenge", ["Low Confidence", "Career Growth", "Work-Life Balance", "Leadership Skills", "Public Speaking"])
            new_goal = st.text_area("Goal", placeholder="What do they want to achieve?")
            new_program = st.selectbox("Interested Program", ["Leadership Accelerator", "Career Restart", "Entrepreneurs 10X", "Public Speaking Mastery"])
            
            if st.form_submit_button("💾 Add Lead", use_container_width=True):
                if new_name:
                    new_entry = {
                        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "Name": new_name,
                        "Role": new_role,
                        "Challenge": new_challenge,
                        "Goal": new_goal,
                        "Program": new_program,
                        "Status": "New",
                        "Notes": "Added manually via CRM"
                    }
                    current_df = load_data()
                    current_df = pd.concat([current_df, pd.DataFrame([new_entry])], ignore_index=True)
                    if save_data(current_df):
                        st.success("✅ Lead added successfully!")
                        st.rerun()
                else:
                    st.error("Name is required!")

# -------------------------------------------------------------------------------------
# MAIN DASHBOARD
# -------------------------------------------------------------------------------------

# Header
st.markdown("""
<div class="main-header">
    <h1 style="margin:0; font-size:2.5rem;">🛡️ PROJECT IRONCLAD</h1>
    <p style="margin:8px 0 0 0; font-size:1.1rem; opacity:0.9;">AI-Powered Lead Management & Conversion Engine</p>
</div>
""", unsafe_allow_html=True)

# KPIs
if not df.empty:
    col1, col2, col3, col4, col5 = st.columns(5)
    
    total = len(df)
    new_count = len(df[df["Status"] == "New"])
    contacted = len(df[df["Status"] == "Contacted"])
    nurturing = len(df[df["Status"] == "Nurturing"])
    converted = len(df[df["Status"] == "Converted"])
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{total}</div>
            <div class="metric-label">Total Leads</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{new_count}</div>
            <div class="metric-label">🆕 New</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{contacted}</div>
            <div class="metric-label">📞 Contacted</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{nurturing}</div>
            <div class="metric-label">🌱 Nurturing</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{converted}</div>
            <div class="metric-label">✅ Converted</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Conversion Rate
    conversion_rate = (converted / total * 100) if total > 0 else 0
    
    # Version Performance
    vers_a = df[df["Version"] == "A"]
    vers_b = df[df["Version"] == "B"]
    conv_a = (len(vers_a[vers_a["Status"] == "Converted"]) / len(vers_a) * 100) if len(vers_a) > 0 else 0
    conv_b = (len(vers_b[vers_b["Status"] == "Converted"]) / len(vers_b) * 100) if len(vers_b) > 0 else 0

    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); 
                color: white; padding: 16px; border-radius: 12px; text-align: center; 
                margin: 20px 0; box-shadow: 0 4px 16px rgba(16,185,129,0.3);">
        <h3 style="margin:0;">Overall Conversion Rate: {conversion_rate:.1f}%</h3>
        <p style="margin:4px 0 0 0; opacity:0.9;">
            🧪 A/B Performance: Version A (Warm): {conv_a:.1f}% | Version B (Urgent): {conv_b:.1f}%
        </p>
    </div>
    """, unsafe_allow_html=True)

# Lead Pipeline
st.markdown('<h2 class="section-header">📋 LEAD PIPELINE</h2>', unsafe_allow_html=True)

if not filtered_df.empty:
    # Display as cards instead of table for better UX
    display_df = filtered_df[["Name", "Role", "Program", "Status", "Challenge"]].copy()
    
    # Interactive table
    event = st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,
        on_select="rerun",
        selection_mode="single-row",
        column_config={
            "Name": st.column_config.TextColumn("👤 Name", width="medium"),
            "Role": st.column_config.TextColumn("💼 Role", width="small"),
            "Program": st.column_config.TextColumn("📚 Program", width="medium"),
            "Status": st.column_config.TextColumn("📊 Status", width="small"),
            "Version": st.column_config.TextColumn("🧪 Test", width="small"),
            "Challenge": st.column_config.TextColumn("🚧 Challenge", width="medium"),
        }
    )
    
    # Lead Detail View
    if event and event["selection"]["rows"]:
        selected_idx = event["selection"]["rows"][0]
        actual_idx = filtered_df.index[selected_idx]
        lead = df.loc[actual_idx]
        
        st.markdown("---")
        st.markdown(f'<h2 class="section-header">👤 LEAD ANALYSIS: {lead["Name"]}</h2>', unsafe_allow_html=True)
        
        col_left, col_right = st.columns([1.2, 1])
        
        with col_left:
            # Lead Info Card
            st.markdown(f"""
            <div class="lead-card">
                <h3 style="margin-top:0; color:#881337;">📋 Lead Information</h3>
                <p><strong>Role:</strong> {lead['Role']}</p>
                <p><strong>Program Interest:</strong> {lead['Program']}</p>
                <p><strong>Status:</strong> <span class="status-badge status-{lead['Status'].lower()}">{lead['Status']}</span></p>
                <p><strong>🧪 A/B Version:</strong> {lead['Version']}</p>
                <p><strong>🎯 Goal:</strong> {lead['Goal']}</p>
                <p><strong>🚧 Challenge:</strong> {lead['Challenge']}</p>
                <p><strong>📅 Captured:</strong> {lead['Timestamp']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("🎙️ Hear User Goal", use_container_width=True):
                goal_text = f"User goal from {lead['Name']}: {lead['Goal']}".replace('"', "'")
                components.html(f"""
                    <script>
                        window.parent.speechSynthesis.cancel();
                        var msg = new SpeechSynthesisUtterance("{goal_text}");
                        msg.pitch = 0.9;
                        msg.rate = 1.0;
                        window.parent.speechSynthesis.speak(msg);
                    </script>
                """, height=0)
            
            # AI Co-Pilot
            st.markdown("### 🤖 AI CO-PILOT")
            st.markdown("*Generate personalized follow-up messages in seconds*")
            
            if st.button("✨ Generate Custom Follow-Up Message", use_container_width=True, type="primary"):
                api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
                
                if api_key:
                    try:
                        with st.spinner("🧠 AI is crafting your personalized message..."):
                            client = Groq(api_key=api_key)
                            prompt = f"""
                            You are a senior counselor at Iron Lady, a premium women's leadership academy.
                            
                            Lead Details:
                            - Name: {lead['Name']}
                            - Role: {lead['Role']}
                            - Challenge: {lead['Challenge']}
                            - Goal: {lead['Goal']}
                            - Program: {lead['Program']}
                            
                            Write a warm, professional WhatsApp message (2-3 sentences) that:
                            1. Addresses them by name
                            2. Acknowledges their specific goal
                            3. Creates urgency with a clear call-to-action
                            4. Feels personal and empowering
                            
                            Keep it conversational and compelling.
                            """
                            
                            completion = client.chat.completions.create(
                                model="llama-3.1-8b-instant",
                                messages=[{"role": "user", "content": prompt}],
                                temperature=0.7,
                                max_tokens=200
                            )
                            
                            msg = completion.choices[0].message.content
                            
                            st.markdown(f"""
                            <div class="ai-message-box">
                                <h4 style="margin-top:0; color:#0369a1;">✅ AI-Generated Message</h4>
                                <p style="font-size:1.05rem; line-height:1.6;">{msg}</p>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            st.code(msg, language="text")
                            st.caption("💡 Copy the message above and send via WhatsApp")
                            
                    except Exception as e:
                        st.error(f"❌ AI Error: {str(e)}")
                else:
                    st.warning("⚠️ Please configure GROQ_API_KEY in your .env file to use AI features.")
        
        with col_right:
            # Update Form
            st.markdown("### ✏️ UPDATE LEAD")
            
            with st.form("update_lead_form"):
                new_status = st.selectbox(
                    "Status",
                    ["New", "Contacted", "Nurturing", "Converted", "Lost"],
                    index=["New", "Contacted", "Nurturing", "Converted", "Lost"].index(lead.get("Status", "New"))
                )
                
                notes = st.text_area(
                    "Internal Notes",
                    value=lead.get("Notes", ""),
                    height=150,
                    placeholder="Add follow-up notes, next steps, or important details..."
                )
                
                col_btn1, col_btn2 = st.columns(2)
                
                with col_btn1:
                    save_btn = st.form_submit_button("💾 Save Changes", use_container_width=True, type="primary")
                
                with col_btn2:
                    delete_btn = st.form_submit_button("🗑️ Delete Lead", use_container_width=True)
                
                if save_btn:
                    df.at[actual_idx, "Status"] = new_status
                    df.at[actual_idx, "Notes"] = notes
                    if save_data(df):
                        st.success("✅ Lead updated successfully!")
                        st.balloons()
                        st.rerun()
                
                if delete_btn:
                    df = df.drop(actual_idx)
                    if save_data(df):
                        st.warning("🗑️ Lead deleted.")
                        st.rerun()
            
            # Quick Stats for this lead
            st.markdown("### 📊 QUICK STATS")
            days_since = (datetime.now() - pd.to_datetime(lead['Timestamp'])).days
            st.metric("Days in Pipeline", f"{days_since} days")
            st.metric("Current Stage", lead['Status'])

else:
    st.info("📭 No leads match your current filters. Try adjusting the filters or add a new lead manually.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:white; padding:20px; opacity:0.8;">
    <p><strong>Project Ironclad</strong> | AI-Powered Lead Management System</p>
    <p style="font-size:0.875rem;">Built with ❤️ for Iron Lady | Powered by Groq AI</p>
</div>
""", unsafe_allow_html=True)

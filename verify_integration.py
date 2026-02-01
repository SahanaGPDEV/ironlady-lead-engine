import os
import csv
import pandas as pd
from datetime import datetime

# Define paths
ROOT_DIR = os.getcwd()
CSV_PATH = os.path.join(ROOT_DIR, "leads.csv")

print(f"Checking Data Bridge at: {CSV_PATH}")

# 1. Simulate Task 1: Create a Lead
print("--- [Step 1] Simulating Task 1 (Asha AI) Lead Capture ---")
test_lead = {
    "name": "Verification User",
    "role": "QA Engineer",
    "challenge": "Testing Integrity",
    "goal": "Ensure Zero Bugs",
    "program": "Systems Mastery"
}

try:
    file_exists = os.path.isfile(CSV_PATH)
    with open(CSV_PATH, "a", newline="", encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "Name", "Role", "Challenge", "Goal", "Program", "Status", "Notes"])
        
        writer.writerow([
            datetime.now(),
            test_lead['name'],
            test_lead['role'],
            test_lead['challenge'],
            test_lead['goal'],
            test_lead['program'],
            "New",
            ""
        ])
    print("✅ Lead saved successfully to CSV.")
except Exception as e:
    print(f"❌ Failed to save lead: {e}")
    exit(1)

# 2. Simulate Task 2: Read and Update Lead
print("\n--- [Step 2] Simulating Task 2 (Project Ironclad) CRUD ---")
try:
    df = pd.read_csv(CSV_PATH)
    print(f"✅ CSV Loaded. Total rows: {len(df)}")
    
    # Verify the lead exists
    target_lead = df[df["Name"] == "Verification User"]
    if target_lead.empty:
        print("❌ Lead not found in DataFrame!")
        exit(1)
    else:
        print("✅ Lead found in DataFrame.")
        
    # Simulate Update (Status Change)
    idx = target_lead.index[0]
    df.at[idx, "Status"] = "Contacted"
    df.at[idx, "Notes"] = "Automated verification test."
    
    # Save back
    df.to_csv(CSV_PATH, index=False)
    print("✅ Lead updated and saved back to CSV.")
    
except Exception as e:
    print(f"❌ Failed during CRUD operation: {e}")
    exit(1)

# 3. Final Verification
print("\n--- [Step 3] Final Data Integrity Check ---")
try:
    final_df = pd.read_csv(CSV_PATH)
    updated_lead = final_df[final_df["Name"] == "Verification User"].iloc[0]
    
    if updated_lead["Status"] == "Contacted" and updated_lead["Notes"] == "Automated verification test.":
        print("✅ SUCCESS: Data flow verified! Task 1 -> CSV -> Task 2 Update verified.")
        
        # Cleanup (Optional: remove the test user to keep file clean)
        # final_df = final_df[final_df["Name"] != "Verification User"]
        # final_df.to_csv(CSV_PATH, index=False)
        # print("🧹 Cleanup completed.")
    else:
        print("❌ FAILURE: Data did not match expected values after update.")
        print(updated_lead)
        exit(1)
        
except Exception as e:
    print(f"❌ Verification failed: {e}")
    exit(1)

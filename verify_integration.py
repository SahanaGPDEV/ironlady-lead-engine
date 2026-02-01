import os
import csv
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
    rows = []
    with open(CSV_PATH, "r", newline="", encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    print(f"✅ CSV Loaded. Total rows: {len(rows)}")
    
    # Verify the lead exists
    found = False
    for row in rows:
        if row["Name"] == "Verification User":
            found = True
            row["Status"] = "Contacted"
            row["Notes"] = "Automated verification test."
            break
            
    if not found:
        print("❌ Lead not found in CSV!")
        exit(1)
    else:
        print("✅ Lead found and updated in memory.")
        
    # Save back
    if rows:
        header = list(rows[0].keys())
        with open(CSV_PATH, "w", newline="", encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(rows)
        print("✅ CSV updated and saved back to disk.")
    
except Exception as e:
    print(f"❌ Failed during CRUD operation: {e}")
    exit(1)

# 3. Final Verification
print("\n--- [Step 3] Final Data Integrity Check ---")
try:
    with open(CSV_PATH, "r", newline="", encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
    updated_lead = next((r for r in rows if r["Name"] == "Verification User"), None)
    
    if updated_lead and updated_lead["Status"] == "Contacted" and updated_lead["Notes"] == "Automated verification test.":
        print("✅ SUCCESS: Data flow verified! Task 1 -> CSV -> Task 2 Update verified.")
        
        # Cleanup (Optional)
        # rows = [r for r in rows if r["Name"] != "Verification User"]
        # with open(CSV_PATH, "w", newline="", encoding='utf-8') as f:
        #     writer = csv.DictWriter(f, fieldnames=header)
        #     writer.writeheader()
        #     writer.writerows(rows)
        # print("Check complete")
    else:
        print("❌ FAILURE: Data did not match expected values after update.")
        print(updated_lead)
        exit(1)
        
except Exception as e:
    print(f"❌ Verification failed: {e}")
    exit(1)

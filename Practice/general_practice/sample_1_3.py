import pandas as pd
from itertools import cycle

# Define your job lists
bronze_jobs_list = [
    "Private Courses", "User Research", "Shared Hosting", "Generic Domain", "Litigation Service",
    "Customer Support", "NFT Artwork", "Investment Advisory", "Coin Insurance", "Estate Planning",
    "Personal Loan", "Private Ledger Services", "Blockchain Developer", "5G Installation", "Graphic Design",
    "Private Network Setup", "Account Setup", "Sports Event Coverage", "Firewall Coding", "Cold Calling",
    "Marketing Strategy", "Manage Securities", "CPU Development", "Business Storage", "Sample 1",
    "Solar Panel Installation", "Business Tokenization"
]

silver_jobs_list = [
    "Public Courses", "Interaction Design", "Dedicated Hosting", "Top Level Domain", "Legal Consultations",
    "Telemarketing", "UI Development", "Tax Filing", "Asset Insurance", "Estate Management", "Business Loan",
    "Ledger Data Upkeep", "Protocol Engineering", "Wi-Fi Coverage", "Animation Coding", "Small Office Network Setup",
    "Data Analysis", "Entertainment Event Coverage", "Malware Protection", "Trade Advising",
    "Search Engine Optimization",
    "Portfolio Management", "Motherboard Development", "Corporate Storage", "Sample 2", "Wind Turbines Construction",
    "National Tokenization"
]

gold_jobs_list = [
    "Business Courses", "Information Architect", "Cloud Hosting", "Premium Domain", "Corporate Defense",
    "Survey Campaign", "NFT Game", "Venture Capital", "Corporate Insurance", "Estate Security", "Corporate Loan",
    "Company Ledger Services", "Token Development", "Tower Management", "Game Publishing", "Corporate Network Setup",
    "Online Marketing", "VIP Event Coverage", "VPN Development", "Token Trading", "Copywriting", "Growth Funding",
    "GPU Development", "Encryption Services", "Sample 3", "Energy Grid Optimization", "Global Tokenization"
]

# Create cycles for each job list so they repeat indefinitely
bronze_cycle = cycle(bronze_jobs_list)
silver_cycle = cycle(silver_jobs_list)
gold_cycle = cycle(gold_jobs_list)

# Simulation settings:
# We work in 30-minute increments (0.5 hour)
time_step = 0.5
total_hours = 24
num_steps = int(total_hours / time_step)  # 48 steps

# Target active jobs at any given moment:
# (These numbers come from the desired steady-state active jobs given the job durations.)
target_bronze = 18  # Bronze jobs last 0.5 hour → 12 active means 24 new per hour overall.
target_silver = 9  # Silver jobs last 1 hour → 12 active means 12 new per hour.
target_gold = 3  # Gold jobs last 2 hours → 6 active means 3 new per hour.
target_total = target_bronze + target_silver + target_gold  # Should be 30 active jobs.

# Durations (in hours) for each job type:
duration_bronze = 0.5
duration_silver = 1.0
duration_gold = 2.0

# Lists to keep track of currently active jobs.
# Each item is a tuple: (job_name, expiry_time)
active_bronze = []
active_silver = []
active_gold = []

# List to record the schedule (each time step with the new jobs spawned).
schedule = []


def format_time(hour_float):
    hours = int(hour_float)
    minutes = int((hour_float - hours) * 60)
    return f"{hours:02d}:{minutes:02d}"


# Simulation loop: for each time step, update active jobs and record new ones.
for step in range(num_steps + 1):  # include final time step
    current_time = step * time_step  # e.g., 0.0, 0.5, 1.0, ...

    # Remove expired jobs (those with expiry time <= current_time)
    active_bronze = [job for job in active_bronze if job[1] > current_time]
    active_silver = [job for job in active_silver if job[1] > current_time]
    active_gold = [job for job in active_gold if job[1] > current_time]

    # Count current active jobs
    count_bronze = len(active_bronze)
    count_silver = len(active_silver)
    count_gold = len(active_gold)

    # Lists to store only the newly added jobs this time step
    new_bronze = []
    new_silver = []
    new_gold = []

    # Add new bronze jobs if needed to reach target_bronze
    if count_bronze < target_bronze:
        needed = target_bronze - count_bronze
        for _ in range(needed):
            job_name = next(bronze_cycle)
            expiry = current_time + duration_bronze
            active_bronze.append((job_name, expiry))
            new_bronze.append(job_name)

    # Add new silver jobs if needed to reach target_silver
    if count_silver < target_silver:
        needed = target_silver - count_silver
        for _ in range(needed):
            job_name = next(silver_cycle)
            expiry = current_time + duration_silver
            active_silver.append((job_name, expiry))
            new_silver.append(job_name)

    # Add new gold jobs if needed to reach target_gold
    if count_gold < target_gold:
        needed = target_gold - count_gold
        for _ in range(needed):
            job_name = next(gold_cycle)
            expiry = current_time + duration_gold
            active_gold.append((job_name, expiry))
            new_gold.append(job_name)

    # Optionally, you can check that the total active jobs is still target_total.
    total_active = len(active_bronze) + len(active_silver) + len(active_gold)
    if total_active != target_total:
        print(f"Warning at time {current_time}: active total = {total_active}, expected {target_total}")

    # Record only the new jobs for this time step.
    schedule.append({
        "Time": format_time(current_time),
        "New Bronze Jobs (30 min)": "\n".join(new_bronze),
        "New Silver Jobs (60 min)": "\n".join(new_silver),
        "New Gold Jobs (120 min)": "\n".join(new_gold),
        "Total New Jobs": len(new_bronze) + len(new_silver) + len(new_gold)
    })

# Create a DataFrame from the schedule and save it to Excel.
df = pd.DataFrame(schedule)
output_file = "job_schedule_new_jobs_only.xlsx"
df.to_excel(output_file, index=False)
print(f"Excel file created: {output_file}")

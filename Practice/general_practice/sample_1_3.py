import pandas as pd
from itertools import cycle

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

bronze_cycle = cycle(bronze_jobs_list)
silver_cycle = cycle(silver_jobs_list)
gold_cycle = cycle(gold_jobs_list)

time_step = 0.5
total_hours = 24
num_steps = int(total_hours / time_step)


target_bronze = 18
target_silver = 9
target_gold = 3
target_total = target_bronze + target_silver + target_gold

duration_bronze = 0.5
duration_silver = 1.0
duration_gold = 2.0

active_bronze = []
active_silver = []
active_gold = []

schedule = []


def format_time(hour_float):
    hours = int(hour_float)
    minutes = int((hour_float - hours) * 60)
    return f"{hours:02d}:{minutes:02d}"


for step in range(num_steps + 1):
    current_time = step * time_step

    # Remove expired jobs (those with expiry time <= current_time)
    active_bronze = [job for job in active_bronze if job[1] > current_time]
    active_silver = [job for job in active_silver if job[1] > current_time]
    active_gold = [job for job in active_gold if job[1] > current_time]

    count_bronze = len(active_bronze)
    count_silver = len(active_silver)
    count_gold = len(active_gold)

    new_bronze = []
    new_silver = []
    new_gold = []

    if count_bronze < target_bronze:
        needed = target_bronze - count_bronze
        for _ in range(needed):
            job_name = next(bronze_cycle)
            expiry = current_time + duration_bronze
            active_bronze.append((job_name, expiry))
            new_bronze.append(job_name)

    if count_silver < target_silver:
        needed = target_silver - count_silver
        for _ in range(needed):
            job_name = next(silver_cycle)
            expiry = current_time + duration_silver
            active_silver.append((job_name, expiry))
            new_silver.append(job_name)

    if count_gold < target_gold:
        needed = target_gold - count_gold
        for _ in range(needed):
            job_name = next(gold_cycle)
            expiry = current_time + duration_gold
            active_gold.append((job_name, expiry))
            new_gold.append(job_name)

    total_active = len(active_bronze) + len(active_silver) + len(active_gold)
    if total_active != target_total:
        print(f"Warning at time {current_time}: active total = {total_active}, expected {target_total}")

    schedule.append({
        "Time": format_time(current_time),
        "New Bronze Jobs (30 min)": "\n".join(new_bronze),
        "New Silver Jobs (60 min)": "\n".join(new_silver),
        "New Gold Jobs (120 min)": "\n".join(new_gold),
        "Total New Jobs": len(new_bronze) + len(new_silver) + len(new_gold)
    })

df = pd.DataFrame(schedule)
output_file = "job_schedule_new_jobs_only.xlsx"
df.to_excel(output_file, index=False)
print(f"Excel file created: {output_file}")

import asyncio
import random

async def fetch_data(task_id: int):
    print(f"Task {task_id}: Fetching data...")
    await asyncio.sleep(random.uniform(1, 3))  # จำลองเวลาโหลดข้อมูล
    print(f"Task {task_id}: Data fetched")
    return f"Data from task {task_id}"

async def main():
    tasks = [fetch_data(i) for i in range(5)]
    results = await asyncio.gather(*tasks)
    print("All tasks completed:", results)

if __name__ == "__main__":
    asyncio.run(main())

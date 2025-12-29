import pandas as pd
import matplotlib.pyplot as plt

def plot_results():
    # 1. Read the CSV
    try:
        df = pd.read_csv("analysis_results.csv")
    except FileNotFoundError:
        print("❌ Error: analysis_results.csv not found. Run benchmark_driver.py first.")
        return

    # 2. Setup the Plot Style
    plt.style.use('bmh') 
    
    # Get unique algorithms
    algorithms = df['Algorithm'].unique()
    
    # --- GRAPH 1: EXECUTION TIME ---
    plt.figure(figsize=(10, 6))
    for algo in algorithms:
        subset = df[df['Algorithm'] == algo]
        plt.plot(subset['Input_Size'], subset['Time_ms'], marker='o', label=algo)
    
    plt.title('Algorithm Execution Time Analysis', fontsize=14)
    plt.xlabel('Input Size (N)', fontsize=12)
    plt.ylabel('Time (milliseconds)', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.savefig('graph_time_complexity.png')
    print("✅ Saved graph_time_complexity.png")
    
    # --- GRAPH 2: MEMORY USAGE ---
    plt.figure(figsize=(10, 6))
    for algo in algorithms:
        subset = df[df['Algorithm'] == algo]
        plt.plot(subset['Input_Size'], subset['Memory_KB'], marker='s', linestyle='--', label=algo)
    
    plt.title('Algorithm Memory Usage Analysis', fontsize=14)
    plt.xlabel('Input Size (N)', fontsize=12)
    plt.ylabel('Peak Memory (KB)', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.savefig('graph_memory_usage.png')
    print("✅ Saved graph_memory_usage.png")

if __name__ == "__main__":
    plot_results()
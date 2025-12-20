# 📊 Advanced Sorting Algorithms Benchmark
> **MSc Course Project - Advanced Algorithms**  
> **Faculty of Computers and Artificial Intelligence - Cairo University**

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-Educational-green?style=for-the-badge)

## 🧐 Project Objective
This project performs a comparative analysis of 5 fundamental sorting algorithms based on **Execution Time** and **Memory Usage**. The goal is to understand the trade-offs between comparison-based sorts and distribution-based sorts under randomized, sorted, and sparse data distributions.

## 🚀 Algorithms Implemented

| Algorithm | Type | Strategy | Complexity (Avg) | Special Implementation Note |
| :--- | :--- | :--- | :--- | :--- |
| **Quick Sort** | Comparison | Divide & Conquer | $O(N \log N)$ | Uses **Randomized Pivot** to avoid $O(N^2)$ worst-case. |
| **Heap Sort** | Comparison | Binary Heap | $O(N \log N)$ | Implemented **In-Place** ($O(1)$ Aux Space). |
| **Count Sort** | Distribution | Frequency Count | $O(N + K)$ | Extremely fast for small integer ranges. |
| **Radix Sort** | Distribution | Digit-by-Digit | $O(NK)$ | Stable sort for large integers. |
| **Bucket Sort** | Distribution | Scatter-Gather | $O(N + K)$ | Optimized for uniform float distributions $[0, 1)$. |

## 📂 Project Structure

```text
Advanced_Algorithms_MSc/
├── algorithms/             # Source code for sorting logic
│   ├── quick_sort.py       # Randomized Quick Sort
│   ├── heap_sort.py        # Iterative Max-Heap Sort
│   ├── count_sort.py       # Counting Sort
│   ├── radix_sort.py       # (Coming Soon)
│   └── bucket_sort.py      # (Coming Soon)
├── data_generator.py       # Factory for Random, Sorted, and Float datasets
├── test_integration.py     # Unit testing script to verify correctness
├── benchmark_driver.py     # Main script for Time/Memory analysis
└── .gitignore              # Configurations to ignore unnecessary files
```
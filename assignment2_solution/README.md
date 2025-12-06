# Student Performance Analysis System

## 📋 Project Overview

This project is a comprehensive **Student Performance Analysis System** designed to analyze student academic performance across multiple university campuses. The system processes student data from multiple campus files, calculates performance metrics, identifies at-risk students, and generates detailed analytical reports.

## 🎯 Features

- **Multi-Campus Data Processing**: Automatically processes data from multiple campus files (CMP*.txt)
- **Performance Metrics**: Calculates average marks for four core subjects:
  - Programming
  - Database
  - Systems Analysis
  - Networking
- **At-Risk Student Identification**: Identifies students with overall average below 50%
- **Campus-Wise Summaries**: Generates individual summary reports for each campus
- **Comprehensive Academic Report**: Creates an institute-wide performance analysis report
- **Keyword Search**: Interactive search feature to query the academic report
- **Automated File Discovery**: Intelligently locates campus data files in multiple directory structures

## 📁 Project Structure

```
assignment2_solution/
│
├── code/
│   └── student_performance_analysis.py    # Main Python script
│
├── campus_data/
│   ├── CMP001.txt                         # Campus 1 student data
│   ├── CMP002.txt                         # Campus 2 student data
│   └── CMP003.txt                         # Campus 3 student data
│
├── output_files/
│   ├── CMP001_summary.txt                 # Campus 1 summary report
│   ├── CMP002_summary.txt                 # Campus 2 summary report
│   ├── CMP003_summary.txt                 # Campus 3 summary report
│   └── academic_performance_report.txt    # Institute-wide report
│
├── Assignment_Report.pdf                  # Assignment documentation
├── README.md                              # This file
└── requirements.txt                       # Python dependencies
```

## 🔧 Installation & Setup

### Prerequisites

- Python 3.6 or higher
- No external libraries required (uses only Python standard library)

### Installation Steps

1. **Clone or download the project**:
   ```bash
   cd /path/to/assignment2_solution
   ```

2. **Verify Python installation**:
   ```bash
   python --version
   # or
   python3 --version
   ```

3. **No additional dependencies needed** - This project uses only Python's built-in libraries!

## 🚀 Running the Project

### Method 1: Running from the `code` directory

```bash
cd code
python student_performance_analysis.py
```

### Method 2: Running from the project root

```bash
python code/student_performance_analysis.py
```

### Method 3: Running as a module

```bash
python -m code.student_performance_analysis
```

## 📊 Input Data Format

Each campus data file (e.g., `CMP001.txt`) should contain student records in the following format:

```
<programming_mark> <database_mark> <systems_analysis_mark> <networking_mark> <student_id>
```

**Example**:
```
85.5 78.0 92.0 88.5 STU001
45.0 38.5 42.0 48.5 STU002
72.5 68.0 75.5 70.0 STU003
```

### Data Requirements:
- Each line represents one student
- Five space-separated values per line
- First four values are numeric marks (float or int)
- Last value is the student ID (string)
- Marks should be between 0 and 100

## 📤 Output Files

### 1. Campus Summary Files (`CMP*_summary.txt`)

Generated for each campus, containing:
- Campus code
- Average marks for each subject
- List of at-risk students (average < 50)

**Example Output**:
```
Campus Code: CMP001
Average Programming Mark: 67.5
Average Database Mark: 61.5
Average Systems Analysis Mark: 69.8
Average Networking Mark: 69.0
Students At Risk (Average < 50):
STU002
```

### 2. Academic Performance Report (`academic_performance_report.txt`)

Comprehensive institute-wide report including:
- Summary statistics (total campuses, students, at-risk students)
- Overall subject trends and averages
- Strongest and weakest subjects
- Performance distribution percentages
- Campus-wise breakdown
- Actionable recommendations for improvement

## 🎓 Running in Jupyter Notebook

### Setup Instructions

1. **Install Jupyter Notebook** (if not already installed):
   ```bash
   pip install jupyter notebook
   ```

2. **Create a new notebook**:
   ```bash
   cd /path/to/assignment2_solution
   jupyter notebook
   ```

3. **In the Jupyter Notebook**, create a new Python 3 notebook and run:

   ```python
   # Cell 1: Import the script functions
   import sys
   import os
   
   # Add the code directory to the path
   sys.path.append(os.path.join(os.getcwd(), 'code'))
   
   from student_performance_analysis import *
   
   # Cell 2: Run the analysis
   print("="*60)
   print("STUDENT PERFORMANCE ANALYSIS SYSTEM")
   print("="*60)
   
   # Process all campuses
   all_data = process_all_campuses()
   
   # Cell 3: Generate the academic report
   if all_data:
       report_file = generate_academic_report(all_data)
       print(f"\nReport generated: {report_file}")
   
   # Cell 4: (Optional) View specific campus data
   if all_data:
       for campus in all_data['campuses']:
           print(f"\n{campus['code']}:")
           print(f"  Total Students: {len(campus['students'])}")
           print(f"  At-Risk Students: {len(campus['at_risk'])}")
           print(f"  Programming Avg: {campus['averages']['programming']:.2f}")
   ```

4. **For interactive keyword search** (in a separate cell):
   ```python
   # Note: This will create an interactive input prompt
   if all_data:
       keyword_search("output_files/academic_performance_report.txt")
   ```

## ☁️ Running in Google Colab

### Setup Instructions

1. **Open Google Colab**: Go to [https://colab.research.google.com/](https://colab.research.google.com/)

2. **Create a new notebook**

3. **Upload the project files**:

   ```python
   # Cell 1: Upload files
   from google.colab import files
   import os
   
   # Create directory structure
   os.makedirs('code', exist_ok=True)
   os.makedirs('campus_data', exist_ok=True)
   os.makedirs('output_files', exist_ok=True)
   
   print("Please upload the following files:")
   print("1. student_performance_analysis.py (to code/)")
   print("2. CMP001.txt, CMP002.txt, CMP003.txt (to campus_data/)")
   
   # Upload the Python script
   uploaded = files.upload()
   
   # Move uploaded files to appropriate directories
   for filename in uploaded.keys():
       if filename.endswith('.py'):
           os.rename(filename, f'code/{filename}')
       elif filename.startswith('CMP') and filename.endswith('.txt'):
           os.rename(filename, f'campus_data/{filename}')
   ```

4. **Alternative: Clone from GitHub** (if you have the project on GitHub):

   ```python
   # Cell 1: Clone repository
   !git clone https://github.com/yourusername/assignment2_solution.git
   %cd assignment2_solution
   ```

5. **Run the analysis**:

   ```python
   # Cell 2: Import and run
   import sys
   sys.path.append('code')
   
   from student_performance_analysis import *
   
   # Process all campuses
   all_data = process_all_campuses()
   
   # Generate report
   if all_data:
       report_file = generate_academic_report(all_data)
   ```

6. **Download output files**:

   ```python
   # Cell 3: Download results
   from google.colab import files
   import glob
   
   # Download all summary files
   for file in glob.glob('output_files/*.txt'):
       files.download(file)
   ```

7. **View results in Colab**:

   ```python
   # Cell 4: Display the academic report
   with open('output_files/academic_performance_report.txt', 'r') as f:
       print(f.read())
   ```

## 🔍 Usage Examples

### Example 1: Basic Analysis

```python
from student_performance_analysis import *

# Run complete analysis
all_data = process_all_campuses()
if all_data:
    generate_academic_report(all_data)
```

### Example 2: Analyze Specific Campus

```python
from student_performance_analysis import *

# Load data from a specific campus
students = load_campus_data('campus_data/CMP001.txt')

# Calculate averages
averages = calculate_subject_averages(students)
print(f"Programming Average: {averages['programming']:.2f}")

# Find at-risk students
at_risk = identify_at_risk_students(students)
print(f"At-Risk Students: {at_risk}")
```

### Example 3: Custom Analysis

```python
from student_performance_analysis import *

# Load all campus data
all_data = process_all_campuses()

# Find the campus with the highest at-risk percentage
if all_data:
    max_risk_campus = None
    max_risk_pct = 0
    
    for campus in all_data['campuses']:
        risk_pct = len(campus['at_risk']) / len(campus['students']) * 100
        if risk_pct > max_risk_pct:
            max_risk_pct = risk_pct
            max_risk_campus = campus['code']
    
    print(f"Campus with highest at-risk percentage: {max_risk_campus} ({max_risk_pct:.2f}%)")
```

## 🛠️ Key Functions

| Function | Description |
|----------|-------------|
| `load_campus_data(file_name)` | Loads student data from a campus file |
| `calculate_subject_averages(students)` | Calculates average marks for each subject |
| `identify_at_risk_students(students)` | Identifies students with average < 50 |
| `generate_campus_summary(...)` | Generates summary file for a campus |
| `process_all_campuses()` | Processes all campus files and returns aggregated data |
| `generate_academic_report(all_data)` | Generates comprehensive academic performance report |
| `keyword_search(filename)` | Interactive keyword search in the report |
| `main()` | Main orchestration function |

## 🐛 Troubleshooting

### Issue: "No campus files found"

**Solution**: Ensure campus data files are in one of these locations:
- Current directory
- `./campus_data/`
- `../campus_data/`

### Issue: "Invalid data format"

**Solution**: Verify that each line in campus files has exactly 5 space-separated values.

### Issue: Module import errors in Jupyter/Colab

**Solution**: Make sure to add the code directory to the Python path:
```python
import sys
sys.path.append('code')
```

### Issue: Permission errors when writing output files

**Solution**: Ensure you have write permissions in the output directory, or run from a directory where you have write access.

## 📝 Notes

- The system automatically detects campus files matching the pattern `CMP*.txt`
- Output files are generated in the `output_files/` directory if it exists, otherwise in the current directory
- The keyword search feature is interactive and requires user input (may not work well in some Jupyter environments)
- All calculations use floating-point arithmetic for precision

## 👨‍💻 Author

This project was created as part of Assignment 2 - Student Performance Analysis System.

## 📄 License

This project is created for educational purposes.

## 🤝 Contributing

This is an assignment project. If you have suggestions for improvements, feel free to create an issue or submit a pull request.

---

**Last Updated**: December 2025

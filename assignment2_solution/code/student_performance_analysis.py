import os
import glob

# Load student data from a campus file.
def load_campus_data(file_name):
    students = []
    
    try:
        with open(file_name, 'r') as file:

            for line in file:
                # Split the line and extract marks and student ID
                parts = line.strip().split()
                
                if len(parts) == 5:
                    student = {
                        'programming': float(parts[0]),
                        'database': float(parts[1]),
                        'systems_analysis': float(parts[2]),
                        'networking': float(parts[3]),
                        'student_id': parts[4]
                    }

                    students.append(student)


    except FileNotFoundError:
        print(f"Error: File {file_name} not found.")

    except ValueError:
        print(f"Error: Invalid data format in {file_name}.")

    
    return students




# Calculate average marks for each subject
def calculate_subject_averages(students):
   
    if not students:
        return {
            'programming': 0.0,
            'database': 0.0,
            'systems_analysis': 0.0,
            'networking': 0.0
        }
    
    total_students = len(students)

    averages = {
        'programming': sum(s['programming'] for s in students) / total_students,
        'database': sum(s['database'] for s in students) / total_students,
        'systems_analysis': sum(s['systems_analysis'] for s in students) / total_students,
        'networking': sum(s['networking'] for s in students) / total_students
    }
    
    return averages


# Identify students with overall average below 50
def identify_at_risk_students(students):
    
    at_risk = []
    
    for student in students:

        # Calculate overall average 
        overall_avg = (
            student['programming'] +
            student['database'] +
            student['systems_analysis'] +
            student['networking']
        ) / 4.0
        
        if overall_avg < 50:
            at_risk.append(student['student_id'])
    
    return at_risk




# Generate summary file for a campus
def generate_campus_summary(campus_code, averages, at_risk_students, output_dir="."):
    
    summary_filename = os.path.join(output_dir, f"{campus_code}_summary.txt")

    
    with open(summary_filename, 'w') as file:
        file.write(f"Campus Code: {campus_code}\n")
        file.write(f"Average Programming Mark: {averages['programming']:.1f}\n")
        file.write(f"Average Database Mark: {averages['database']:.1f}\n")
        file.write(f"Average Systems Analysis Mark: {averages['systems_analysis']:.1f}\n")
        file.write(f"Average Networking Mark: {averages['networking']:.1f}\n")
        file.write(f"Students At Risk (Average < 50):\n")

        
        if at_risk_students:

            for student_id in at_risk_students:
                file.write(f"{student_id}\n")
        else:
            file.write("None\n")

    
    print(f"Generated summary: {summary_filename}")





# Find campus data files in campus data directories
def find_campus_files():
    
    # First, try current directory
    campus_files = glob.glob("CMP*.txt")
    data_dir = "."
    
    # If not found, try campus_data subdirectory
    if not campus_files and os.path.isdir("../campus_data"):
        campus_files = glob.glob("../campus_data/CMP*.txt")
        data_dir = "../campus_data"

    
    # Try campus_data in current directory
    if not campus_files and os.path.isdir("campus_data"):
        campus_files = glob.glob("campus_data/CMP*.txt")
        data_dir = "campus_data"

    
    return campus_files, data_dir





#  Process all campus data files and generate campus data summaries
def process_all_campuses():
    
    # Find all campus files
    campus_files, data_dir = find_campus_files()
    
    if not campus_files:
        print("No campus files found in the current directory or campus_data folder.")
        print("\nPlease ensure CMP*.txt files are in one of these locations:")
        print("  1. Current directory")
        print("  2. ./campus_data/")
        print("  3. ../campus_data/")
        return None
    

    
    # Determine output directory
    output_dir = "."

    if os.path.isdir("../output_files"):
        output_dir = "../output_files"

    elif os.path.isdir("output_files"):
        output_dir = "output_files"

    
    all_data = {
        'campuses': [],
        'total_students': 0,
        'total_at_risk': 0,
        'all_students': []
    }

    
    print(f"\n{'='*60}")
    print(f"Processing {len(campus_files)} campus(es)...")
    print(f"Data directory: {data_dir}")
    print(f"Output directory: {output_dir}")
    print(f"{'='*60}\n")


    
    for campus_file in sorted(campus_files):

        # Extract campus code from filename (e.g., CMP001 from CMP001.txt)
        campus_code = os.path.splitext(os.path.basename(campus_file))[0]
        
        print(f"Processing {campus_code}...")
        
        # Load student data
        students = load_campus_data(campus_file)
        

        if not students:
            print(f" No valid data found in {campus_file}")
            continue
        
        
        # Calculate averages
        averages = calculate_subject_averages(students)
        
        # Identify at-risk students
        at_risk = identify_at_risk_students(students)
        
        # Generate summary file
        generate_campus_summary(campus_code, averages, at_risk, output_dir)
        
        # Store campus data
        campus_data = {
            'code': campus_code,
            'students': students,
            'averages': averages,
            'at_risk': at_risk
        }

        all_data['campuses'].append(campus_data)
        all_data['total_students'] += len(students)
        all_data['total_at_risk'] += len(at_risk)
        all_data['all_students'].extend(students)

        
        print(f" Students: {len(students)}, At Risk: {len(at_risk)}\n")
    
    return all_data





# Generate comprehensive academic performance report
def generate_academic_report(all_data):

    if not all_data or not all_data['campuses']:
        print("No data available to generate report.")
        return
    
    
    # Determine output directory
    output_dir = "."
    if os.path.isdir("../output_files"):
        output_dir = "../output_files"
    elif os.path.isdir("output_files"):
        output_dir = "output_files"
    

    # Calculate institute-wide statistics
    total_campuses = len(all_data['campuses'])
    total_students = all_data['total_students']
    total_at_risk = all_data['total_at_risk']
    

    # Calculate overall subject averages
    overall_averages = calculate_subject_averages(all_data['all_students'])
    
    # Calculate percentages
    at_risk_percentage = (total_at_risk / total_students * 100) if total_students > 0 else 0
    high_performer_percentage = 100 - at_risk_percentage
    
    # Generate report file
    report_filename = os.path.join(output_dir, "academic_performance_report.txt")
    



    with open(report_filename, 'w') as file:
        file.write("="*70 + "\n")
        file.write("ACADEMIC PERFORMANCE ANALYSIS REPORT\n")
        file.write("="*70 + "\n\n")

        
        # Purpose
        file.write("PURPOSE OF ANALYSIS:\n")
        file.write("-" * 70 + "\n")
        file.write("This report analyzes student performance across multiple university\n")
        file.write("campuses to identify academic trends, at-risk students, and provide\n")
        file.write("data-driven recommendations for improving educational outcomes.\n\n")

        
        # Summary Statistics
        file.write("SUMMARY STATISTICS:\n")
        file.write("-" * 70 + "\n")
        file.write(f"Total Number of Campuses Processed: {total_campuses}\n")
        file.write(f"Total Students Processed: {total_students}\n")
        file.write(f"Total At-Risk Students: {total_at_risk}\n\n")

        
        # Overall Subject Trends
        file.write("OVERALL SUBJECT TRENDS:\n")
        file.write("-" * 70 + "\n")
        file.write(f"Average Programming Mark: {overall_averages['programming']:.2f}\n")
        file.write(f"Average Database Mark: {overall_averages['database']:.2f}\n")
        file.write(f"Average Systems Analysis Mark: {overall_averages['systems_analysis']:.2f}\n")
        file.write(f"Average Networking Mark: {overall_averages['networking']:.2f}\n\n")

        
        # Identify strongest and weakest subjects
        subject_scores = {
            'Programming': overall_averages['programming'],
            'Database': overall_averages['database'],
            'Systems Analysis': overall_averages['systems_analysis'],
            'Networking': overall_averages['networking']
        }
        strongest = max(subject_scores, key=subject_scores.get)
        weakest = min(subject_scores, key=subject_scores.get)

        
        file.write(f"Strongest Subject: {strongest} ({subject_scores[strongest]:.2f})\n")
        file.write(f"Weakest Subject: {weakest} ({subject_scores[weakest]:.2f})\n\n")

        
        # Performance Distribution
        file.write("PERFORMANCE DISTRIBUTION:\n")
        file.write("-" * 70 + "\n")
        file.write(f"Institute-wide High-Performer Percentage: {high_performer_percentage:.2f}%\n")
        file.write(f"Institute-wide At-Risk Percentage: {at_risk_percentage:.2f}%\n\n")


        
        # Campus-wise Breakdown
        file.write("CAMPUS-WISE BREAKDOWN:\n")
        file.write("-" * 70 + "\n")

        for campus in all_data['campuses']:
            campus_at_risk_pct = (len(campus['at_risk']) / len(campus['students']) * 100) if len(campus['students']) > 0 else 0
            file.write(f"{campus['code']}: {len(campus['students'])} students, ")
            file.write(f"{len(campus['at_risk'])} at risk ({campus_at_risk_pct:.1f}%)\n")
            
        file.write("\n")
        

        # Recommendations
        file.write("RECOMMENDATIONS:\n")
        file.write("-" * 70 + "\n")
        file.write("1. IMMEDIATE INTERVENTION:\n")
        file.write(f"   - Provide targeted support to {total_at_risk} at-risk students\n")
        file.write("   - Implement peer tutoring programs\n")
        file.write("   - Offer additional office hours for struggling students\n\n")
        

        file.write("2. CURRICULUM ENHANCEMENT:\n")
        file.write(f"   - Strengthen {weakest} curriculum and teaching methods\n")
        file.write("   - Share best practices from high-performing subjects\n")
        file.write("   - Introduce more practical, hands-on learning activities\n\n")

        
        file.write("3. MONITORING AND ASSESSMENT:\n")
        file.write("   - Implement early warning systems for struggling students\n")
        file.write("   - Conduct regular progress assessments\n")
        file.write("   - Establish feedback mechanisms for continuous improvement\n\n")

        
        file.write("4. RESOURCE ALLOCATION:\n")
        file.write("   - Allocate additional resources to campuses with higher at-risk rates\n")
        file.write("   - Invest in learning management systems and online resources\n")
        file.write("   - Provide professional development for faculty\n\n")
        

        file.write("="*70 + "\n")
        file.write("End of Report\n")
        file.write("="*70 + "\n")

    
    print(f"Generated academic report: {report_filename}")

    return report_filename





# Interactive keyword search in the academic report
def keyword_search(filename):

    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        print(f"\n{'='*60}")
        print("KEYWORD SEARCH FEATURE")
        print(f"{'='*60}")
        print(f"Searching in: {filename}")
        print("Type 'exit' to quit the search.\n")

        
        while True:
            keyword = input("Enter keyword to search: ").strip()
            
            if keyword.lower() == 'exit':
                print("Exiting search...")
                break
            
            if not keyword:
                print("Please enter a valid keyword.\n")
                continue

            
            # Case-insensitive search
            count = content.lower().count(keyword.lower())

            print(f"Keyword '{keyword}' found {count} times.\n")

    
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")








# Main function to orchestrate the entire analysis process
def main():
    
    print("\n" + "="*60)
    print("STUDENT PERFORMANCE ANALYSIS SYSTEM")
    print("="*60)

    
    # Load and process all campus data files
    all_data = process_all_campuses()
    
    if not all_data:
        print("\nNo data to process. Exiting...")
        return
    

    
    # Generate academic performance report
    print(f"\n{'='*60}")
    print("Generating Academic Performance Report...")
    print(f"{'='*60}\n")
    report_file = generate_academic_report(all_data)


    
    # Keyword search feature
    if report_file:
        keyword_search(report_file)


    
    print(f"\n{'='*60}")
    print("Analysis Complete!")
    print(f"{'='*60}")
    print("\nGenerated Files:")
    print("  - Campus summary files: CMP*_summary.txt")
    print("  - Academic report: academic_performance_report.txt")
    print(f"{'='*60}\n")




if __name__ == "__main__":
    main()

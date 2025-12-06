# ICT702 - Assignment Solutions Repository

This repository contains comprehensive solutions for **ICT702 (Introduction to Relational Database)** course assignments, including both programming and database design projects.

---

## 📚 Repository Contents

This repository includes solutions for **two major assignments**:

1. **[Assignment 2 - Student Performance Analysis System](#assignment-2---student-performance-analysis-system)** (Programming)
2. **[Database Design Assignment - Football Tournament Management](#database-design-assignment---football-tournament-management)** (Database Design)

---

## 📁 Repository Structure

```
faisal/
│
├── assignment2_solution/              # Student Performance Analysis System
│   ├── code/
│   │   └── student_performance_analysis.py
│   ├── campus_data/
│   │   ├── CMP001.txt
│   │   ├── CMP002.txt
│   │   └── CMP003.txt
│   ├── output_files/
│   │   ├── CMP*_summary.txt
│   │   └── academic_performance_report.txt
│   ├── README.md                      # Detailed project documentation
│   ├── COLAB_SETUP.md                 # Google Colab setup guide
│   └── requirements.txt
│
├── ict702_assignment/                 # Football Tournament Database Design
│   ├── ICT702_Assignment2_Football_Tournament_Solution.md
│   ├── ICT702_Assignment2_Football_Tournament_Solution.docx
│   ├── football_tournament_er_diagram.png
│   └── football_tournament_er_diagram_mermaid.md
│
├── ICT702-Assessment 2 (Draft)-T3-25 Week 6.pdf
├── Student_Performance_Analysis_Colab.ipynb
└── README.md                          # This file
```

---

## 🎯 Assignment 2 - Student Performance Analysis System

### Overview

A comprehensive **Python-based Student Performance Analysis System** designed to analyze student academic performance across multiple university campuses. The system processes student data, calculates performance metrics, identifies at-risk students, and generates detailed analytical reports.

### Key Features

- ✅ **Multi-Campus Data Processing**: Automatically processes data from multiple campus files (CMP*.txt)
- ✅ **Performance Metrics**: Calculates average marks for four core subjects (Programming, Database, Systems Analysis, Networking)
- ✅ **At-Risk Student Identification**: Identifies students with overall average below 50%
- ✅ **Campus-Wise Summaries**: Generates individual summary reports for each campus
- ✅ **Comprehensive Academic Report**: Creates an institute-wide performance analysis report
- ✅ **Keyword Search**: Interactive search feature to query the academic report
- ✅ **Automated File Discovery**: Intelligently locates campus data files

### Technologies Used

- **Language**: Python 3.6+
- **Libraries**: Standard Python libraries only (no external dependencies)
- **Platforms**: Local Python, Jupyter Notebook, Google Colab

### Quick Start

```bash
# Navigate to the project directory
cd assignment2_solution/code

# Run the analysis
python student_performance_analysis.py
```

### Sample Results

**Total Statistics:**
- Campuses: 3
- Students: 30
- At-Risk: 8 (26.67%)
- High Performers: 73.33%

**Subject Averages:**
- Programming: 68.67
- Database: 70.57
- Systems Analysis: 69.52
- Networking: 71.18 (Strongest)

### Documentation

📖 **Detailed Documentation**: [assignment2_solution/README.md](assignment2_solution/README.md)  
☁️ **Google Colab Guide**: [assignment2_solution/COLAB_SETUP.md](assignment2_solution/COLAB_SETUP.md)  
📓 **Jupyter Notebook**: [Student_Performance_Analysis_Colab.ipynb](Student_Performance_Analysis_Colab.ipynb)

---

## 🗄️ Database Design Assignment - Football Tournament Management

### Overview

A comprehensive **Entity-Relationship (ER) database design** for a Football Tournament Management System. This assignment demonstrates advanced database modeling concepts including normalization, specialization hierarchies, weak entities, and complex relationships.

### Key Features

- ✅ **12 Entities**: Exactly 12 entities as required (Tournament, Team, Player, Match, Venue, etc.)
- ✅ **Specialization Hierarchy**: Player → {Goalkeeper, FieldPlayer} (Disjoint subtypes)
- ✅ **Weak Entity**: MatchEvent with composite primary key
- ✅ **Composite & Surrogate Keys**: Both key types implemented
- ✅ **Multiple Data Types**: Numeric, Varchar, and Date fields
- ✅ **Normalized Design**: 3NF achieved with junction tables for M:N relationships
- ✅ **Complete Documentation**: All 8 required sections included

### Database Schema Highlights

#### Entities (12 Total)

**Core Entities:**
1. Tournament
2. Team
3. Player (Supertype)
4. Match
5. Venue

**Specialized Entities:**
6. Goalkeeper (Subtype - Disjoint)
7. FieldPlayer (Subtype - Disjoint)

**Supporting Entities:**
8. Official
9. Sponsor
10. MedicalStaff
11. Coach

**Weak Entity:**
12. MatchEvent (Dependent on Match)

#### Relationships

- **1:1 Relationships**: Coach ↔ Team
- **1:N Relationships**: Tournament → Team, Team → Player, Venue → Match, etc.
- **M:N Relationships**: Sponsor ↔ Tournament/Team/Player (with junction tables)

#### Key Design Features

**Specialization Hierarchy (Disjoint):**
```
Player (Supertype)
├── Goalkeeper (Subtype)
└── FieldPlayer (Subtype)
```

**Weak Entity:**
- **MatchEvent** depends on Match
- Composite Primary Key: (MatchID, EventSequence)

**Normalization:**
- All entities in 3NF (Third Normal Form)
- M:N relationships resolved with junction tables:
  - TournamentSponsor
  - TeamSponsor
  - PlayerSponsor

### Deliverables

📄 **Word Document**: [ict702_assignment/ICT702_Assignment2_Football_Tournament_Solution.docx](ict702_assignment/ICT702_Assignment2_Football_Tournament_Solution.docx)  
📝 **Markdown Version**: [ict702_assignment/ICT702_Assignment2_Football_Tournament_Solution.md](ict702_assignment/ICT702_Assignment2_Football_Tournament_Solution.md)  
🖼️ **ER Diagram (PNG)**: [ict702_assignment/football_tournament_er_diagram.png](ict702_assignment/football_tournament_er_diagram.png)  
📊 **Mermaid Diagram**: [ict702_assignment/football_tournament_er_diagram_mermaid.md](ict702_assignment/football_tournament_er_diagram_mermaid.md)

### Assignment Requirements Met

| Requirement | Status | Implementation |
|-------------|--------|----------------|
| 10-12 entities | ✅ | Exactly 12 entities |
| Unique scenario | ✅ | Football Tournament Management |
| Specialization hierarchy | ✅ | Player → {Goalkeeper, FieldPlayer} (Disjoint) |
| Composite primary key | ✅ | MatchEvent (MatchID, EventSequence) |
| Surrogate primary key | ✅ | 9 entities with auto-generated IDs |
| Numeric field | ✅ | Multiple (IDs, scores, statistics) |
| Varchar field | ✅ | Multiple (names, descriptions) |
| Date field | ✅ | Multiple (dates, timestamps) |
| Weak entity | ✅ | MatchEvent (dependent on Match) |
| Normalized | ✅ | 3NF, M:N resolved |

---

## 🚀 Getting Started

### Prerequisites

**For Student Performance Analysis:**
- Python 3.6 or higher
- No external libraries required

**For Database Design:**
- Word processor (to view .docx file)
- Markdown viewer (optional)
- Mermaid diagram viewer (optional)

### Installation

1. **Clone or download this repository**:
   ```bash
   git clone <repository-url>
   cd faisal
   ```

2. **For Student Performance Analysis**:
   ```bash
   cd assignment2_solution
   python code/student_performance_analysis.py
   ```

3. **For Database Design**:
   - Open `ict702_assignment/ICT702_Assignment2_Football_Tournament_Solution.docx`
   - Or view the markdown version in any markdown viewer

---

## 📖 Documentation

### Student Performance Analysis System
- **Main README**: [assignment2_solution/README.md](assignment2_solution/README.md)
- **Google Colab Setup**: [assignment2_solution/COLAB_SETUP.md](assignment2_solution/COLAB_SETUP.md)
- **Jupyter Notebook**: [Student_Performance_Analysis_Colab.ipynb](Student_Performance_Analysis_Colab.ipynb)

### Football Tournament Database Design
- **Complete Assignment Document**: [ict702_assignment/ICT702_Assignment2_Football_Tournament_Solution.md](ict702_assignment/ICT702_Assignment2_Football_Tournament_Solution.md)
- **Word Document (Submission)**: [ict702_assignment/ICT702_Assignment2_Football_Tournament_Solution.docx](ict702_assignment/ICT702_Assignment2_Football_Tournament_Solution.docx)
- **ER Diagram Visual**: [ict702_assignment/football_tournament_er_diagram.png](ict702_assignment/football_tournament_er_diagram.png)
- **Mermaid Schema**: [ict702_assignment/football_tournament_er_diagram_mermaid.md](ict702_assignment/football_tournament_er_diagram_mermaid.md)

---

## 🎓 Course Information

**Course**: ICT702 - Introduction to Relational Database  
**Institution**: [Your Institution]  
**Semester**: T3-25  
**Due Date**: Sunday, 7/12/2025 23:59

---

## 📊 Assignment Breakdown

### Assignment 2 - Student Performance Analysis (Programming)
- **Weight**: 20 marks
- **Type**: Python programming assignment
- **Focus**: File processing, data analysis, report generation
- **Deliverables**: Python code, output files, documentation

### Database Design Assignment (ER Modeling)
- **Weight**: 10% of course mark
- **Type**: Database design assignment
- **Focus**: ER modeling, normalization, database design principles
- **Deliverables**: Case study, ER diagram, complete documentation

---

## ✅ Features Summary

### Student Performance Analysis System
- Multi-campus data processing
- Statistical analysis and reporting
- At-risk student identification
- Interactive keyword search
- Automated file discovery
- Professional report generation

### Football Tournament Database Design
- Comprehensive ER diagram with 12 entities
- Specialization hierarchy (disjoint subtypes)
- Weak entity with composite key
- Normalized to 3NF
- Complete relationship documentation
- Professional Word document for submission

---

## 🛠️ Technologies & Tools

### Programming Assignment
- **Python 3.6+**: Core programming language
- **Standard Libraries**: os, glob, sys (no external dependencies)
- **Jupyter Notebook**: Interactive development
- **Google Colab**: Cloud-based execution

### Database Design Assignment
- **Markdown**: Documentation format
- **Microsoft Word**: Submission format
- **Mermaid**: ER diagram visualization
- **Pandoc**: Document conversion

---

## 📝 Submission Guidelines

### Student Performance Analysis
1. Zip the entire `assignment2_solution` folder
2. Include assignment report with:
   - Cover page
   - Implementation explanation
   - Test cases and results
   - Screenshots of output
3. Submit the zip file via course portal

### Database Design Assignment
1. Review the Word document
2. Add your name and student ID
3. Ensure ER diagram is embedded
4. Submit `.docx` file via course portal by deadline

---

## 🐛 Troubleshooting

### Student Performance Analysis
- **Issue**: "No campus files found"
  - **Solution**: Ensure campus data files are in `campus_data/` directory
  
- **Issue**: Module import errors
  - **Solution**: Add code directory to Python path: `sys.path.append('code')`

### Database Design
- **Issue**: Word document won't open
  - **Solution**: Use the markdown version or Google Docs to view

---

## 👨‍💻 Author

**Student Name**: [Your Name]  
**Student ID**: [Your ID]  
**Course**: ICT702 - Introduction to Relational Database

---

## 📄 License

These projects are created for educational purposes as part of ICT702 course assignments.

---

## 🤝 Acknowledgments

- Course instructors and teaching staff
- ICT702 course materials and resources
- Python documentation and community

---

## 📞 Support

For questions or issues:
1. Review the detailed README files in each project directory
2. Check the assignment specification documents
3. Contact course teaching staff

---

**Last Updated**: December 6, 2025

---

## 🎯 Quick Links

| Resource | Link |
|----------|------|
| **Student Performance Analysis README** | [assignment2_solution/README.md](assignment2_solution/README.md) |
| **Google Colab Setup Guide** | [assignment2_solution/COLAB_SETUP.md](assignment2_solution/COLAB_SETUP.md) |
| **Database Design Document (Word)** | [ict702_assignment/ICT702_Assignment2_Football_Tournament_Solution.docx](ict702_assignment/ICT702_Assignment2_Football_Tournament_Solution.docx) |
| **Database Design Document (Markdown)** | [ict702_assignment/ICT702_Assignment2_Football_Tournament_Solution.md](ict702_assignment/ICT702_Assignment2_Football_Tournament_Solution.md) |
| **ER Diagram (PNG)** | [ict702_assignment/football_tournament_er_diagram.png](ict702_assignment/football_tournament_er_diagram.png) |
| **Mermaid ER Diagram** | [ict702_assignment/football_tournament_er_diagram_mermaid.md](ict702_assignment/football_tournament_er_diagram_mermaid.md) |
| **Assignment Specification** | [ICT702-Assessment 2 (Draft)-T3-25 Week 6.pdf](ICT702-Assessment%202%20(Draft)-T3-25%20Week%206.pdf) |

---

**Status**: ✅ Both assignments complete and ready for submission

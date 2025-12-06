# Football Tournament Management System - ER Diagram (Mermaid)

## Mermaid ER Diagram Schema

```mermaid
erDiagram
    TOURNAMENT ||--o{ TEAM : "organizes"
    TOURNAMENT ||--o{ MATCH : "schedules"
    TOURNAMENT }o--o{ SPONSOR : "sponsored by"
    
    TEAM ||--o{ PLAYER : "employs"
    TEAM ||--o{ MATCH : "plays home"
    TEAM ||--o{ MATCH : "plays away"
    TEAM ||--o{ MEDICALSTAFF : "assigns"
    TEAM ||--|| COACH : "managed by"
    TEAM }o--o{ SPONSOR : "sponsored by"
    
    PLAYER ||--o{ MATCHEVENT : "involves"
    PLAYER ||--o| GOALKEEPER : "is a"
    PLAYER ||--o| FIELDPLAYER : "is a"
    PLAYER }o--o{ SPONSOR : "sponsored by"
    
    MATCH ||--o{ MATCHEVENT : "records"
    MATCH }o--|| VENUE : "hosted at"
    MATCH }o--|| OFFICIAL : "officiated by"
    
    TOURNAMENT {
        int TournamentID PK
        varchar TournamentName
        date StartDate
        date EndDate
        varchar Season
        decimal PrizeMoney
        varchar Location
    }
    
    TEAM {
        int TeamID PK
        varchar TeamName
        int FoundedYear
        varchar City
        varchar HomeStadium
        int TournamentID FK
    }
    
    PLAYER {
        int PlayerID PK
        varchar FirstName
        varchar LastName
        date DateOfBirth
        varchar Nationality
        decimal Height
        decimal Weight
        int JerseyNumber
        int TeamID FK
    }
    
    GOALKEEPER {
        int PlayerID PK_FK
        decimal SavePercentage
        int CleanSheets
        int GoalsConceded
    }
    
    FIELDPLAYER {
        int PlayerID PK_FK
        varchar Position
        int GoalsScored
        int Assists
        decimal PassAccuracy
    }
    
    MATCH {
        int MatchID PK
        date MatchDate
        varchar KickOffTime
        int HomeTeamScore
        int AwayTeamScore
        int Attendance
        int TournamentID FK
        int VenueID FK
        int HomeTeamID FK
        int AwayTeamID FK
        int RefereeID FK
    }
    
    MATCHEVENT {
        int MatchID PK_FK
        int EventSequence PK
        varchar EventType
        int EventTime
        int PlayerID FK
        varchar Description
    }
    
    OFFICIAL {
        int OfficialID PK
        varchar FirstName
        varchar LastName
        varchar Nationality
        int ExperienceYears
        date CertificationDate
    }
    
    VENUE {
        int VenueID PK
        varchar VenueName
        varchar City
        varchar Country
        int Capacity
        varchar SurfaceType
        int YearBuilt
    }
    
    SPONSOR {
        int SponsorID PK
        varchar SponsorName
        varchar Industry
        varchar ContactPerson
        varchar ContactEmail
        decimal SponsorshipAmount
        date ContractStartDate
        date ContractEndDate
    }
    
    MEDICALSTAFF {
        int StaffID PK
        varchar FirstName
        varchar LastName
        varchar Specialization
        varchar LicenseNumber
        date HireDate
        int TeamID FK
    }
    
    COACH {
        int CoachID PK
        varchar FirstName
        varchar LastName
        varchar Nationality
        date DateOfBirth
        varchar CoachingLicense
        date ContractStartDate
        date ContractEndDate
        decimal Salary
        int TeamID FK
    }
```

## Relationship Cardinalities

### One-to-Many (1:N)
- **TOURNAMENT → TEAM**: One tournament organizes many teams
- **TOURNAMENT → MATCH**: One tournament schedules many matches
- **TEAM → PLAYER**: One team employs many players
- **TEAM → MEDICALSTAFF**: One team assigns many medical staff
- **VENUE → MATCH**: One venue hosts many matches
- **OFFICIAL → MATCH**: One official officiates many matches
- **PLAYER → MATCHEVENT**: One player involved in many match events
- **MATCH → MATCHEVENT**: One match records many match events

### One-to-One (1:1)
- **TEAM ← COACH**: One team is managed by one coach
- **PLAYER → GOALKEEPER**: One player can be one goalkeeper (disjoint subtype)
- **PLAYER → FIELDPLAYER**: One player can be one field player (disjoint subtype)

### Many-to-Many (M:N)
- **SPONSOR ↔ TOURNAMENT**: Many sponsors can sponsor many tournaments
- **SPONSOR ↔ TEAM**: Many sponsors can sponsor many teams
- **SPONSOR ↔ PLAYER**: Many sponsors can sponsor many players

## Key Notation

- **PK**: Primary Key
- **FK**: Foreign Key
- **PK_FK**: Primary Key that is also a Foreign Key (for subtypes and weak entities)

## Specialization Hierarchy

### Player Specialization (Disjoint)
```
Player (Supertype)
├── Goalkeeper (Subtype) - Disjoint
└── FieldPlayer (Subtype) - Disjoint
```

**Rule**: A player must be EITHER a Goalkeeper OR a FieldPlayer, not both.

## Weak Entity

**MATCHEVENT** is a weak entity:
- Depends on MATCH for existence
- Composite Primary Key: (MatchID, EventSequence)
- MatchID is both part of PK and FK to MATCH
- EventSequence is a partial key

## Notes

1. **Surrogate Keys**: All main entities use auto-generated integer IDs
2. **Composite Key**: MatchEvent uses (MatchID, EventSequence)
3. **Data Types**:
   - `int`: Integer/Numeric fields
   - `varchar`: String/Text fields
   - `date`: Date fields
   - `decimal`: Decimal/Float fields for money and percentages

4. **Junction Tables** (for M:N relationships, not shown in diagram):
   - TournamentSponsor (TournamentID, SponsorID)
   - TeamSponsor (TeamID, SponsorID)
   - PlayerSponsor (PlayerID, SponsorID)

## How to Use This Mermaid Diagram

### In Markdown Files
Copy the mermaid code block and paste it into any markdown file. GitHub, GitLab, and many markdown editors will render it automatically.

### Online Editors
- [Mermaid Live Editor](https://mermaid.live/)
- Paste the code to visualize and export

### Documentation Tools
- GitHub README.md
- GitLab wikis
- Notion
- Obsidian
- VS Code with Mermaid extension

### Export Options
From Mermaid Live Editor, you can export to:
- PNG
- SVG
- PDF

---

**Created for**: ICT702 Assessment 2 - Football Tournament Management System  
**Date**: December 6, 2025

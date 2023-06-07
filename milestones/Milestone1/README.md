# Milestone 1: Database Design and Architecture (32 points)

The goal of this milestone is to create a complete technical document that will define in detail the conceptual 
design and architecture of your database system. Note that this milestone is a professional document that is read 
by technical and non-technical people and teams (i,e CEO, CTO, Project Managers, Founders, Engineers, Testers....).

Milestone 1 contains several checkpoints that represent the technical documentation for your database system. 

Students will be provided with a random database topic assigned by the instructor. Once a database topic is assigned, it is highly recommended doing some research about the topic. Several things to consider during your research are finding out the missing features of similar databases systems and create or improve them in your database system. During your research, take notes of your findings because you'll summarize them in your product summary. (more about this later)


## Checkpoint I (10 points)

This checkpoint contains three sections: cover page, table of contents and product description.


### Cover Page 

The cover page of your document must contain the title of your project (i.e. Library Management System ), your name, student id and GitHub username, and finally, a version history table similar to the one in the below:

|     Checkpoint #  |    Date Submitted   |
| ----------------- | ------------------- |
|    Checkpoint I   |      02/14/2023     |

### Table of Contents 

A technical document like this one is read by technical and non-technical people (i,e CEO, founders, 
engineers....). So, some of them would want to have access to specific sections of this milestone directly and 
skip some others. A table of contents with page numbers will help them to access quickly to all the content in 
this milestone. The table of contents must be updated after a checkpoint is finished to reflect the page number 
corresponding to all the content included in that checkpoint.
   

### Project Description 

In this section, you are going to create a complete description of the idea for your database system project. 
Note that this is a high level description since at this point, the scope of the database system that you are about to create 
is not clear yet. Use the following guidelines to create your product description in paragraph form.

    • Describe the motivations to create this database system and which problems you are trying to solve (high level only)
    • A high level non-technical description of your database system 
    • A description of the unique features (high level only) that you will implement in your database system based on your research, including the ones         that exists in other similar database systems which will be improved in your system.
    • A description of at least five use cases where your unique features will be implemented and used. (check class notes and slides)
    • Name at least two existing software tools or products that are actually in the market that would benefit from using your database system. Explain in
      detail the WHY.

### Functional Database Requirements 

Functional requirements are the ones that focus on the services provided to cover the database user needs. For example, "A user shall be able to log into the system from multiple devices". Functional requirements are grouped by the entity that performed the action. 

Students must provide at least 60 functional database requirements, and they must be enumerated and grouped by the entity that performs the action. The following are some examples of database requirements extracted from a library database management system

    1. User 
        1.1. A user shall create only one account 
        1.2. A user shall be able to check out multiple books at a time
        1.3. A user shall have at least one role.

    2. Account 
        2.1. An account shall be created by only one user. 
    
    3. Role
        3.1 A role shall be linked to many users. 
    
    4. Book
        4.1 A book can be checked out by multiple users

Functional database requirements listed in this section must cover ALL the following relationships:

1. Many-to-Many
2. One-to-One
3. Many-to-One
4. One-to-Many
5. ISA
6. Aggregation 
7. Recursive

### Non-functional Database Requirements 

Non-functional database requirements focus on the constraints and properties of the database system. They are grouped by categories such as Performance, Storage, Security, Scalability.... (for more details refer to your class notes and slides)

The following are some examples of non-functional database requirements: 

     1. Performance 
         1.1 The database system shall support concurrent transactions. 
         
     2. Storage 
         2.1 The database system shall assign 10 MB of memory per table.
         2.2 The database system should support persistent storage
         
     3. Security
         3.1 Only encrypted passwords shall be supported by the database system 
         3.2 All the values inserted into the database shall be consistent with the attribute's datatype and domain. 
         3.2 The database shall be automatically backed up everyday at 11:59 pm. 

Although there is no limit in the number of non-functional requirements required for this checkpoint, your non-functional 
requirements must cover all the constraints and properties of your database system to get credit. Please check lecture notes and slides to learn about all the categories required for non-functional database requirements.  

## Checkpoint II: Database Conceptual Design (15 points)

In this checkpoint, students will use the database functional requirements created in checkpoint #1 to build
the conceptual design of the database (ERD) and to create a detailed description of all the entities in the database.

## Entity Relationship Diagram (ERD) 
Create an Entity Relationship Diagram (ERD) that will represent the conceptual high level design of your relational 
database system. This ERD must be done using a software tool that supports drawing diagrams. I strongly recommend 
for this [draw.io](https://www.draw.io). ***Note: hand-drawing diagrams are not allowed***

***The diagram must contain at least 16 STRONG entities to get credit for this checkpoint; No exceptions!***

Once the ERD is completed, it must be exported (pdf, png, jpg....) and must be embedded into your document for this 
checkpoint. Screenshots of your ERD are also allowed as long as the image is readable and high quality. ***If we can't 
read your ERD, no credit will be given for this checkpoint***

## Entity Description 

This section **MUST** be completed concurrently with the ERD section because most of the weak entities will be unknown 
until the ERD is completed. When describing your entities state clearly their form (strong or weak), and include at least 
three attributes per entity. The attributes must be defined by their domain and form. Below, you can find several
examples of entities descriptions.

      1. User (Strong)
          * user_id: key, numeric 
          * name: composite, alphanumeric
          * dob: multivalue, timestamp
          
      2. Book (Strong)
          * ISBM: key, alphanumeric
          * title: composite, alphanumeric
          * author: composite, alphanumeric
      
      3. Role (Strong)
          * role_id: key, numeric
          * description: alphanumeric
      
      3. Account (Weak)
          * id: key, numeric 
          * user: key, numeric 
          * role: key, numeric
          


***Note: give meaningful names to your entities and your attributes. For instance 'rid' is not a good
attribute name for the id of the role***

## Checkpoint III: Database Architecture (7 points)

In this checkpoint, students will build the database architecture based on their ERD and entity description 
from checkpoint II. 

### Entity Establishment Relationship Diagram (EER) 

***Note: This section must be done using MySQLWorkBench***

Create an EER model of your database system based on the final version of your ERD and entity descriptions. 
Your EER must show clearly the following components:
 
   • PK, FK and Unique keys (if any)
  
   • All the table attributes, and their data types
  
   • NOT NULL in attributes (if any)
  
   • Identifying relationships and non-identifying relationships. Both of them represented by solid and dashed lines in 
  the database model. 
  
   • All the relationships between entities and their cardinalities including those with zeros 
   
Once the EER is completed do the following: 

   (1) save your database model as EER.mwb and upload this file to the "files" folder located in this directory 
   
   (2) export your EER to any of the following formats (pdf, png, jpg....) and embed it into your milestone1.pdf file for this checkpoint. Screenshots of your EER are also allowed as long as the image is readable and high quality. ***If we can't read your ERD, no credit will be given for this checkpoint****


### Constraints Description 

In your document, create a description table (similar format to the one below) including all the tables that implement ON DELETE AND ON UPDATE and all their possible constraints (CASCADE, SET NULL......). This description should include a detailed comment about your motivations to select those tables as the ones that implement those constraints. 

|     Table     |       FK        |       ON DELETE        |        ON UPDATE        |                  Comment                        | 
| ------------- | --------------- | ---------------------- | ----------------------- | ----------------------------------------------- |
|    Account    |      user       |       ON CASCADE       |        ON CASCADE       | If a user is deleted, then the account from that user must be deleted as well
|    User       |      role       |       SET NULL         |        ON CASCADE       | If a role is removed from a specific user, the user that was holding that role will hold no role until a new one is assigned.


### Forward Engineering and Populating Database 

***Note that all your work done in this section must be uploaded in the file's folder found in this directory***

The forwarding engineering process is the one that translates your database model (EER) into the database schema that is used to create the physical database, tables and attributes in your database system. Note that this process must be done in MYSQLWorkBench as seen in class. Backward engineering is not allowed in this section

Before starting the forwarding engineering process of your database model, make sure to provide a meaningful name for your database schema. By default, MSQLWorkBench assign 'mydb'. Replace it with the name of your database + "DB" (i.e. LibraryManagementDB)

Proceed with the forward engineering process of your database model as learned in class, and create a file databasemodel.sql file that contains all the CREATE SQL statements from the forward engineering process

Run databasemodel.sql script in your mysql instance to create your physical database schema and its tables in your system (localhost). This can be done in many ways, but the most common ones are:

    (1) Run the databasemodel.sql script directly in your MYSQLWorkBench or

    (2) Open a SQL script windows MYSQLWorkBench, and copy and paste the content of databasemodel.sql there. Then, click on run. or

    (3) Open a terminal windows, and connect to your MySQL instance, then execute the following command: 
    
        mysql> source <path_to_your_sql_script>;

Once your database and tables are created in your mysql localhost instance, then upload the databasemodel.sql file in the 'files' folder located in this directory

***No need to add anything to the pdf document for this section.***

***Note that at grading time your databasemodel.sql must run without errors to get credit for this section***

### Inserting Sample Data 

In order to test your database system, it needs to be populated first with sample data that represents the scope and domain
of the business requirements that will be implemented by the software product that is using your database system. 

1. Create a file inserts.sql file. 

2. Add some comments on the top of the file to explain the context of this file

3. The first SQL code this file must have is the following: 

    ```mysql
       USE LibrarySystemDB; -- Replace LibrarySystemDB with the name of your database system
    ```
4. Insert some sample data in all your tables. ***Each table in your database must have at least three inserts.***
For instance, our library system database has three tables User, Book, and Account: 
    ```mysql
       -- Script name: inserts.sql
       -- Author:      Jose Ortiz
       -- Purpose:     insert sample data to test the integrity of this database system
       
       -- the database used to insert the data into.
       USE LibrarySystemDB; 
       
       -- User table inserts
       INSERT INTO User (user_id, name, dob) VALUES (1, 'Alice', 631152000), (2, 'Bob', 694742400), (3, 'Trudi', 958089600);
       
       -- Book table inserts
       INSERT INTO Book (ISBM, title, author) VALUES (87736778838, 'Database System Concepts', 'Avi Silberschatz'), (87736778838, 'Clean Code', 'Robert C. Martin'), (8773677564, 'The Art of Computer Programming', 'Donald E. Knuth');
   
       -- Account table inserts
       INSERT INTO Account (account_id, user, role) VALUES (1, 1, 'Admin'), (2, 2, 'user'), (3, 3, 'admin');
       
   ``` 
5. Run inserts.sql in your MySQL instance. 

6. Upload the inserts.sql file in 'files' folder located in this directory

7. No need to add anything to the pdf document for this section. 

***No need to add anything to the pdf document for this section.***
***Note: inserts.sql must run without errors in order to get credit for this section***

# Grading Rubrics 

1. This milestone is worth 32 points. 

3. Good formatting in technical documents is really important. Points will be deducted for bad formatting. 

4. Every checkpoint must begin in a new page.


# Submission Guidelines 

The due date for every checkpoint of this milestone will be announced in class, Canvas, Discord, and by email. 
The following are the submission guidelines that you need to follow:

1. Submissions are final and late work won't be accepted. I will give students more than enough time to complete all the checkpoints. Therefore, plan your time accordingly and submit your work on time.

2. The table of assignments (found in main README file of your repository) MUST be updated to "DONE" once a checkpoint is completed by its deadline. Checkpoints set to "TODO" will be considered not submitted. Therefore, won't get credit.

3. Checkpoints are cumulative work. Use the same document (milestone1.pdf) to submit every checkpoint for this milestone. For example, if you completed checkpoint II, your document in this folder should also include your work in all the previous checkpoints.

4. Milestone 1 document must be hosted in the master branch of your class repository 
(DatabaseSystems/milestones/milestone1/milestone1.pdf).

5. Milestone documents sent by email, hosted in personal repositories, or uploaded in a file format other than PDF won't get credit, and will be considered as not submitted. ***No exceptions***













-- Create the database tables
CREATE TABLE branches (
    branch_id INTEGER PRIMARY KEY,
    branch_name TEXT NOT NULL
);

CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL,
    branch_id INTEGER NOT NULL,
    FOREIGN KEY (branch_id) REFERENCES branches(branch_id)
);

-- Insert sample data
INSERT INTO branches (branch_id, branch_name) VALUES
(1, 'Computer Science'),
(2, 'Electronics'),
(3, 'Mechanical');

INSERT INTO students (student_id, student_name, branch_id) VALUES
(1, 'Alice', 1),
(2, 'Bob', 1),
(3, 'Charlie', 2),
(4, 'David', 1),
(5, 'Eve', 3);

-- Query to count students in each branch (count > 1)
SELECT 
    b.branch_name,
    COUNT(s.student_id) AS student_count
FROM branches b
LEFT JOIN students s ON b.branch_id = s.branch_id
GROUP BY b.branch_id, b.branch_name
HAVING COUNT(s.student_id) > 1;
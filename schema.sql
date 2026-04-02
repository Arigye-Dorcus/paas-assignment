-- Create the students table
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a courses table (extra table to show more database design)
CREATE TABLE IF NOT EXISTS courses (
    id SERIAL PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create enrollments table (links students and courses)
CREATE TABLE IF NOT EXISTS enrollments (
    id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(id) ON DELETE CASCADE,
    course_id INT REFERENCES courses(id) ON DELETE CASCADE,
    enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sample data for students
INSERT INTO students (name, email) VALUES
('Alice Nakato', 'alice@example.com'),
('Brian Ssempa', 'brian@example.com'),
('Carol Apio', 'carol@example.com'),
('David Otim', 'david@example.com');

-- Sample data for courses
INSERT INTO courses (title, description) VALUES
('Cloud Computing', 'Introduction to cloud platforms and services'),
('Web Development', 'Building modern web applications'),
('Database Systems', 'Relational databases and SQL');

-- Sample enrollments
INSERT INTO enrollments (student_id, course_id) VALUES
(1, 1),
(1, 2),
(2, 1),
(3, 3),
(4, 2);
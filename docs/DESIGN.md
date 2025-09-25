
**EduFlow SMS – Design & Architecture**

---

## 1. 🎯 Objective

EduFlow SMS is designed as a modular backend system that demonstrates:

* **OOP principles (4 pillars)** → Abstraction, Encapsulation, Inheritance, Polymorphism.
* **Clean architecture** → clear separation of domain, application, infrastructure, and interfaces.
* **Practical business rules** → course capacity and duplicate enrollment prevention.
* **Extensibility** → scraper integration, API, and CLI.

---

## 2. 🏛 OOP Principles in EduFlow

### 2.1 Abstraction

* Defined in the `Person` class (`src/domain/models/person.py`) as an **abstract base class (ABC)**.
* `Student` and `Teacher` **must implement** the abstract method `role()`.
* This hides implementation details while forcing subclasses to define their specific role.

```python
class Person(ABC):
    @abstractmethod
    def role(self) -> str:
        pass
```

---

### 2.2 Encapsulation

* `Student` manages its own enrollments internally (`self.enrollments`).
* The only safe way to modify enrollments is via the `enroll()` method, which checks rules (capacity, duplicates).
* Prevents external code from corrupting state.

```python
class Student(Person):
    def enroll(self, course):
        if course.capacity_reached():
            raise ValueError("Course is full.")
        if course in self.enrollments:
            raise ValueError("Already enrolled.")
        self.enrollments.append(course)
        course.enrolled_students.append(self)
```

---

### 2.3 Inheritance

* `Student` and `Teacher` both inherit from `Person`.
* This avoids duplication and allows shared attributes (`id`, `name`, `email`, `created_at`).

```python
class Student(Person): ...
class Teacher(Person): ...
```

---

### 2.4 Polymorphism

* Both `Student` and `Teacher` override the `role()` method in their own way.
* Same interface (`role()`), different behavior depending on the class.

```python
def role(self) -> str:
    return "Student"

def role(self) -> str:
    return "Teacher"
```

---

## 3. 🏗️ Clean Architecture Layers

EduFlow follows a **layered architecture**:

```
Domain → Application → Infrastructure → Interfaces
```

---

### 3.1 Domain Layer (`src/domain/`)

* **Pure business logic** → `Person`, `Student`, `Teacher`, `Course`, `Enrollment`.
* No external dependencies (no DB, no FastAPI).
* Demonstrates **OOP pillars**.

---

### 3.2 Application Layer (`src/application/`)

* **Services** implement business rules:

  * `EnrollmentService` → prevents duplicate enrollment and enforces capacity.
  * `StudentService`, `TeacherService`, `CourseService` → handle creation/retrieval.
* **Mappers** convert Domain ↔ DB models.
* Raises **custom exceptions** (`BusinessRuleViolation`).

---

### 3.3 Infrastructure Layer (`src/infrastructure/`)

* **Database** → SQLAlchemy models + session.
* **Scraper** → fetches data (quotes/books), saves to JSON and DB.
* Deals with **external technology** (PostgreSQL, HTTP).

---

### 3.4 Interfaces Layer (`src/interfaces/`)

* **API (FastAPI)** → REST endpoints for students, teachers, courses, enrollments, and scraped resources.
* **CLI** → trigger scraper from terminal.
* This is the **entrypoint** for end users and developers.

---

## 4. 🔄 Data Flow

1. User calls API → `FastAPI Router` (Interfaces).
2. Router calls → `Service` (Application).
3. Service applies → Business Rules + Domain logic.
4. Service persists/retrieves from → DB Models (Infrastructure).
5. Service maps back → Domain Objects.
6. Router returns → JSON response to User.

---

## 5. 📦 Scraper Integration

* **Scraper** (Infrastructure) fetches data from `quotes.toscrape.com`.
* Saves to `samples/scraped.json`.
* Optionally inserts into DB (`scraped_resources` table).
* Exposed via:

  * **CLI** → `python -m src.interfaces.cli scrape --pages 3 --db`
  * **API** → `GET /scraped_resources/`

---

## 6. 🛡️ Business Rules

* A student **cannot enroll twice** in the same course.
* A course **cannot exceed capacity**.
* Violations raise `BusinessRuleViolation`, handled globally in API.

---

## 7. ✅ Testing Strategy

* **Unit Tests** → Domain models (`Student.enroll()`, `Course.capacity_reached()`).
* **Integration Tests** → API endpoints, enrollment rules, DB persistence.
* **Scraper Test** → ensures data is scraped and JSON saved correctly.

---

## 8. 🚀 Why This Design Works

* **Separation of Concerns** → domain logic isn’t polluted by DB/API details.
* **Testability** → domain logic can be tested independently.
* **Extensibility** → scraper, API, and CLI are modular.
* **OOP Demonstration** → clearly showcases abstraction, encapsulation, inheritance, and polymorphism.
* **Production Practices** → logging, Docker, migrations, and testing included.

---
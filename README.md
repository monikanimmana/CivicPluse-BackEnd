# CivicLens — Civic Complaint Management Platform

A role-based civic complaint management system that allows citizens to report civic issues and enables officers, field workers, and administrators to track, assign, and resolve them through a structured, multi-stage workflow.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Tech Stack](#tech-stack)
3. [User Roles](#user-roles)
4. [Authentication](#authentication)
5. [Duplicate Complaint Detection](#duplicate-complaint-detection)
6. [Complaint Lifecycle](#complaint-lifecycle)
7. [API Architecture](#api-architecture)
8. [Project Structure](#project-structure)
9. [Roadmap](#roadmap)

---

## Project Overview

CivicLens is a full-stack platform for managing civic issue reporting and resolution. It supports four distinct user roles, each with different permissions and views, and includes location-aware duplicate detection to reduce redundant complaint submissions — a common problem in civic reporting systems where multiple citizens report the same issue independently.

**Core capabilities:**
- Role-based access control across four user types
- JWT-based authentication with automatic token refresh
- Geolocation-based duplicate complaint detection
- Multi-stage complaint status tracking with automated timestamping
- React + TypeScript frontend consuming a Django REST API

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend Framework | Django |
| API Layer | Django REST Framework |
| Database | PostgreSQL |
| Authentication | JWT (SimpleJWT) |
| Frontend | React + TypeScript |

---
<img width="959" height="463" alt="image" src="https://github.com/user-attachments/assets/a3af2f6f-64de-4baa-ae8e-d063c0685163" />
<img width="959" height="461" alt="image" src="https://github.com/user-attachments/assets/8cd7aa19-0e94-4243-ae1d-bc978e6bb47b" />

<img width="796" height="452" alt="image" src="https://github.com/user-attachments/assets/2aa8c63f-0f98-4f3c-8aee-bc55f9c39698" />

<img width="959" height="509" alt="image" src="https://github.com/user-attachments/assets/69161898-7e6f-4dfd-9885-8f26a424f060" />

<img width="773" height="386" alt="image" src="https://github.com/user-attachments/assets/b280a846-967d-47aa-a4e3-448d46c2026b" />

<img width="752" height="506" alt="image" src="https://github.com/user-attachments/assets/b771c7c0-b450-408f-bd37-5c79fa0d5675" />





## User Roles

The platform supports four distinct roles, each with scoped permissions:

| Role | Responsibility |
|---|---|
| **Citizen** | Submits complaints, tracks status of their own submissions |
| **Officer** | Reviews and assigns incoming complaints |
| **Worker** | Handles on-ground resolution of assigned complaints |
| **Admin** | Full platform oversight — manages users, roles, and complaint data |

Role-based access control ensures each user type only sees and interacts with the data and actions relevant to their responsibilities.

---

## Authentication

Authentication is implemented using **JWT (JSON Web Tokens)** via the `djangorestframework-simplejwt` package.

### Access and Refresh Tokens

- **Access token** — short-lived token used to authenticate individual API requests.
- **Refresh token** — longer-lived token used to obtain a new access token once the current one expires, without requiring the user to log in again.

### Automatic Token Refresh

The React frontend automatically detects when an access token has expired (via a `401 Unauthorized` response) and transparently requests a new access token using the stored refresh token — keeping the user logged in without manual intervention.

### Centralized 401 Error Handling

Rather than handling authentication errors individually in every API call, the frontend uses a centralized interceptor pattern to catch `401` responses globally, attempt a token refresh, and retry the original request — or redirect to login if the refresh token itself has expired.

---

## Duplicate Complaint Detection

A key feature of CivicLens is automatic detection of potentially duplicate complaints, using the **Haversine formula**.

### The Problem

When multiple citizens report the same civic issue (e.g., a pothole, broken streetlight) independently, it creates redundant entries that waste officer/worker time and fragment the resolution process.

### The Solution — Haversine Formula

The Haversine formula calculates the great-circle distance between two points on Earth's surface given their latitude and longitude — accounting for the Earth's curvature, which a simple Euclidean distance calculation would ignore.

```
distance = Haversine(complaint_new.lat, complaint_new.lng, complaint_existing.lat, complaint_existing.lng)
```

When a new complaint is submitted, its coordinates are compared against existing open complaints in the surrounding area. If an existing complaint is found within a **100-meter radius**, the new submission is flagged as a potential duplicate.

**Why 100 meters?** This radius is small enough to avoid falsely flagging genuinely distinct issues (e.g., two different potholes on the same street), while still catching the common case of multiple citizens reporting the exact same issue from slightly different GPS readings.

---

## Complaint Lifecycle

Each complaint moves through a defined sequence of statuses:

```
Pending → Assigned → In Progress → Resolved → Closed
```

| Status | Meaning |
|---|---|
| **Pending** | Complaint submitted, awaiting officer review |
| **Assigned** | Officer has assigned the complaint to a field worker |
| **In Progress** | Worker is actively resolving the issue |
| **Resolved** | Issue has been fixed, pending final confirmation |
| **Closed** | Complaint fully closed out |

### Automated Timestamping

Every status transition is automatically timestamped, creating an auditable history of how long a complaint spent in each stage — useful for tracking officer/worker response times and identifying bottlenecks in the resolution process.

### Unique Complaint ID Generation

Each complaint is assigned a unique identifier upon submission, used for tracking and reference throughout its lifecycle.

### Role-Based Status Transitions

Not every role can move a complaint to every status — for example, only an assigned worker can mark a complaint as "In Progress" or "Resolved," and only an officer can move a complaint from "Pending" to "Assigned." This prevents unauthorized or accidental status changes.

---

## API Architecture

The backend exposes **20+ REST API endpoints** consumed by the React + TypeScript frontend, covering:

- Complaint creation, retrieval, update, and status transitions
- User authentication (login, token refresh, logout)
- Role-based data filtering (each role only receives data relevant to their permissions)
- Duplicate detection checks during complaint submission

The frontend and backend are fully decoupled — the React app communicates with Django exclusively through this REST API layer, allowing the two to be developed, tested, and deployed independently.

---

## Project Structure

```
civiclens/
├── backend/
│   ├── complaints/       # Complaint models, views, serializers
│   ├── users/            # User roles, authentication logic
│   ├── core/              # Shared utilities (e.g., Haversine calculation)
│   └── config/             # Django project settings
├── frontend/
│   ├── src/
│   │   ├── components/    # Reusable React components
│   │   ├── pages/          # Role-specific views (Citizen, Officer, Worker, Admin)
│   │   ├── services/        # API client, token refresh interceptor
│   │   └── types/            # TypeScript type definitions
```

---

## Roadmap

- [x] Role-based user system (Citizen, Officer, Worker, Admin)
- [x] JWT authentication with access/refresh token flow
- [x] Automatic token refresh and centralized 401 handling
- [x] Haversine-based duplicate complaint detection
- [x] Multi-stage complaint lifecycle with automated timestamping
- [x] React + TypeScript frontend integration (20+ endpoints)
- [ ] Notification system for status changes
- [ ] Analytics dashboard for admins (complaint volume, resolution time trends)
- [ ] Mobile-responsive UI improvements

---

## Why CivicLens

Civic issue reporting is often fragmented across phone calls, in-person visits, and disconnected systems, making it hard for municipal bodies to track resolution progress or avoid duplicated effort. CivicLens centralizes this process into a single role-based platform, with built-in duplicate detection to keep the complaint queue clean and actionable for officers and field workers.

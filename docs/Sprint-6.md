# 🏁 Sprint 6: User Access + Role-Based Permissions

### ✅ Sprint Goals

* Implement protected views using JWT
* Add role-based access control (Retailer vs Customer)
* Create endpoint to fetch logged-in user info
* Implement logout endpoint using JWT blacklist
* (Optional) Add refresh token logic

---

### 🧱 Features & Tasks Checklist

#### 🔐 JWT Protected Views

* [ ] Apply `IsAuthenticated` to sensitive views
* [ ] Handle 401 errors clearly for frontend

#### 🛂 Role-Based Permissions

* [ ] Create `IsRetailer` and `IsCustomer` permission classes
* [ ] Add permissions to medicine/product views
* [ ] Validate unauthorized access errors (403)

#### 👤 User Info Endpoint

* [ ] Create `/api/v1/users/me/` view (GET)
* [ ] Return profile data of logged-in user

#### 🚪 Logout API (JWT Blacklist)

* [ ] Enable blacklist app in `settings.py`
* [ ] Implement logout view to blacklist refresh token

#### 🔁 (Optional) Refresh Token Support

* [ ] Allow refresh using `/token/refresh/`
* [ ] Educate frontend how to store and rotate tokens

---

### 📦 Folder Structure (Suggestion)

```
users/
├── views.py  ← Add MeView, LogoutView
├── permissions.py  ← IsRetailer, IsCustomer
└── urls.py   ← Add new endpoints
```

---

### 📚 Concepts to Learn During Sprint

* `request.user` and JWT Auth
* `IsAuthenticated` and `BasePermission`
* Blacklisting tokens via `rest_framework_simplejwt.token_blacklist`
* Protecting APIs using custom roles

---

### 📅 Sprint Duration Suggestion

**Target**: 3-4 days (can be parallel with frontend prep)

Let’s go full product-mode 🚀

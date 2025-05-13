🧠 So Now: How Does the Flow Work?
Let’s draw the whole path:

🎯 Data Flow When RegisterView() API is Hit:
Frontend / Postman
     ↓
[RegisterView] (CreateAPIView)
     ↓
self.get_serializer(data=request.data)
     ↓
[RegisterSerializer] (validates, saves)
     ↓
serializer.save()   → calls create()
     ↓
create() → CustomUser.objects.create_user(...)
     ↓
CustomUserManager.create_user(...)  ← this is where self.model(...) happens
     ↓
user = self.model(...)  ← creates in-memory object
user.set_password(...)  ← hashes password
user.save()              ← triggers CustomUser.save()
     ↓
super().save() → models.Model.save() ← writes to database

|-------------------------------------------------------------------------------------------------|

✅ Quick Future Roadmap: Models & Views to Create (Checklist Only)
We'll build these step-by-step later — for now, just bookmark it:

🧑 Users App (Auth / Roles)

Custom User model (is_staff → owner, is_superuser → platform admin)

Roles: medical shop owner (admin), staff, customer

Auth views: login, register, logout

Token auth (already in place ✅)

Password reset (future)

🏬 Shop Management

MedicalShop model (OneToOne with User)

Shop profile: name, address, license, logo

Associate Medicines to a shop

📦 Inventory / Sales

Orders model (customer orders)

OrderItems (line items per order)

Stock audit / logs (maybe later)

Billing model (future)

💬 Customer App (if public-facing)

Profile, Addresses

Wishlist / Cart

Reviews/ratings (if needed)

🧠 Admin Panel / Dashboard Views

Admin: list of shops, orders, users

Shop Owner: inventory dashboard, earnings

Charts/Stats APIs (for frontend)

Bookmark ✅ this. We'll return to it after MVP is complete.

|-------------------------------------------------------------------------------------------------|
Upcoming Core Features (Planned):

🔍 Search + Filter Medicines

🛒 Add-to-cart & place order (Retail side)

📦 Stock & Inventory per medical store

📈 Store-specific dashboards

💸 Payment or Subscription model for shop owners

🧾 Invoices/Receipts for placed orders

🧪 Unit + Integration testing before deployment

|-------------------------------------------------------------------------------------------------|
🚀 Updated Sprint Plan (Sprint 5: "API Usability + Frontend Readiness")


Day	Task	Status
Day 1	✅ Pagination with response format testing	Done
Day 2	🔍 Filtering + Search (DRF filters) — by name, expiry, mg	Next
Day 3	📘 Auto API docs with Swagger / Redoc	Planned
Day 4	🔐 Improve Auth error messages (custom exception handler)	Planned
Day 5	🎯 Frontend-friendly API response (clean JSON, remove useless metadata)	Planned
Day 6	🧪 Sample frontend (basic HTML or Postman Visualizer)	Optional/Fun
Day 7	📌 Sprint wrap + Commit docs in /docs/Sprint-5.md	Final Day


|-------------------------------------------------------------------------------------------------|
🎯 How it links to core features:


Feature	Mapping
Search + Filter	Sprint 5 Day 2
Inventory APIs	Already being used/tested
Add to cart / Place order	Starts in next sprint (Sprint 6)
Payment / Subscription	Post MVP feature
Store Dashboards	Later Sprint


|-------------------------------------------------------------------------------------------------|

✅ Pagination: DONE
You’ve correctly implemented DRF pagination. Now instead of returning a huge list of medicines, it chunks the response into manageable pages. This prevents:

Slow frontend loading on large datasets

API timeouts due to massive responses

Memory overheads for clients fetching everything at once.

🎯 Final thought: You can consider this task ✅ done. You can improve it later with page size query support like ?page_size=5.

|-------------------------------------------------------------------------------------------------|
🚀 Next Backend Features to Build

-User Accounts

Custom User model (email as username)

Roles: Admin, Retailer, Customer

JWT Auth already in use — extend it with role-based permissions

-Retailer Profile

One-to-one with User

Store name, address, license info (optional)

Only Retailers can create/manage products

-Customer Profile

One-to-one with User

Basic info: name, email, phone

Later: delivery address, order history

-Orders

Models: Order, OrderItem

Status: Pending, Approved, Delivered

Retailer sees only their orders

Customer sees their order history

-Cart System (Optional MVP)

Add-to-cart functionality

Can be tied to Order creation later

-Review & Ratings (Future sprint)

Customers can rate medicines

Avg rating shown on listings

|-------------------------------------------------------------------------------------------------|

To load this fixture later:
bash
python manage.py loaddata medicines_fixture.json
(Django automatically checks all fixtures/ directories in installed apps)

Best Practice:
For organization, you might want to name the fixture by model and date:

bash
python manage.py dumpdata medicines --indent 2 > apps/medicines/fixtures/medicines_$(date +%Y-%m-%d).json

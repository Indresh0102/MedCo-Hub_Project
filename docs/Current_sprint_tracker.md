# 🛣️ MedCo-Hub Project: Progress Tracker

## ✅ DONE
| Task | Status | Notes |
|------|--------|-------|
| Project Structure Setup | ✅ | `backend/`, `apps/`, `manage.py` – all good |
| `users` app created | ✅ | Inside `backend/apps/users` |
| `AUTH_USER_MODEL` configured | ✅ | Custom User model active |
| DRF installed and project bootstrapped | ✅ | REST framework ready |
| `users` models, views started | ✅ | Basic structure done |
| MVP Features locked | ✅ | Core features planned |
| Render confirmed for deployment | ✅ | We’ll handle this later |
| Sprint-2.md created in `/docs` | ✅ | 🧠 Team-style documentation |
| Figma UI flow uploaded | ✅ | UI direction confirmed |

---

## 🏃‍♂️ IN PROGRESS
| Task | Status | What to Do |
|------|--------|------------|
| Create `medicines` app | 🔄 | Use:
`python manage.py startapp medicines apps/medicines` |
| Register `medicines` in `INSTALLED_APPS` | 🔄 | Add `'apps.medicines'` to `settings.py` |
| Plan `models.py` for Medicines | 🔄 | Include `name`, `description`, `price`, `expiry`, etc. |
| Create DRF `serializers.py` | 🔄 | For `MedicineSerializer` |
| Setup CRUD APIs for medicines | 🔄 | Use `APIView` or `ViewSets` |
| Add dummy medicine data | 🔄 | For testing purposes |
| Connect frontend to these APIs | 🔄 | After endpoints are ready |

---

## 🧩 COMING UP NEXT
| Task | Priority | Notes |
|------|----------|-------|
| Authentication: JWT setup | Medium | `SimpleJWT` config |
| Token refresh, access expiry | Medium | Secure auth |
| Search/filter medicines | High | Bonus feature |
| Pagination support | High | DRF handles this easily |
| Create reusable UI components | High | From your Figma |
| Write Sprint-3.md planning | Medium | Next set of deliverables |

---

## 🚀 Final Deployment Goals (Later)
| Task | Notes |
|------|-------|
| Configure environment variables | Use `.env`, don’t hardcode secrets |
| Final deploy to Render | Production-ready |
| Add monitoring (Sentry/logs) | Optional, bonus feature |
| Write tests (unit + integration) | Use `pytest` or Django’s `TestCase` |



# Troubleshooting Guide (Sprint-3)

## ❗ Problem: ModuleNotFoundError: No module named 'rest_framework'

### ✅ Fix:
Add `'rest_framework'` to your `INSTALLED_APPS` in `settings.py`.

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

### 🤔 Why this happens?
When you use Django REST Framework (DRF) views like `APIView`, Django needs to know where to find them. If `'rest_framework'` isn’t added in `INSTALLED_APPS`, Django can’t locate its internal structure.

---

## 📸 Reference: APIView Visible in API Browser

Check that your `/api/medicines/` endpoint is visible in the browsable API UI after fixing `INSTALLED_APPS`.

---

## 🧠 Tip for Future Devs

Always check if DRF is installed and added to `INSTALLED_APPS` before writing DRF views. You can verify with:

```bash
pip show djangorestframework
```

Or reinstall if needed:

```bash
pip install djangorestframework
```

Then run:

```bash
python manage.py runserver
```

Enjoy the browsable API UI! 😎

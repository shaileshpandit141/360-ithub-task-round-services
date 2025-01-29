# **360 IT Hub Task Round (Services Project)**

This is a Django-based web application that provides functionalities for managing services,
user subscriptions, and payment integration with Razorpay. It includes CRUD operations for services, 
user authentication, subscription flows, secure payment processing, and includes test data setup.

---

## **Demo Video**

A recorded demo video showcasing the project functionality is available:
- **File**: recorded_demo_video.mp4
- **Contents**: Demonstrates complete user workflow including registration, service browsing,
subscription process, and payment flow
- **Duration**: ~5 minutes

---

## **Features**

1. **User Authentication**:
   - Secure user registration with OTP verification.
   - Login and logout functionality.

2. **Service Management**:
   - Model with fields: name, payment_terms, price, package, tax, image, active
   - Add, update, delete, and view services
   - List only active services on the homepage

3. **Subscription Management**:
   - Model with fields: user, service, address, payment_status, transaction_id
   - Handles user subscriptions and payment tracking
   - Supports Razorpay payment integration

4. **Payment Integration**:
   - Razorpay API integration for secure payments.
   - Payment status management and order tracking.

5. **Admin Panel**:
   - Manage users, services, and subscriptions.

6. **Environment Variables**:
   - Uses `python-decouple` for secure management of sensitive data in a `.env` file.

7. **Test Data Setup**:
   - Includes `add_test_data.py` script for populating test data
   - Creates sample users, services and subscriptions
   - Useful for testing and development

---

## **Tech Stack**

- **Backend**: Django, Python
- **Frontend**: HTML, CSS (Bootstrap), Jinja2 Templates
- **Database**: SQLite
- **Payment Gateway**: Razorpay
- **Environment Management**: `python-decouple`

---

## **Setup Instructions**

Follow these steps to set up the project locally.

### **1. Prerequisites**
- Python (>=3.9)
- Pip and Virtual Environment

### **2. Clone the Repository**
```bash
git clone https://github.com/shaileshpandit141/360-ithub-task-round-services.git
cd it_services_task
```

### **3. Create and Activate a Virtual Environment**
```bash
python3 -m venv .venv
source .venv/bin/activate  # For Linux/Mac
.venv\Scripts\activate     # For Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Configure Environment Variables**
Create a `.env` file in the project root and add the following:
```bash
# SECRET_KEY Env Configuration Settings
# -------------------------------------
SECRET_KEY=your-secret-key

# DEBUG Env Configuration Settings
# --------------------------------
DEBUG=True

# ALLOWED_HOSTS Env Configuration Settings
# ----------------------------------------
ALLOWED_HOSTS=localhost,127.0.0.1

# Email Env Configuration Settings
# --------------------------------
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
EMAIL_HOST_USER=user-email
EMAIL_HOST_PASSWORD=user-email-host-password
DEFAULT_FROM_EMAIL=default-from-email

# Razorpay API Env keys Configuration Settings
# --------------------------------------------
RAZORPAY_KEY_ID=your-razorpay-key-id
RAZORPAY_KEY_SECRET=your-razorpay-key-secret
```

### **5. Apply Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **6. Create a Superuser**
```bash
python manage.py createsuperuser
```

### **7. Run the Development Server**
```bash
python manage.py runserver
```

### **8. Add Test Data (Optional)**
```bash
python add_test_data.py
```
This will populate the database with sample:
- Services with varying prices and packages
- Sample subscriptions and transactions
- Test data useful for development and testing

## **Usage Instructions**

### **1. Admin Panel**
- Access the admin panel at: http://localhost:8000/admin
- Use the superuser credentials to log in.

### **2. User Workflow**
- Register: Users register with their email, username, and password. An OTP is sent for verification.
- Login: After registration, users can log in to access the services.
- Browse Services: Users can view all active services on the homepage.
- Subscribe: Users can subscribe to a service, provide their address, and proceed to payment using Razorpay.
- Payments: Upon successful payment, the subscription is saved with the status Success.

### **3. Service Management**
Admins or authorized users can:
- Add a new service.
- Update an existing service.
- Delete a service.
- Mark services as active/inactive.

## **API Integrations**

### **Razorpay Integration**
- **Order Creation**:
  - Orders are created dynamically based on the service price and tax
  - Uses Razorpay's order API endpoint
  - Returns order ID for payment processing

- **Payment Verification**:
  - Implements signature verification using Razorpay's verification API
  - Validates payment authenticity
  - Updates subscription status upon successful verification

## **Contact Information**

For questions, please contact:

**Email**: shaileshpandit@gmail.com.com\
**Phone**: +917970367915

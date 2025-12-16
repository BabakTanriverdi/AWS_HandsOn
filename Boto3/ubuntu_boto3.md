# Installing boto3 on Ubuntu Using a Python Virtual Environment (venv)

This guide provides a complete, ordered set of commands to create a Python virtual environment on Ubuntu, install **boto3**, exit the environment, and re-enter it when needed.

---

## 1. Install Required System Packages

```bash
sudo apt update
sudo apt install -y python3-full python3-venv python3-pip
```

---

## 2. Create and Enter a Working Directory

```bash
mkdir ~/Desktop/boto
cd ~/Desktop/boto
```

---

## 3. Create the Virtual Environment

```bash
python3 -m venv venv
```

---

## 4. Activate the Virtual Environment

```bash
source venv/bin/activate
```

The prompt will change to:

```text
(venv) user@ubuntu:~/Desktop/boto$
```

---

## 5. Upgrade pip (Recommended)

```bash
pip install --upgrade pip
```

---

## 6. Install boto3

```bash
pip install boto3
```

---

## 7. Verify the Installation

```bash
python -c "import boto3; print(boto3.__version__)"
```

---

## 8. (Optional) AWS Test Command

```bash
python - <<'EOF'
import boto3
print(boto3.client("sts").get_caller_identity())
EOF
```

---

## 9. Exit the Virtual Environment

```bash
deactivate
```

The prompt will return to normal:

```text
user@ubuntu:~/Desktop/boto$
```

---

## 10. Re-enter the Virtual Environment Later

```bash
cd ~/Desktop/boto
source venv/bin/activate
```

---

## 11. Check the Active Python Interpreter

```bash
which python
```

Expected output:

```text
/home/user/Desktop/boto/venv/bin/python
```

---

## 12. Completely Remove the Virtual Environment (If Needed)

```bash
deactivate  # only if currently active
rm -rf venv
```

---

## Quick Summary (One-Glance)

```bash
sudo apt install python3-full python3-venv python3-pip
cd ~/Desktop/boto
python3 -m venv venv
source venv/bin/activate
pip install boto3
deactivate
```


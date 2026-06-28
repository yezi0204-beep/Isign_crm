import streamlit as st
from database import query_df, execute_sql, hash_password, check_password
from utils import get_user_map, clear_user_cache

def login(username: str, password: str):
    """登录验证，返回用户信息或 None"""
    user = query_df("SELECT username, password_hash, name, role FROM users WHERE username = ?", (username,))
    if user.empty:
        return None
    if check_password(password, user.iloc[0]['password_hash']):
        return {
            "u_id": username,
            "name": user.iloc[0]['name'],
            "role": user.iloc[0]['role']
        }
    return None

def change_password(username: str, old_pwd: str, new_pwd: str) -> bool:
    """修改密码"""
    user = query_df("SELECT password_hash FROM users WHERE username = ?", (username,))
    if user.empty or not check_password(old_pwd, user.iloc[0]['password_hash']):
        return False
    if len(new_pwd) < 3:
        return False
    new_hash = hash_password(new_pwd)
    execute_sql("UPDATE users SET password_hash = ? WHERE username = ?", (new_hash, username))
    return True